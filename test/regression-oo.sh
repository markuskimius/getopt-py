#!/bin/bash

if "true" : '''\'
then
    export PYTHONPATH="$(dirname $0)/../lib"

    echo "*** BASIC ***"
    python3 "$0" myarg1
    python3 "$0" -n
    python3 "$0" --no-arg
    python3 "$0" -w warg1
    python3 "$0" --with-arg warg1
    python3 "$0" --with-arg=warg1
    python3 "$0" -i1024
    python3 "$0" -i 1024
    python3 "$0" --integer 1024
    python3 "$0" --integer=1024
    python3 "$0" -o 128
    python3 "$0" -o128
    python3 "$0" --opt-arg 128
    python3 "$0" --opt-arg=128

    echo "*** REPETITIONS ***"
    python3 "$0" myarg1 myarg2
    python3 "$0" -nn
    python3 "$0" --no-arg --no-arg
    python3 "$0" -w warg1 -w warg2
    python3 "$0" -wwarg1 -wwarg2
    python3 "$0" --with-arg warg1 --with-arg warg2
    python3 "$0" --with-arg=warg1 --with-arg=warg2
    python3 "$0" -i1024 -i2048
    python3 "$0" -i 1024 -i 2048
    python3 "$0" --integer 1024 --integer 2048
    python3 "$0" --integer=1024 --integer=2048
    python3 "$0" -o 128 -o 256
    python3 "$0" -o128 -o256
    python3 "$0" --opt-arg 128 --opt-arg 256
    python3 "$0" --opt-arg=128 --opt-arg=256

    echo "*** COMBINATION (RELATED) ***"
    python3 "$0" -n --no-arg
    python3 "$0" -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4
    python3 "$0" -i1024 -i 2048 --integer 3072 --integer=4096

    echo "*** COMBINATION (COMPREHENSIVE) ***"
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1
    python3 "$0" --no-arg -nwwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1
    python3 "$0" --no-arg -wwarg1 -nw warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1
    python3 "$0" --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -ni1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1
    python3 "$0" --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -ni 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1
    python3 "$0" --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1 -n
    python3 "$0" --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 -n myarg1
    python3 "$0" --no-arg -w warg1 --with-arg warg2 --with-arg=warg3 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1 -nwwarg4
    python3 "$0" --no-arg -w warg1 --with-arg warg2 --with-arg=warg3 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 -nwwarg4 myarg1
    python3 "$0" --no-arg -wwarg1 --with-arg warg2 --with-arg=warg3 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1 -nw warg4
    python3 "$0" --no-arg -wwarg1 --with-arg warg2 --with-arg=warg3 -i1024 -i 2048 --integer 3072 --integer=4096 -o 32 -o64 --opt-arg 128 --opt-arg=256 -nw warg4 myarg1
    python3 "$0" --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i 1024 --integer 2048 --integer=3072 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1 -ni4096
    python3 "$0" --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i 1024 --integer 2048 --integer=3072 -o 32 -o64 --opt-arg 128 --opt-arg=256 -ni4096 myarg1
    python3 "$0" --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 --integer 2048 --integer=3072 -o 32 -o64 --opt-arg 128 --opt-arg=256 myarg1 -ni 4096
    python3 "$0" --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 --integer 2048 --integer=3072 -o 32 -o64 --opt-arg 128 --opt-arg=256 -ni 4096 myarg1

    echo "*** EMPTY ARGS ***"
    python3 "$0" -n --no-arg -wwarg1 -w "" --with-arg warg2 --with-arg=warg3 -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --with-arg "" --with-arg=warg3 -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg= -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 -i1024 -i 1024 --integer 2048 --integer=3072 myarg1 --with-arg=
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 -i1024 -i 1024 --integer 2048 --integer=3072 --with-arg= myarg1
    python3 "$0" -n --no-arg -wwarg1 -w "" --opt-arg warg2 --opt-arg=warg3 -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --opt-arg "" --opt-arg=warg3 -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --opt-arg warg3 --opt-arg= -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --opt-arg warg3 -i1024 -i 1024 --integer 2048 --integer=3072 myarg1 --opt-arg=
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --opt-arg warg3 -i1024 -i 1024 --integer 2048 --integer=3072 --opt-arg= myarg1
    python3 "$0" -n --no-arg -wwarg1 -w "" -o warg2 -owarg3 -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    python3 "$0" -n --no-arg -wwarg1 -w warg2 -o "" -owarg3 -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    python3 "$0" -n --no-arg -wwarg1 -w warg2 -o warg3 -o "" -i1024 -i 2048 --integer 3072 --integer=4096 myarg1
    python3 "$0" -n --no-arg -wwarg1 -w warg2 -o warg3 -i1024 -i 1024 --integer 2048 --integer=3072 myarg1 -o ""
    python3 "$0" -n --no-arg -wwarg1 -w warg2 -o warg3 -i1024 -i 1024 --integer 2048 --integer=3072 -o "" myarg1

    echo "*** EXCEPTIONS (EMPTY INTEGER ARGS) ***"
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i "" --integer 2048 --integer=3072 myarg1
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer "" --integer=3072 myarg1
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer 3072 --integer= myarg1

    echo "*** EXCEPTIONS (MISSING MANDATORY ARGS) ***"
    python3 "$0" -n --no-arg -w warg1 --with-arg warg2 --with-arg=warg3 -i1024 -i 1024 --integer 2048 --integer=3072 myarg1 -w
    python3 "$0" -n --no-arg -wwarg1 --with-arg warg2 --with-arg=warg3 -i1024 -i 1024 --integer 2048 --integer=3072 myarg1 -w
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --with-arg=warg3 -i1024 -i 1024 --integer 2048 --integer=3072 myarg1 --with-arg
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i 1024 --integer 2048 --integer=3072 myarg1 -i
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 --integer 2048 --integer=3072 myarg1 -i
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer=3072 myarg1 --integer
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer 3072 --integer= myarg1
    python3 "$0" -n --no-arg -wwarg1 -w warg2 --with-arg warg3 --with-arg=warg4 -i1024 -i 2048 --integer 3072 myarg1 --integer=

    exit 0
fi
'''

import sys, os, errno, getopts


def test(args):
    print("  target %s:" % ' '.join(map(lambda x: x if len(x) else '{}', args)))
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
        optind = str(getopt.optind)
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


if __name__ == "__main__":
    try:
        test(sys.argv[1:])
    except KeyboardInterrupt:
        print("")
        sys.exit(errno.EOWNERDEAD)


# vim:ft=python
