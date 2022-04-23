"""
Jaskier
~~~~~~~

A basic handler for more rich loggings.

:copyright: (c) 2022-present
:license: MIT, see LICENSE for more details.

"""

__title__ = 'jaskier'
__author__ = 'kyomi'
__license__ = 'MIT'
__copyright__ = 'Copyright 2022-present kyomi'
__version__ = '1.0.0'


from typing import Literal, NamedTuple

from .handlers import JaskierHandler as JaskierHandler


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal['alpha', 'beta', 'candidate', 'stable']
    serial: int

version_info = VersionInfo(1, 0, 0, 'stable', 0)
