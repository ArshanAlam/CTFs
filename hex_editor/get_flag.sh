#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
FILENAME="hex_editor.jpg"
cd $DIR
strings $DIR/$FILENAME | grep "flag"
