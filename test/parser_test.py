#!/usr/bin/env python

import sys
sys.path.append("..")
from src import parser

if __name__ == "__main__":
    intcode, vartable = parser.parse(sys.stdin)
    for line in intcode:
        print(line["label"] + '\t' + line["code"] + "\t\tScope:" + str(line["scope"]))

    for svlist in vartable.svlists:
        print(svlist)
