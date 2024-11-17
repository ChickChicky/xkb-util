# XKB Utility

Quick-and-dirty parser for X11 keyboard files

For now, it only supports *symbols* files, and is made to export a layout mapping into a C structrue that maps keys and characters to PS/2 keyboard scan codes.

# [naming.py](./naming.py)

Used to generate *charmap* for [xkb.py](#xkb.py). <br>
Might require root permissions.

# [xkb.py](./xkb.py)

Parses XKB symbol files for a specific layout and dumps the result.
