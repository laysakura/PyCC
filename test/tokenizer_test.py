#!/usr/bin/env python

import sys
sys.path.append("..")
from src import tokenizer

def output_for_test(linenum, token, tok_kind):
    if tok_kind == "TOK_INT_LITERAL" or tok_kind == "TOK_ID":
        print(str(linenum) + ":" + tok_kind + " (" + token + ")")
    else:
        print(str(linenum) + ":" + tok_kind)

if __name__ == "__main__":
    for cur, next in tokenizer.gen_tokens(sys.stdin):
        output_for_test(cur["linenum"], cur["token"], cur["tok_kind"])
