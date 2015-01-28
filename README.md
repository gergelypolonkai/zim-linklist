Link listing for Zim
====================

List all links in your [Zim](http://zim-wiki.org/) notebook, prefixed
with an `E` for existing or `M` for missing pages.

Installation
------------

Download/clone this repository in your `$XDG_DATA_HOME/zim/plugins`
(usually it is in `~/.local/share`).

Usage
-----

Open a terminal and enter

    $ zim --plugin linklist --notebook <notebook name>

Add `--missing-only` or `--existing-only` to list only dangling or
existing pages.
