#!/usr/bin/env bash

declare -i number="$1"
declare -i num_digits="${#number}"
declare -i sum=0

for (( i=0; i < num_digits; i++ )); do
	sum+=$(( ${number:i:1} ** num_digits ))
done

if (( sum == number )); then
	echo true
else
	echo false
fi
