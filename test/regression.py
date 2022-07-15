#!/bin/bash

##############################################################################
# BOOTSTRAP
#
# Include ../lib in the search path then call python3 or python.
# (Thanks to https://unix.stackexchange.com/questions/20880)
#
if "true" : '''\'
then
    export PYTHONPATH="$(dirname $0)/../lib"
    pythoncmd=python

    if command -v python3 >/dev/null; then
        pythoncmd=python3
    fi

    echo "*** BASIC ***"
    "$pythoncmd" "$0" myarg1
    "$pythoncmd" "$0" -n
    "$pythoncmd" "$0" --no-arg
    "$pythoncmd" "$0" -w warg1
    "$pythoncmd" "$0" --with-arg warg1
    "$pythoncmd" "$0" --with-arg=warg1
    "$pythoncmd" "$0" -i1024
    "$pythoncmd" "$0" -i 1024
    "$pythoncmd" "$0" --integer 1024
    "$pythoncmd" "$0" --integer=1024
    "$pythoncmd" "$0" -o 128
    "$pythoncmd" "$0" -o128
    "$pythoncmd" "$0" --opt-arg 128
    "$pythoncmd" "$0" --opt-arg=128

    echo "*** REPETITIONS ***"
    "$pythoncmd" "$0" myarg1 myarg2
    "$pythoncmd" "$0" -nn
    "$pythoncmd" "$0" --no-arg --no-arg
    "$pythoncmd" "$0" -w warg1 -w warg2
    "$pythoncmd" "$0" -wwarg1 -wwarg2
    "$pythoncmd" "$0" --with-arg warg1 --with-arg warg2
    "$pythoncmd" "$0" --with-arg=warg1 --with-arg=warg2
    "$pythoncmd" "$0" -i1024 -i2048
    "$pythoncmd" "$0" -i 1024 -i 2048
    "$pythoncmd" "$0" --integer 1024 --integer 2048
    "$pythoncmd" "$0" --integer=1024 --integer=2048
    "$pythoncmd" "$0" -o 128 -o 256
    "$pythoncmd" "$0" -o128 -o256
    "$pythoncmd" "$0" --opt-arg 128 --opt-arg 256
    "$pythoncmd" "$0" --opt-arg=128 --opt-arg=256

    echo "*** COMBINATION (RELATED) ***"
    "$pythoncmd" "$0" -n --no-arg
    "$pythoncmd" "$0" -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4
    "$pythoncmd" "$0" -i1024 -i 2048 --integer 3072 --integer=4096

    echo "*** COMBINATION (COMPREHENSIVE) ***"
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1
    "$pythoncmd" "$0" --no-arg -nwwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1
    "$pythoncmd" "$0" --no-arg -wwarg1 -nw warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1
    "$pythoncmd" "$0" --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -ni1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1
    "$pythoncmd" "$0" --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -ni 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1
    "$pythoncmd" "$0" --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1 -n
    "$pythoncmd" "$0" --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 -n myarg1
    "$pythoncmd" "$0" --no-arg -w warg1 --with-arg warg2 --with-arg=warg3 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1 -nwwarg4
    "$pythoncmd" "$0" --no-arg -w warg1 --with-arg warg2 --with-arg=warg3 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 -nwwarg4 myarg1
    "$pythoncmd" "$0" --no-arg -wwarg1 --with-arg warg2 --with-arg=warg3 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1 -nw warg4
    "$pythoncmd" "$0" --no-arg -wwarg1 --with-arg warg2 --with-arg=warg3 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 -nw warg4 myarg1
    "$pythoncmd" "$0" --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i 1024 --integer 2048 --integer=3072 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1 -ni4096
    "$pythoncmd" "$0" --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i 1024 --integer 2048 --integer=3072 -o 32 -o64 --opt-arg 128 --opt-arg=256 -ni4096 myarg1
    "$pythoncmd" "$0" --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 --integer 2048 --integer=3072 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1 -ni 4096
    "$pythoncmd" "$0" --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 --integer 2048 --integer=3072 -o 32 -o64 --opt-arg 128 --opt-arg=256 -ni 4096 myarg1

    echo "*** EMPTY ARGS ***"
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w "" --with-arg warg2 --with-arg=warg3 -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --with-arg "" --with-arg=warg3 -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg= -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 -i1024 -i 1024 --integer 2048 --integer=3072 myarg1 --with-arg=
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 -i1024 -i 1024 --integer 2048 --integer=3072 --with-arg= myarg1
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w "" --opt-arg warg2 --opt-arg=warg3 -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --opt-arg "" --opt-arg=warg3 -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --opt-arg warg3 --opt-arg= -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --opt-arg warg3 -i1024 -i 1024 --integer 2048 --integer=3072 myarg1 --opt-arg=
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --opt-arg warg3 -i1024 -i 1024 --integer 2048 --integer=3072 --opt-arg= myarg1
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w "" -o warg2 -owarg3 -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 -o "" -owarg3 -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 -o warg3 -o "" -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 -o warg3 -i1024 -i 1024 --integer 2048 --integer=3072 myarg1 -o ""
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 -o warg3 -i1024 -i 1024 --integer 2048 --integer=3072 -o "" myarg1

    echo "*** EXCEPTIONS (EMPTY INTEGER ARGS) ***"
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i "" --integer 2048 --integer=3072 myarg1
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer "" --integer=3072 myarg1
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer 3072 --integer= myarg1

    echo "*** EXCEPTIONS (MISSING MANDATORY ARGS) ***"
    "$pythoncmd" "$0" -n --no-arg -w warg1 --with-arg warg2 --with-arg=warg3 -i1024 -i 1024 --integer 2048 --integer=3072 myarg1 -w
    "$pythoncmd" "$0" -n --no-arg -wwarg1 --with-arg warg2 --with-arg=warg3 -i1024 -i 1024 --integer 2048 --integer=3072 myarg1 -w
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --with-arg=warg3 -i1024 -i 1024 --integer 2048 --integer=3072 myarg1 --with-arg
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i 1024 --integer 2048 --integer=3072 myarg1 -i
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 --integer 2048 --integer=3072 myarg1 -i
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer=3072 myarg1 --integer
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer 3072 --integer= myarg1
    "$pythoncmd" "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer 3072 myarg1 --integer=

    exit 0
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
__version__ = "1.0.4"
__author__ = "Mark Kim"


##############################################################################
# MAIN

def main(args):
    print("  target %s:" % ' '.join(map(lambda x: x if len(x) else '{}', args[1:])))
    sys.stdout.flush()
    output = target(args)

    for name in sorted(output.keys()):
        values = output[name]

        if len(values):
            print("  %s = %s" % (name, ' '.join(values)))

    print('')


def target(args):
    opts = {
        '-|opts'  : [],
        '-|index' : [],
        '0'       : [],
        'n'       : [],
        'w'       : [],
        'i'       : [],
        'o'       : [],
        'x'       : [],
    }

    getopt = getopts.getopts(args, {
        "n": 0               , "no-arg"   : 0,
        "w": 1               , "with-arg" : 1,
        "i": is_int          , "integer"  : is_int,
        "o": [is_int,"null"] , "opt-arg"  : [is_int,"null"],
    })

    for c in getopt:
        optopt = '0' if c == '-' else getopt.optopt
        optind = str(getopt.optind-1)
        optarg = getopt.optarg if len(getopt.optarg) else '{}'

        opts['-|opts'].append(optopt)
        opts['-|index'].append(optind)

        if(c in ('-'))               : opts['0'].append(optarg)
        elif(c in ('n', 'no-arg'))   : opts['n'].append(optarg)
        elif(c in ('w', 'with-arg')) : opts['w'].append(optarg)
        elif(c in ('i', 'integer'))  : opts['i'].append(optarg)
        elif(c in ('o', 'opt-arg'))  : opts['o'].append(optarg)
        else                         : opts['x'].append(optarg)

    return opts


def is_int(s_int):
    isint = True

    try: int(s_int)
    except: isint = False

    return isint


##############################################################################
# ENTRY POINT

if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("")
        sys.exit(errno.EOWNERDEAD)


# vim:ft=python
