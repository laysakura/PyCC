#!/usr/bin/env python

import sys
sys.path.append("..")
from src import parser
from src import cogen

if __name__ == "__main__":
    intcodes, vartable = parser.parse(sys.stdin)
    asm = cogen.cogen(intcodes, vartable)

    for svlist in vartable.svlists:
        print(svlist)

    for line in intcodes:
        print(line["label"] + '\t' + line["code"] + "\t\tScope:" + str(line["scope"]))

    for line in asm:
        print(line)
