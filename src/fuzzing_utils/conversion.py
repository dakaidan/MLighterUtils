import struct
import math
from typing import Callable, Dict

import numpy as np


def to_float(value: int | np.int64) -> float:
    """Converts an int or np.int64 to a float value"""
    return struct.unpack('!f', struct.pack('!I', value))[0]


def to_fraction(value: int | np.int64) -> float:
    """Converts an int or np.int64 to a float between 0 and 1"""
    # return abs(float(value) / MAX_INT)
    """
    Using modf as it may scale better than the above.
    Currently untested.
    """
    return math.modf(to_float(value))[0]


def to_positive(value: int | np.int64) -> int:
    """Converts an int or np.int64 to a positive int"""
    return abs(value)


def to_positive_or_none(value: int | np.int64) -> int | None:
    """Positive int or None"""
    if value <= 0:
        return None
    else:
        return value


def to_greater_than(value: int | np.int64, min_value: int) -> int:
    """Converts an int or np.int64 to a positive int greater than min_value"""
    return min_value + abs(value)


def to_greater_than_or_none(value: int | np.int64, min_value: int) -> int | None:
    """Converts an int or np.int64 to a positive int greater than min_value"""
    if value <= 0:
        return None
    else:
        return min_value + abs(value)


def to_positive_integer_or_fraction(value: int | np.int64) -> int | float:
    """Converts an int or np.int64 to a positive int or fraction"""
    if value <= 0:
        return to_fraction(value)
    else:
        return value


class Reserved:
    """A reserved type"""
    pass


def to_reserved_or_else(value: int | np.int64, reserved: Dict[int | np.int64, any] | Callable[[int | np.int64], any],
                        else_function: Callable[[int | np.int64], any]) -> any:
    """
    Takes a value and returns a reserved value or the else_function

    Args:
        value (int | np.int64): The value to check
        reserved (dict[int | np.int64, any] | callable[[int | np.int64], any]): A dictionary of reserved values or a
        function which takes a value, and either returns its replacement or Reserved type
        else_function (callable[[int | np.int64], any]): A function which takes a value and returns its replacement
    """
    if type(reserved) is dict:
        if value in reserved:
            return reserved[value]
        else:
            return else_function(value)
    else:
        reserved_value = reserved(value)
        if reserved_value != Reserved:
            return reserved_value
        else:
            return else_function(value)
