#!/bin/bash
CUR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PASSWD_FILE="$CUR_DIR/passwd"
SHADOW_FILE="$CUR_DIR/shadow"
CRACK_ME_FILE="$CUR_DIR/crack_me"

unshadow $PASSWD_FILE $SHADOW_FILE > $CRACK_ME_FILE
john $CRACK_ME_FILE
john --show $CRACK_ME_FILE
