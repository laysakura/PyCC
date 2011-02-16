import re

def fully_match(pattern, string):
    """
    Returns if 'string' completely matches to 'pattern'

    Usage:
    p = re.compile("[a-z][0-9]")
    ("x9", p)  ->  True
    ("x98", p) ->  False
    """
    return re.match(pattern, string).group() == string
