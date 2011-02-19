#!/bin/bash

echo -n "Processing cogen_data/fib.c	"
./cogen_test.py < cogen_data/fib.c 2> /dev/null
if [ $? -eq 0 ]; then
    echo "[OK]" ;
else
    echo "[FAIL]" ;
fi

echo -n "Processing cogen_data/pi.c	"
./cogen_test.py < cogen_data/pi.c 2> /dev/null
if [ $? -eq 0 ]; then
    echo "[OK]" ;
else
    echo "[FAIL]" ;
fi

echo -n "Processing cogen_data/ackermann.c	"
./cogen_test.py < cogen_data/ackermann.c 2> /dev/null
if [ $? -eq 0 ]; then
    echo "[OK]" ;
else
    echo "[FAIL]" ;
fi

echo -n "Processing cogen_data/prime.c	"
./cogen_test.py < cogen_data/prime.c 2> /dev/null
if [ $? -eq 0 ]; then
    echo "[OK]" ;
else
    echo "[FAIL]" ;
fi

echo -n "Processing cogen_data/prime5.c	"
./cogen_test.py < cogen_data/prime5.c 2> /dev/null
if [ $? -eq 0 ]; then
    echo "[OK]" ;
else
    echo "[FAIL]" ;
fi
