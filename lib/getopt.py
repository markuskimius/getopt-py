"""A getopt library for Python.

https://github.com/markuskimius/getopt-py
"""

import sys, re

__copyright__ = "Copyright 2019 Mark Kim"
__license__ = "Apache 2.0"

# Public
optarg = None
optopt = None
optind = None

# Private
__argv = None
__optstring = None
__subind = None
__done = None

# Constants
__NONOPTION = "-"
__ERROR = "?"
__EOF = -1

def getopt(argv, optstring):
    global optarg, optopt, optind
    global __argv, __optstring, __subind, __done
    global __NONOPTION, __ERROR, __EOF
    islong = False
    gotarg = False

    # Initialize
    if(argv != __argv or optstring != __optstring):
        optind = 1
        __done = False
        __argv = argv
        __optstring = optstring
        __subind = 1

    # Get the next argument
    if(optind < len(__argv)):
        optarg = __argv[optind]
        optind += 1
    else:
        return __EOF

    # If we previously encountered "--", we're done
    if(__done):
        return __NONOPTION

    # Is this "--"? If so, get the next argument
    if(optarg == "--"):
        __done = True
        return getopt(argv, optstring)

    # Is this a long option, short option, or an optionless argument?
    if(optarg[0:2] == "--"):
        optopt = optarg[2:]
        optarg = ""
        islong = True

        # --optopt=optarg
        if("=" in optopt):
            index = optopt.find("=")
            optarg = optopt[index+1:]
            optopt = optopt[:index]
            gotarg = True
    elif(optarg[0] == "-" and len(optarg) > 1):
        optopt = optarg[__subind]
        __subind += 1

        # Go to the next subindex
        if(__subind < len(optarg)):
            # We need to take back one index because we previously
            # increased prematurely previously.
            optind -= 1
        else:
            __subind = 1
    else:
        return __NONOPTION

    # Is this a valid option?
    if(optopt in __optstring.keys()):
        v_fn = __optstring[optopt]
    else:
        sys.stderr.write("%s: invalid option -- '%s'\n" % (__argv[0], optopt))
        return __ERROR

    # Is the argument optional and/or have a default value?
    isargopt = False
    defalt = ""
    if(isinstance(v_fn,list)):
        isargopt = True
        defalt = v_fn[1] if(len(v_fn) > 1) else ""
        v_fn = v_fn[0]

    # Does this option take an argument?
    if(v_fn == 0):
        # No - return with the default value, if any
        optarg = defalt

        return optopt

    # Is there an argument for us to read?
    if(islong and (gotarg or isargopt)):
        # Nothing to do
        pass
    elif(isargopt):
        # Short option, optional argument without space
        if(__subind > 1):
            optarg = __argv[optind]
            optarg = optarg[__subind:]

            optind += 1
            __subind = 1
        else:
            optarg = defalt
    elif(optind < len(__argv)):
        optarg = __argv[optind]
        optind += 1

        # Short option, argument without space
        if(__subind > 1):
            optarg = optarg[__subind:]
            __subind = 1
    else:
        sys.stderr.write("%s: option requires an argument -- '%s'\n" % (__argv[0], optopt))
        return __ERROR

    # Do we need to validate the argument?
    if(optarg == "" and isargopt):
        # No argument specified and isn't required - use the default
        optarg = defalt
    elif(isinstance(v_fn, int)):
        # No validation needed
        pass
    elif(not callable(v_fn)):
        # We should never get here. Show error message then crash so the
        # developer can see the stacktrace and debug their code.
        raise Exception("%s: invalid validation function -- '%s'" % (__argv[0], v_fn))
    elif(v_fn(optarg)):
        # Validation passed - nothing to do
        pass
    else:
        # Validation fail
        sys.stderr.write("%s: invalid argument to option '%s' -- '%s'\n" % (__argv[0], optopt, optarg))
        return __ERROR

    return optopt

