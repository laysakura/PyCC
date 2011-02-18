#!/bin/bash

if [ ! -e ./cogen ]; then
    echo "./cogen not found";
    exit 1;
fi


benchmark()
{
    input=$1
    mkdir -p out
    base=out/`basename $input .c`
    echo "********** ${input} **********" 1>&2
    shift

    echo "=== gcc ===" 1>&2
    gcc -o ${base}.gcc ${input} C0main.c
    ./${base}.gcc $@ | tee ${base}.gcc.out

    echo "=== gcc -O3 ===" 1>&2
    gcc -O3 -o ${base}.gccO3 ${input} C0main.c    
    ./${base}.gccO3 $@ | tee ${base}.gccO3.out

    echo "=== cogen ===" 1>&2
    ./cogen ${input} > ${base}.s
    gcc -o ${base}.cogen ${base}.s C0main.c
    ./${base}.cogen $@ | tee ${base}.cogen.out

    diff ${base}.cogen.out ${base}.gcc.out > ${base}.diff
    if [ -s ${base}.diff ]; then
        echo "********** ${input}: NG **********" 1>&2
    else
        echo "********** ${input}: OK **********" 1>&2
    fi

    echo "" 1>&2
}

benchmark fib.c 40
benchmark prime.c 10000000
benchmark prime5.c 10000000
benchmark ackermann.c 3 13
benchmark pi.c 100000000 1000 1

# rm *.$ext
# rm $ext.s
