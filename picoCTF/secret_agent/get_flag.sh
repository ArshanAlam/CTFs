#!/bin/bash

curl --silent -L -XGET http://2018shell.picoctf.com:60372/flag -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" | grep -o "picoCTF{.*}"
