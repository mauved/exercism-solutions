#!/usr/bin/env bash

# Start out with an empty string and append to it as its factors are checked
translated=""

if [ $(( ${1} % 3 )) == 0 ]; then
	translated+="Pling"
fi

if [ $(( ${1} % 5 )) == 0 ]; then
	translated+="Plang"
fi

if [ $(( ${1} % 7 )) == 0 ]; then
	translated+="Plong"
fi

# If no factors are found, just print the original string
if [ "${translated}" != "" ]; then
	echo "${translated}"
else
	echo "${1}"
fi
