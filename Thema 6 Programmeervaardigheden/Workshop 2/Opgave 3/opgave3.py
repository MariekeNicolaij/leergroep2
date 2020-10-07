
from math import *

# sq

def sq(x):
    """
    Returns sq x
    """

    return x ** 2

# interp

def interp(low, hi, fraction):
    """
    Returns the progress between low and high
    """

    difference = hi - low
    step = difference * fraction

    return low + step

# checkends

def checkends(s):
    """
    Returns True when first character of 's' is the same as the last character of 's'
    """

    s = s.lower()

    if s[0] == s[-1]:
        print("Gelijk! Letters: ", s[0] + s[-1])
        return True
    else:
        print("Ongelijk! Letters: ", s[0] + s[-1])
        return False


# flipside

def flipside(s):
    """
    Flips the string!
    """

    sLength = len(s)
    halfLength = floor(sLength / 2)

    return s[halfLength:sLength] + s[0:halfLength]
    
# convert_from_seconds

def convert_from_seconds(s):
    """
    Convert s to seconds
    """

    s = abs(s) # makes the value absolute, so no negatives :)

    days = s // (24 * 60 * 60)
    s = s % (24 * 60 * 60)

    hours = s // (60 * 60)
    s = s % (60 * 60)

    minutes = s // 60
    s = s % 60

    seconds = s

    print("Days: ", days, ", Hours: ", hours, ", Minutes: ", minutes, ", Seconds: ", seconds)
    return [days, hours, minutes, seconds]