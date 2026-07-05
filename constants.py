from enum import IntEnum


class Module(IntEnum):
    """
    Represents the state of a QR module.
    """

    EMPTY = -1

    WHITE = 0
    BLACK = 1

    RESERVED = 2