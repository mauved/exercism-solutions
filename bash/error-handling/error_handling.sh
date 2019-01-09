#!/usr/bin/env bash

if [ ${#@} -lt 1 ]; then
	echo "Usage: ./error_handling <greetee>"
	exit 1
fi

if [ ${#@} -gt 1 ]; then
	echo "Script takes one argument as greetee. Try quotes"
	exit 2
fi

echo "Hello, ${1}"
