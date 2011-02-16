#!/bin/bash
for i in `seq 0 4`; do
    ./tokenizer_test.py < tokenizer_data/0${i}.txt > tokenizer_data/0${i}.my ;
done

for i in `seq 0 4`; do
    diff tokenizer_data/0${i}.ans tokenizer_data/0${i}.my ;
    if [ $? -eq 0 ]; then
        echo "Succeeded in tokenizing 0${i}.txt !!" ;
    else
        echo "Failed in tokenizing 0${i}.txt ..." ;
    fi
done
