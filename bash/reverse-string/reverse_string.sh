#!/usr/bin/env bash
#
# Tested with 
# GNU bash, version 4.4.23(1)-release (x86_64-redhat-linux-gnu)

for ((i=${#1}-1;i>=0;i--));
do
	# Substring expansion used to extract characters in reverse order
	# one character at a time
	printf "%s" "${1:${i}:1}"
done
