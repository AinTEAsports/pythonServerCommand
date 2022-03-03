#!/bin/bash


workingDirectory=$(pwd)

printf "alias pyserv='$workingDirectory/pyserv.py'" > $SHELL
source $SHELL
