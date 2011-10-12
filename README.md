compresses and restore your tiddlywiki backups using diffs.

## usage

    Usage: tiddlydiff.py command [config] [options]
    
    Options:
      -h, --help            show this help message and exit

      Commands:
	-b, --backup        convert your backups to diffs
	-r RESTOREFILE, --restore=RESTOREFILE
			    restore a version of your wiki from backup diffs;
			    takes the name (with optional path) of the diff to be
			    restored; creates a new html file in your backup diffs
			    folder.
    
      Config:
	folder and various config options

	-n TIDDLYNAME, --name=TIDDLYNAME
			    name of the wiki file (e.g. 'wiki' for wiki.html)
	-k BACKUPDIR, --bkdir=BACKUPDIR
			    path to normal tiddlywiki backup folder
	-f DIFFDIR, --diffdir=DIFFDIR
			    path to backup diff destination folder

## license

    /*
     * ----------------------------------------------------------------------------
     * "THE BEER-WARE LICENSE" (Revision 42):
     * <aj@drfloob.com> wrote this file. As long as you retain this notice you
     * can do whatever you want with this stuff. If we meet some day, and you think
     * this stuff is worth it, you can buy me a beer in return. AJ Heller
     * ----------------------------------------------------------------------------
    */


## system requirements

 * `diff -u ...` and `patch -u ...` commands must be available on your system.

## assumptions

 * tiddlywiki backups live in their own folder with nothing else.
 * tiddlywiki backup diffs live in their own separate folder as well, without anything else.

