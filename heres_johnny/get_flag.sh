#!/bin/bash

# After cracking the password, use netcat to get the flag
USERNAME="root"
PASSWORD="hellokitty"

printf "$USERNAME\n$PASSWORD\n" | nc 2018shell.picoctf.com 35225
