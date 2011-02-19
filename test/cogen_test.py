#!/usr/bin/env python

import sys
sys.path.append("..")
from src import parser
from src import cogen

if __name__ == "__main__":
    intcodes, vartable = parser.parse(sys.stdin)
    asm = cogen.cogen(intcodes, vartable)

    for svlist in vartable.svlists:
        sys.stderr.write(str(svlist) + '\n')

    for line in intcodes:
        sys.stderr.write(line["label"] + '\t' + line["code"] + "\t\tScope:" + str(line["scope"]) + '\n')

    sys.stderr.write("\n====Assembly====")
    for line in asm:
        print(line)
