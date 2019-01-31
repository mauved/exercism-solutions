#!/usr/bin/env bash

# Verify that two strings have been placed in input
# before anything else
if [ "$#" -ne 2 ]; then
	echo "Usage: hamming.sh <string1> <string2>"
	exit 1
fi

strand1="${1}"
strand2="${2}"
declare -i hamming_count=0

if [ ${#strand1} -ne ${#strand2} ]; then
	echo "left and right strands must be of equal length" >&2
	exit 1
fi

# iterate over each single character substring and do a comparison
for (( i=0; i < ${#strand1}; i++ )); do
	if [ "${strand1:${i}:1}" != "${strand2:${i}:1}" ]; then
		hamming_count+=1
	fi
done

echo "${hamming_count}"
