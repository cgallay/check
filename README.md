# check
Python lib to check argument pass to a function at run time.

[![Build Status](https://travis-ci.org/cgallay/check.svg?branch=master)](https://travis-ci.org/cgallay/check)
[![Coverage Status](https://coveralls.io/repos/github/cgallay/check/badge.svg?branch=master)](https://coveralls.io/github/cgallay/check?branch=master)

## Install

``` bash
git clone git@github.com:cgallay/check.git
cd check
pip install -e .
```

## Examples

``` python
import check

@check.arg(name='nb', vtype=check.Integer(), doc='Number of time to repeate the message')
@check.arg(name='msg', vtype=check.String(), doc='Message to be repeated')
def repeat(nb, msg):
    for i in range(nb):
        print(msg)

# Works
repeat(3, "hello")

# Raise an exception
repeat(4.6, "hello")
```


