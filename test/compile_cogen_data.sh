#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Compile a source and link it with cogen_data/C0main.c"
    echo "Usage: \$ $0  SOURCE" 1>&2
    exit 1
fi

src=$1
asm=`echo $1 |sed "s/\.c/\.s/"`
out=`echo $1 |sed "s/\.c//"`

./cogen_test.py < ${src} 2> /dev/null > ${asm}
gcc -o ${out} cogen_data//C0main.c ${asm}

echo "${out} outputs:"
./${out}
