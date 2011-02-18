#!/usr/bin/env python

import sys
sys.path.append("..")
from src import parser

if __name__ == "__main__":
    intcode = parser.parse(sys.stdin)
    for line in intcode:
        print(line["code"])
