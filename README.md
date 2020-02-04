# getopt-py
A getopt library for Python.


## Motivation

Python already has several argument parers. But the [C-style getopt parser]
that comes with the standard Python library does not take advantage of the
flexible syntax of a script language. And the [argparse] parser does not allow
for the ordered processing of the arguments. This library was ported to Python
from [getopt-tcl] to fill this gap.


## Features

The feature set is based on GNU `getopt_long`:

- Short options. Options may be combined (`-a -b -c` is equivalent to `-abc`).
  Option arguments, if any, may appear with or without a space (`-o value` is
  equivalent to `-ovalue`).
- Long options. Option arguments, if any, may appear with or without an equal sign
  (`--option value` is equivalent to `--option=value`).
- Optional arguments are supported. The optional argument for a short option
  must be specified without a space (`-ovalue`) and for a long option must be
  specified with an equal sign (`--option=value`).
- Options (with or without arguments) and optionless arguments may appear in
  any order.
- `--` can be used to denote the end of options.


## Usage
```python
c = getopt.getopt(argv, optstring)
```

All parameters are mandatory:
- `argv` - The argument list (e.g., sys.argv[1:])
- `optstring` - A dictionary containing the valid options and a specification
  of whether they take an argument. The keys are the options. The value may be
  `0` if the option takes no argument, or `1` if it takes an argument. Instead
  of `0` or `1`, it may specify a validation function that returns `1` if the
  argument is valid, or `0` otherwise. To specify the argument as optional,
  surround it in brackets (make it a list), with the optional second element
  specifying the default value.

The function returns a single value which may be one of:
- `-1`: End of `argv` processing.
- `-`: An optionless argument. The value of the argument is stored in `getopt.optarg`.
- `?`: An invalid option. An error message has been printed to `getopt.stderr` and the
  option that caused the error is stored in `getopt.optopt`.
- All other values: A valid option. This value is also stored in `getopt.optopt`. If
  the option takes an argument, the value is stored in `getopt.optarg`.

The following variable names are available:
- `getopt.optind`: The index of the next `argv`.
- `getopt.optopt`: The last option processed.
- `getopt.optarg`: The argument to the last option.



## Example
```python
while True:
    c = getopt.getopt(sys.argv[1:], {
        "h": 0         , "help"   : 0,
        "o": 1         , "output" : 1,
        "p": is_port   , "port"   : is_port,
        "v": [is_int,1], "verbose": [is_int,1]
    })

    if c == -1 : break
    elif c in ("-")           : opts.files.append(getopt.optarg)
    elif c in ("h", "help")   : usage() ; sys.exit(0)
    elif c in ("o", "output") : opts.output  = getopt.optarg
    elif c in ("p", "port")   : opts.port    = int(getopt.optarg)
    elif c in ("v", "verbose"): opts.verbose = int(getopt.optarg)
    else: sys.exit(1)
```

In the above example, single character options `h`, `o`, `p`, `v` may be
specified with a single hyphen (`-h`, `-o`, `-p`, `-v`). Two hyphens are also
accepted. The others must be specified with two hyphens (`--help`,
`--output`, `--port`, `--verbose`).

- `-h` and `--help` take no arguments since the value that follows each is 0.
- `-o` and `--output` take any argument since the value that follows each is 1.
- `-p` and `--port` take an argument whose value must pass a test by `is_port`.
  For example,

```python
def is_port(value):
    isport = False

    if(isinstance(value, int) and int(value) >= 1024 and int(value) < 65536):
        isport = True

    return isport
```

Finally, `-v` and `--verbose` take an optional argument whose value, if any,
must pass the test by `is_int`. If no argument is specified, `getopt.optarg`
defaults to `1`.

See [example.py] for a more complete example.


## Object-Oriented Version

An object-oriented version of the library is also provided, accessible via the
plural `getopts` (note the `s` at the end).  The usage is almost identical as
the aforementioned procedural version, `getopt`, but it is only called once to
initialize, and it returns an iterator:
```python
getopt = getopts.getopts(sys.argv, {
    "h": 0         , "help"   : 0,
    "o": 1         , "output" : 1,
    "p": is_port   , "port"   : is_port,
    "v": [is_int,1], "verbose": [is_int,1]
})

for c in getopt:
    if c in ("-")             : opts.files.append(getopt.optarg)
    elif c in ("h", "help")   : usage() ; sys.exit(0)
    elif c in ("o", "output") : opts.output  = getopt.optarg
    elif c in ("p", "port")   : opts.port    = int(getopt.optarg)
    elif c in ("v", "verbose"): opts.verbose = int(getopt.optarg)
    else: sys.exit(1)
```

See [example-oo.py] for a more complete example.


## License

[Apache 2.0]


[C-style getopt parser]: <https://docs.python.org/3.1/library/getopt.html>
[argparse]: <https://docs.python.org/3/library/argparse.html>
[getopt-tcl]: <https://github.com/markuskimius/getopt-tcl/>
[example.py]: <https://github.com/markuskimius/getopt-py/blob/master/test/example.py>
[example-oo.py]: <https://github.com/markuskimius/getopt-py/blob/master/test/example-oo.py>
[Apache 2.0]: <https://github.com/markuskimius/getopt-py/blob/master/LICENSE>

