Compresses your tiddlywiki backups using diffs.

## License

    /*
     * ----------------------------------------------------------------------------
     * "THE BEER-WARE LICENSE" (Revision 42):
     * <aj@drfloob.com> wrote this file. As long as you retain this notice you
     * can do whatever you want with this stuff. If we meet some day, and you think
     * this stuff is worth it, you can buy me a beer in return. AJ Heller
     * ----------------------------------------------------------------------------
    */


## REQUIREMENTS:

 * only works on *nix-compatible operating systems right now. Reuqires that you have
     `diff -u ...` and `cp` commands available to create diffs, and `patch -u ...` 
     to get back your original files.

## ASSUMPTIONS:

 * tiddlywiki backups are stored in their own folder, which contains nothing but
      tiddlywiki backups.
 * tiddlywiki backud diffs will be stored in their own folder, which contains 
      nothing but tiddlywiki backup diffs.


