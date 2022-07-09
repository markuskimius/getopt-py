"""An object-oriented getopt library for Python.

https://github.com/markuskimius/getopt-py
"""

__copyright__ = "Copyright 2019-2022 Mark Kim"
__license__ = "Apache 2.0"
__version__ = "1.0.4"
__author__ = "Mark Kim"
__all__ = ["getopts"]

import sys, re

class getopts(object):
    NONOPTION = "-"
    ERROR = "?"

    def __init__(self, argv, optstring):
        self.argv = argv
        self.optstring = optstring

        self.optarg = None
        self.optopt = None
        self.optind = 1

        self.__done = False
        self.__subind = 1

    def __iter__(self):
        return self

    def __next__(self):
        islong = False
        gotarg = False

        # Get the next argument
        if(self.optind < len(self.argv)):
            self.optarg = self.argv[self.optind]
            self.optind += 1
        else:
            raise StopIteration

        # If we previously encountered "--", we're done
        if(self.__done):
            return getopts.NONOPTION

        # Is this "--"? If so, get the next argument
        if(self.optarg == "--"):
            self.__done = True
            return next(self)

        # Is this a long option, short option, or an optionless argument?
        if(self.optarg[0:2] == "--"):
            self.optopt = self.optarg[2:]
            self.optarg = ""
            islong = True

            # --self.optopt=self.optarg
            if("=" in self.optopt):
                index = self.optopt.find("=")
                self.optarg = self.optopt[index+1:]
                self.optopt = self.optopt[:index]
                gotarg = True
        elif(self.optarg[0:1] == "-" and len(self.optarg) > 1):
            self.optopt = self.optarg[self.__subind]
            self.__subind += 1

            # Go to the next subindex
            if(self.__subind < len(self.optarg)):
                # We need to take back one index because we previously
                # increased prematurely previously.
                self.optind -= 1
            else:
                self.__subind = 1
        else:
            return getopts.NONOPTION

        # Is this a valid option?
        if(self.optopt in self.optstring.keys()):
            v_fn = self.optstring[self.optopt]
        else:
            sys.stderr.write("%s: invalid option -- '%s'\n" % (self.argv[0], self.optopt))
            return getopts.ERROR

        # Is the argument optional and/or have a default value?
        isargopt = False
        defalt = ""
        if(isinstance(v_fn,list)):
            isargopt = True
            defalt = v_fn[1] if(len(v_fn) > 1) else None
            v_fn = v_fn[0]

        # Does this option take an argument?
        if(v_fn == 0):
            # No - return with the default value, if any
            self.optarg = defalt

            return self.optopt

        # Is there an argument for us to read?
        if(islong and (gotarg or isargopt)):
            # Nothing to do
            pass
        elif(isargopt):
            # Short option, optional argument without space
            if(self.__subind > 1):
                self.optarg = self.argv[self.optind]
                self.optarg = self.optarg[self.__subind:]

                self.optind += 1
                self.__subind = 1
            else:
                self.optarg = defalt
                return self.optopt

        elif(self.optind < len(self.argv)):
            self.optarg = self.argv[self.optind]
            self.optind += 1

            # Short option, argument without space
            if(self.__subind > 1):
                self.optarg = self.optarg[self.__subind:]
                self.__subind = 1
        else:
            sys.stderr.write("%s: option requires an argument -- '%s'\n" % (self.argv[0], self.optopt))
            self.optarg = ''
            return getopts.ERROR

        # Do we need to validate the argument?
        if(isinstance(v_fn, int)):
            # No validation needed
            pass
        elif(self.optarg == "" and isargopt):
            # No argument specified and isn't required - use the default
            self.optarg = defalt
        elif(not callable(v_fn)):
            # We should never get here. Show error message then crash so the
            # developer can see the stacktrace and debug their code.
            raise Exception("%s: invalid validation function -- '%s'" % (self.argv[0], v_fn))
        elif(v_fn(self.optarg)):
            # Validation passed - nothing to do
            pass
        else:
            # Validation fail
            sys.stderr.write("%s: invalid argument to option '%s' -- '%s'\n" % (self.argv[0], self.optopt, self.optarg))
            return getopts.ERROR

        return self.optopt

    def next(self):
        return self.__next__()

