import sys
import re

def gen_unique_id():
    n = 0
    while True:
        yield n
        n += 1

def fully_match(pattern, string):
    """
    Returns if 'string' completely matches to 'pattern'

    Usage:
    p = re.compile("[a-z][0-9]")
    fully_match(p, "x9")  ->  True
    fully_match(p, "x98") ->  False
    """
    m = re.match(pattern, string)
    if m is None:
        return False
    else:
        return m.group() == string

def startwith(string, pattern):
    """
    Returns if 'string' starts with 'pattern'

    Usage:
    startwith("hogefoobar", "hoge")  -> True
    startwith("hogefoobar", "foo")   -> False
    """
    return string.find(pattern) == 0

def err_exit(err):
    sys.stderr.write(err)
    exit(1)
