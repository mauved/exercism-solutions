#!/usr/bin/env bash

declare -i integer_n="${1}"

# Only positive integers permitted!
if [ "${integer_n}" -lt 1 ]; then
	echo "Error: Only positive numbers are allowed"
	exit 1
fi

declare -i step_count=0

# test the collatz conjecture by running it
until [ "${integer_n}" -eq 1 ]; do
	if (( integer_n % 2 == 0 )); then
		(( integer_n/=2 ))
	else
		(( integer_n*=3 ))
		(( integer_n+=1 ))
	fi

	# increment at every iteration
	(( step_count+=1 ))
done

echo "${step_count}"
