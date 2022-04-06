# Jaskier
![issues](https://img.shields.io/github/issues/soukyomi/jaskier)
![forks](https://img.shields.io/github/forks/soukyomi/jaskier)
![stars](https://img.shields.io/github/stars/soukyomi/jaskier)
![license](https://img.shields.io/github/license/soukyomi/jaskier)

Library to make loggings more prettier and readable.


Table of Contents
=================
<!--ts-->
  * [Installing](#installing)
  * [Quickstart](#quickstart)
  * [Documentation](#documentation)
  * [License](#license)

## Installing

**Python 3.5.3 or higher is required.**

To install the library, you can just run the following command:
```sh
# Linux/macOS
$ python3 -m pip install -U jaskier

# Windows
$ py -3 -m pip install -U jaskier
```


## Quickstart

Jaskier currently only adds a single handler, you can add it like this:
```py
import logging
from jaskier import JaskierHandler

logger = logging.getLogger('my-logger')
logger.setLevel(logging.DEBUG)
logger.addHandler(JaskierHandler())

logger.debug('Some debug message')
logger.info('And another info message')
# etc.
```

## Documentation

Jaskier documentation can be found [here](https://jaskier.readthedocs.io/en/latest/).


## License

Jaskier is protected by MIT license:
```
MIT License

Copyright (c) 2021 Caio Alexandre

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```