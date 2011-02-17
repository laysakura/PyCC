#!/usr/bin/env python

import sys
sys.path.append("..")
from src import parser

if __name__ == "__main__":
    parser.parse(sys.stdin)
