from constants import Module

"""
Reusable QR Code patterns.

This file contains the fixed structures defined
by the QR Code specification.
"""

FINDER_PATTERN = [
    [Module.BLACK, Module.BLACK, Module.BLACK, Module.BLACK, Module.BLACK, Module.BLACK, Module.BLACK],
    [Module.BLACK, Module.WHITE, Module.WHITE, Module.WHITE, Module.WHITE, Module.WHITE, Module.BLACK],
    [Module.BLACK, Module.WHITE, Module.BLACK, Module.BLACK, Module.BLACK, Module.WHITE, Module.BLACK],
    [Module.BLACK, Module.WHITE, Module.BLACK, Module.BLACK, Module.BLACK, Module.WHITE, Module.BLACK],
    [Module.BLACK, Module.WHITE, Module.BLACK, Module.BLACK, Module.BLACK, Module.WHITE, Module.BLACK],
    [Module.BLACK, Module.WHITE, Module.WHITE, Module.WHITE, Module.WHITE, Module.WHITE, Module.BLACK],
    [Module.BLACK, Module.BLACK, Module.BLACK, Module.BLACK, Module.BLACK, Module.BLACK, Module.BLACK],
]