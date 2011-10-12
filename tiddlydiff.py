#!/usr/bin/env python
"""Compresses your tiddlywiki backups using diffs."""

__author__ = "aj heller"
__email__ = "aj@drfloob.com"
__license__ = """

/*
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 42):
 * <aj@drfloob.com> wrote this file. As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer in return. AJ Heller
 * ----------------------------------------------------------------------------
 */

"""



################################################################################
###  DEFAULT CONFIG - these can all be overriden by command line options

# the base name of your wiki file. My file is "wiki.html"
TIDDLY_NAME="wiki"

# the folder your backups are saved in. Backups MUST be saved in a separate 
#   folder for this script to not jack up your wiki.
BKUP_DIR="bkup"

# the folder you want to store your diffs in.
DIFF_DIR="bkup.diffs"


###  END CONFIG
################################################################################



from os import mkdir, listdir, system, remove
from os.path import isdir, isfile, join, basename
from pprint import pprint
import shutil


from optparse import OptionParser, OptionGroup # python 2.3 to 2.6

parser = OptionParser("%prog command [config] [options]")
commandGroup = OptionGroup(parser, "Commands")
commandGroup.add_option("-b", "--backup", action="store_true", dest="doBackup",
                  help="convert your backups to diffs")
commandGroup.add_option("-r", "--restore", dest="restoreFile", 
                  help="restore a version of your wiki from backup diffs; takes the name (with optional path) of the diff to be restored; creates a new html file in your backup diffs folder.")
parser.add_option_group(commandGroup)

configGroup = OptionGroup(parser, "Config", "folder and various config options")
configGroup.add_option("-n", "--name", dest="tiddlyName", default=TIDDLY_NAME,
                       help="name of the wiki file (e.g. 'wiki' for wiki.html)")
configGroup.add_option("-k", "--bkdir", dest="backupDir", default=BKUP_DIR,
                       help="path to normal tiddlywiki backup folder")
configGroup.add_option("-f", "--diffdir", dest="diffDir", default=DIFF_DIR,
                       help="path to backup diff destination folder")
parser.add_option_group(configGroup)


def make_backup():

    tn = options.tiddlyName
    bd = options.backupDir
    dd = options.diffDir

    backup_files = sorted(filter(lambda x: x.startswith(tn) and x.endswith(".html"), listdir(bd)))

    if not isdir(dd):
        mkdir(dd)
    else:
        # dir existed. if an html file exists, append it to the backup_files list
        diffbasefiles = sorted(filter(lambda x: x.startswith(tn) and x.endswith(".html"), listdir(dd)))
        diffbasefile = max(diffbasefiles)


    def doDiff(fn1, fn2, outfile):
        # just in case, don't overwrite any diffs
        if isfile(outfile):
            print "\t" + outfile + " ALREADY EXISTS!"
            print "\tdon't know how you want to deal with that. I quit."
            exit(1)

        # all is well, perform the diff
        system(" ".join(["diff -u", fn1, fn2, ">", outfile]))
        
    # @TODO: smarter filtering: just diff the files that haven't been diffed yet, based on the diff base file

    ### Diff the diffbasefile with the oldest tiddlywiki backup
    if diffbasefile != "":
        print "Diffing previous base file against oldest tiddlywiki backup"
        outfile = join(dd, diffbasefile) + ".diff"
        fn1 = join(bd, min(backup_files))
        fn2 = join(dd, diffbasefile)
        doDiff(fn1, fn2, outfile)


    ### Do the rest of the diffs
    for i in xrange(len(backup_files)-2, -1, -1):
        print len(backup_files) - i - 1, "of", len(backup_files)-1
        outfile = join(dd, backup_files[i]) + ".diff"
        fn1 = join(bd, backup_files[i+1])
        fn2 = join(bd, backup_files[i])
        doDiff(fn1, fn2, outfile)



    ### Copy the most recent backup file, on which the diff chain is based
    shutil.copy(join(bd, max(backup_files)), dd)

    ### Remove all other diff base files
    print "Cleaning up old base files"
    if diffbasefiles is not None:
        for i in diffbasefiles:
            remove(join(dd, i))

    print "DONE."



def restore_file():
    # make sure file exists in diffs

    rf = basename(options.restoreFile)
    if rf.endswith(".diff"):
        rf = rf[0:-5]
    if not rf.endswith(".html"):
        print("invalid file")
        exit(1)
    rfd = rf + ".diff"

    dd = options.diffDir
    if not isfile(join(dd, rfd)):
        print("file not found")
        exit(1)

    # copy base diff file with desired name
    diffs = sorted(listdir(dd))
    diffbasefiles = filter(lambda x: x.startswith(options.tiddlyName) and x.endswith(".html"), diffs)
    diffbasefile = max(diffbasefiles)
    pdbf = join(dd, diffbasefile)
    prf = join(dd, rf)
    shutil.copyfile(pdbf, prf)

    # filter diffs to only those we want to apply
    keepdiffs = filter(lambda x: x > rfd and x.endswith(".diff"), diffs)

    # apply in order, newest to oldest
    for i in xrange(len(keepdiffs)-1,-1,-1):
        ppf = join(dd, keepdiffs[i])
        system(" ".join(["patch", "-u", prf, ppf]))

    print "DONE"

def parserError(str):
    print "ERROR:", str, "\n"
    parser.print_help()
    exit(1)

if __name__ == "__main__":
    (options, args) = parser.parse_args()

    if len(args) > 0:
        parserError("couldn't parse arguments; incorrect usage")
    if options.doBackup and options.restoreFile:
        parserError("you can only run one command at a time")

    if options.doBackup:
        make_backup()
    elif options.restoreFile:
        restore_file()
    else:
        parserError("no command given")
    
