#!/bin/bash

curl --silent -L -XGET http://2018shell.picoctf.com:29568/74efc.html | grep -o "picoCTF{.*}"
