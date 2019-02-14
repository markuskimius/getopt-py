#!/usr/bin/env python3

import sys, errno, os

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "lib")))
import getopt

def usage():
    print("Usage: example.py [option] [file]")
    print("")
    print("Example script to show how to use getopt.py")
    print("")
    print("Options:")
    print("  [file]                       Input file(s) [default=stdin]")
    print("  -o <file>, --output=<file>   Output file [default=stdout]")
    print("")
    print("  -n, --number[=start]         Show line numbers, starting at [start] if specified")
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

    while(True):
        c = getopt.getopt(sys.argv, { "o": 1, "output": 1, "n": [0,1], "number": [is_int,1], "H": is_int, "head": is_int, "h": 0, "help": 0 })
        if(c == -1): break

        if(c == '-'): opts.files.append(getopt.optarg)
        elif(c == 'o' or c == 'output'): opts.output = getopt.optarg
        elif(c == 'n' or c == 'number'):
            opts.number = True
            opts.offset = int(getopt.optarg) - 1
        elif(c == 'H' or c == 'head'): opts.head = int(getopt.optarg)
        elif(c == 'h' or c == 'help'): opts.help = True
        else: errcount += 1

    # Sanity check
    if(errcount > 0):
        print("", file=sys.stderr)
        print("Type '%s --help' for help" % sys.argv[0], file=sys.stderr)
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
            print(e, file=sys.stderr)
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
            print(e, file=sys.stderr)
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

        print(line, file=ofs)

    # Close input file
    if(ifs != sys.stdin):
        ifs.close()

def chomp(line):
    return line.rstrip('\n')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
        sys.exit(errno.EOWNERDEAD)

