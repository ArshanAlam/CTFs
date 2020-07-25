#!/bin/bash

strings 2018.png | grep -o "picoCTF{.*}"
