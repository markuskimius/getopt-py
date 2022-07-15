# getopt-py

A classic getopt library for Python with long options and optional arguments
support.


## Motivation

For developers that find [argparse] too constraining.


## Example

```python
import getopts

...

getopt = getopts.getopts(sys.argv, {
    "h": 0         , "help"   : 0,
    "o": 1         , "output" : 1,
    "p": is_port   , "port"   : is_port,
    "v": [is_int,1], "verbose": [is_int,1]
})

for c in getopt:
    if   c in ("-")           : opts.files.append(getopt.optarg)
    elif c in ("h", "help")   : usage() ; sys.exit(0)
    elif c in ("o", "output") : opts.output  = getopt.optarg
    elif c in ("p", "port")   : opts.port    = int(getopt.optarg)
    elif c in ("v", "verbose"): opts.verbose = int(getopt.optarg)
    else: sys.exit(1)
```

- `-h` and `--help` take no arguments (0).
- `-o` and `--output` take any argument (1).
- `-p` and `--port` take an argument that, when passed to the `is_port`
  function, returns True.
- `-v` and `--verbose` take an optional argument that, when passed to the
  `is_int` function, returns True.  If no argument is specified, it defaults to
  `1`.

See [example.py] for a more complete example.


## Features

The features are based on GNU `getopt_long`:

- Short options.  Options may be combined (`-a -b -c` is equivalent to `-abc`).
  If the option takes a mandatory argument, the argument may appear with or
  without whitespaces (`-o value` is equivalent to `-ovalue`).

- Long options.  If the option takes a mandatory argument, the argument may
  appear with or without an equal sign (`--option value` is equivalent to
  `--option=value`).

- Optional arguments. If the option takes an optional argument, the argument
  must appear without a space after a short option (`-ovalue`) or with an equal
  sign after a long option (`--option=value`).

- Options may appear in any order.

- `--` can be used to denote the end of options.


## Installation

With pip:

```
pip install getopts
```
(note the plural 's')

With [dpm]:
```
dpm install https://github.com/markuskimius/getopt-py.git
```


## Usage

```python
getopts.getopts(argv, optdict)
```

All parameters are mandatory:
- `argv` - The argument list (e.g., sys.argv)
- `optdict` - A dictionary containing the valid options and a specification
  of whether they take an argument. The keys are the options. The value may be
  `0` if the option takes no argument, or `1` if it takes an argument. Instead
  of `0` or `1`, it may specify a validation function that returns `1` if the
  argument is valid, or `0` otherwise. To specify the argument as optional,
  surround it in brackets (make it a list), with the optional second element
  specifying the default value.

The function returns an iterable object that, if evaluated, returns one of the
following:
- `-`: An optionless argument.  The value of the argument is stored in `getopt.optarg`.
- `?`: An invalid option. An error message has been printed to `getopt.stderr` and the
  option that caused the error is stored in `getopt.optopt`.
- All other values: A valid option.  This value is also stored in `getopt.optopt`.  If
  the option takes an argument, the value is stored in `getopt.optarg`.

The following variable names are available:
- `getopt.optind`: The index of the next `argv`.
- `getopt.optopt`: The last option processed.
- `getopt.optarg`: The argument to the last option.


## License

[Apache 2.0]


[C-style getopt parser]: <https://docs.python.org/3.1/library/getopt.html>
[argparse]: <https://docs.python.org/3/library/argparse.html>
[getopt-tcl]: <https://github.com/markuskimius/getopt-tcl/>
[example.py]: <https://github.com/markuskimius/getopt-py/blob/master/test/example.py>
[Apache 2.0]: <https://github.com/markuskimius/getopt-py/blob/master/LICENSE>
[dpm]: <https://github.com/markuskimius/dpm>

