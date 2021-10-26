"""Convert integer to Roman numeral.

Adapted from https://diveinto.org/python3/unit-testing.html
"""
roman_numeral_map = (("M",  1000),
                     ("CM", 900),
                     ("D",  500),
                     ("CD", 400),
                     ("C",  100),
                     ("XC", 90),
                     ("L",  50),
                     ("XL", 40),
                     ("X",  10),
                     ("IX", 9),
                     ("V",  5),
                     ("IV", 4),
                     ("I",  1))

def to_roman(n):
    """Convert integer to Roman numeral"""
    if not isinstance(n, int):
        raise ValueError("Number must be an integer")
    if not (0 < n < 4000):
        raise ValueError("Number out of range (must in range 1-4000)")

    result = ""
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
#            print(f"subtracting {integer}, adding {numeral} to output")
    return result

def from_roman(s):
    """Convert Roman numeral to integer"""
    import re 

    if not isinstance(s, str):
        raise ValueError("Roman numeral must be a string")

    roman_numeral_pattern = re.compile(
            "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",
            re.VERBOSE)
    if not roman_numeral_pattern.search(s):
        raise ValueError(f"Invalid Roman numeral: {s}")

    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
#            print(f"found {numeral}, adding {integer}")
    return result

#print(from_roman("X"))
#print(to_roman(9))

