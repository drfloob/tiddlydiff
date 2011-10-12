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
###  CONFIG

# the base name of your wiki file. My file is "wiki.html"
TIDDLY_NAME="wiki"

# the folder your backups are saved in. Backups MUST be saved in a separate 
#   folder for this script to not jack up your wiki.
BKUP_DIR="bkup"

# the folder you want to store your diffs in.
DIFF_DIR="bkup.diffs"


###  END OF CONFIG
################################################################################



"""
REQUIREMENTS:

 * only works on *nix-compatible operating systems right now. Reuqires that you have
     `diff -u ...` and `cp` commands available.

ASSUMPTIONS:

 * tiddlywiki backups are stored in their own folder, which contains nothing but
      tiddlywiki backups.
 * tiddlywiki backud diffs will be stored in their own folder, which contains 
      nothing but tiddlywiki backup diffs.
"""


from os import mkdir, listdir, system, remove
from os.path import isdir, isfile, join
from pprint import pprint

backup_files = sorted(filter(lambda x: x.startswith(TIDDLY_NAME) and x.endswith(".html"), listdir(BKUP_DIR)))
#print backup_files

if not isdir(DIFF_DIR):
    mkdir(DIFF_DIR)
else:
    # dir existed. if an html file exists, append it to the backup_files list
    diffbasefiles = sorted(filter(lambda x: x.startswith(TIDDLY_NAME) and x.endswith(".html"), listdir(DIFF_DIR)))
    diffbasefile = max(diffbasefiles)


def doDiff(fn1, fn2, outfile):
    # just in case, don't overwrite any diffs
    if isfile(outfile):
        print "\t" + outfile + " ALREADY EXISTS!"
        print "\tdon't know how you want to deal with that. I quit."
        exit(1)

    # all is well, perform the diff
    system("diff -u " + fn1 + " " + fn2 + " > " + outfile)


### Diff the diffbasefile with the oldest tiddlywiki backup
if diffbasefile != "":
    print "Diffing previous base file against oldest tiddlywiki backup"
    outfile = join(DIFF_DIR, diffbasefile) + ".diff"
    fn1 = join(BKUP_DIR, min(backup_files))
    fn2 = join(DIFF_DIR, diffbasefile)
    doDiff(fn1, fn2, outfile)


### Do the rest of the diffs
for i in xrange(len(backup_files)-2, -1, -1):
    print len(backup_files) - i - 1, "of", len(backup_files)-1
    outfile = join(DIFF_DIR, backup_files[i]) + ".diff"
    fn1 = join(BKUP_DIR, backup_files[i+1])
    fn2 = join(BKUP_DIR, backup_files[i])
    doDiff(fn1, fn2, outfile)



### Copy the most recent backup file, on which the diff chain is based
system("cp " + join(BKUP_DIR, max(backup_files)) + " " + DIFF_DIR)

### Remove all other diff base files
print "Cleaning up old base files"
if diffbasefiles is not None:
    for i in diffbasefiles:
        remove(join(DIFF_DIR, i))

print "DONE."
