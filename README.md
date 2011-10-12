`tiddlydiff.py` compresses and restores your tiddlywiki backups using diffs.

I started a wiki one night on a whim, and turned on auto-save. After an hour of typing, the size of my backup folder was about 15M. That rate of growth would not be sustainable for long on this tiny laptop drive. So I whipped up `tiddlydiff` and shrank the total size of my backups to ~500K. That's a bit more sustainable, I think. I can live with that, as long as this script doesn't bork my backups!

Fwiw, this script may bork your backups.

## usage

   Note that this script *does not* remove your backups, but it *does* require you (re)move them yourself. `tiddlydiff` will fail if any backups it's already processed in a previous run are still in the backups folder on the next run. Leftover backup-file tolerance is on the todo list.

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


## configuration

If you're lazy like me, you'll want to hard-code your defaults for `TIDDLYNAME`, `BACKUPDIR`, and `DIFFDIR` in the first bit of the script, inside the box labeled "DEFAULT CONFIG". 


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

Tested on debian sid/wheezy with python 2.6.7 and tiddlywiki 2.6.5

## assumptions

 * tiddlywiki backups live in their own folder with nothing else.
 * tiddlywiki backup diffs live in their own separate folder as well, without anything else.

