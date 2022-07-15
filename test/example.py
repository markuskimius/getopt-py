#!/bin/sh

##############################################################################
# BOOTSTRAP
#
# Include ../lib in the search path then call python3 or python.
# (Thanks to https://unix.stackexchange.com/questions/20880)
#
if "true" : '''\'
then
    export PYTHONPATH="$(dirname $0)/../lib:$PYTHONPATH"
    pythoncmd=python

    if command -v python3 >/dev/null; then
        pythoncmd=python3
    fi

    exec "$pythoncmd" "$0" "$@"
    exit 127
fi
'''

##############################################################################
# PYTHON CODE BEGINS HERE

import os
import sys
import errno
import getopts

__copyright__ = 'Copyright 2019-2022 Mark Kim'
__license__ = 'Apache 2.0'
__version__ = "1.0.5"
__author__ = "Mark Kim"


##############################################################################
# GLOBALS

SCRIPTNAME = os.path.basename(__file__)

class opts:
    files = []
    output = "-"
    number = False
    offset = 0
    head = 0
    help = False


##############################################################################
# USAGE

def usage():
    """\
Usage: {SCRIPTNAME} [option] [file]

Example script to show how to use object-oriented getopts.py.

Options:
  [file]                       Input file(s) [default=stdin]
  -o <file>, --output=<file>   Output file [default=stdout]

  -n[start], --number[=start]  Show line numbers, starting at [start] if specified
  -H <NUM>, --head=<NUM>       Head operation - show <NUM> lines

  -h, --help                   Show help screen (this screen)
"""

    print(usage.__doc__.format(**globals()))


##############################################################################
# MAIN

def main():
    ofs = sys.stdout
    errcount = 0

    getopt = getopts.getopts(sys.argv, {
        "h": 0         , "help"   : 0,
        "o": 1         , "output" : 1,
        "H": is_int    , "head"   : is_int,
        "n": [is_int,1], "number" : [is_int,1]
    })

    for c in getopt:
        if(c in ('-'))             : opts.files.append(getopt.optarg)
        elif(c in ('h', 'help'))   : opts.help = True
        elif(c in ('o', 'output')) : opts.output = getopt.optarg
        elif(c in ('H', 'head'))   : opts.head = int(getopt.optarg)
        elif(c in ('n', 'number')) :
            opts.number = True
            opts.offset = int(getopt.optarg) - 1
        else: errcount += 1

    # Sanity check
    if(errcount > 0):
        eprint("")
        eprint("Type '%s --help' for help" % sys.argv[0])
        sys.exit(1)

    # Help screen
    if(opts.help):
        usage()
        sys.exit(0)

    # Open output.  Consider "-" as stdout.
    if(opts.output != "-"):
        try:
            ofs = open(opts.output, "w")
        except IOError as e:
            eprint(e)
            sys.exit(1)

    # Read stdin by default
    if(len(opts.files) == 0):
        opts.files.append("-")

    # cat input files
    for file in opts.files:
        cat(ofs, file)

    ofs.close()


def is_int(s_int):
    isint = True

    try: int(s_int)
    except: isint = False

    return isint


def cat(ofs, file):
    global opts
    off = opts.offset
    ifs = sys.stdin
    count = 0

    # Open input file, enable line buffering
    if(file != "-"):
        try:
            ifs = open(file, "r")
        except iOError as e:
            eprint(e)
            sys.exit(1)

    # cat the file
    while(True):
        line = ifs.readline()
        if(line == ""): break

        count += 1
        line = chomp(line)

        # Head
        if(opts.head and count > opts.head): break

        # Line numbers
        if(opts.number > 0):
            num = count + off
            line = "%3d %s" % (num, line)

        ofs.write("%s\n" % line)

    # Close input file
    if(ifs != sys.stdin):
        ifs.close()


def chomp(line):
    return line.rstrip('\n')


def eprint(text):
    sys.stderr.write("%s\n" % text)


##############################################################################
# ENTRY POINT

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
        sys.exit(errno.EOWNERDEAD)


# vim:ft=python
