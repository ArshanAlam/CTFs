#!/bin/bash

gcc -m32 -masm=intel intro_asm_rev.S get_flag.c -o get_flag
chmod 700 get_flag
