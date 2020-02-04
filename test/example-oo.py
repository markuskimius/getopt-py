#!/bin/sh

# Include ../lib in the search path so we can find getopt.py
# (Thanks to https://unix.stackexchange.com/questions/20880)
if "true" : '''\'
then
    exec env PYTHONPATH="$(dirname $0)/../lib" python3 "$0" "$@"
    exit 127
fi
'''

import sys, os, errno, getopts

def usage():
    print("Usage: example-oo.py [option] [file]")
    print("")
    print("Example script to show how to use object-oriented getopts.py.")
    print("")
    print("Options:")
    print("  [file]                       Input file(s) [default=stdin]")
    print("  -o <file>, --output=<file>   Output file [default=stdout]")
    print("")
    print("  -n[start], --number[=start]  Show line numbers, starting at [start] if specified")
    print("  -H <NUM>, --head=<NUM>       Head operation - show <NUM> lines")
    print("")
    print("  -h, --help                   Show help screen (this screen)")
    print("")

class opts:
    files = []
    output = "-"
    number = False
    offset = 0
    head = 0
    help = False

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

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
        sys.exit(errno.EOWNERDEAD)

