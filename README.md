compresses and restore your tiddlywiki backups using diffs.

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

