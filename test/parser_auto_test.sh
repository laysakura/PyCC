#!/bin/bash
for i in `seq 0 9`; do
    echo -n "Parsing regular/f0${i}.c	"
    ./parser_test.py < parser_data/regular/f0${i}.c 2> /dev/null
    if [ $? -eq 0 ]; then
        echo "[OK]" ;
    else
        echo "[FAIL]" ;
    fi
done

for i in `seq 10 43`; do
    echo -n "Parsing regular/f${i}.c	"
    ./parser_test.py < parser_data/regular/f${i}.c 2> /dev/null
    if [ $? -eq 0 ]; then
        echo "[OK]" ;
    else
        echo "[FAIL]" ;
    fi
done


for i in `seq 0 9`; do
    echo -n "Parsing fuzzying/c0${i}.c	"
    ./parser_test.py < parser_data/fuzzying/c0${i}.c 2> /dev/null
    if [ $? -eq 0 ]; then
        echo "[OK]" ;
    else
        echo "[FAIL]" ;
    fi
done

for i in `seq 10 30`; do
    echo -n "Parsing fuzzying/c${i}.c	"
    ./parser_test.py < parser_data/fuzzying/c${i}.c 2> /dev/null
    if [ $? -eq 0 ]; then
        echo "[OK]" ;
    else
        echo "[FAIL]" ;
    fi
done


for i in `seq 0 9`; do
    echo -n "Parsing fuzzying/w0${i}.c	"
    ./parser_test.py < parser_data/fuzzying/w0${i}.c 2> /dev/null
    if [ $? -eq 1 ]; then
        echo "[OK, detected syntacs error]" ;
    else
        echo "[FAIL]" ;
    fi
done

for i in `seq 10 30`; do
    echo -n "Parsing fuzzying/w${i}.c	"
    ./parser_test.py < parser_data/fuzzying/w${i}.c 2> /dev/null
    if [ $? -eq 1 ]; then
        echo "[OK, detected syntacs error]" ;
    else
        echo "[FAIL]" ;
    fi
done

