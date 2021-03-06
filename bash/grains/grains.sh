#!/usr/bin/env bash

readonly BOARDTOTAL=$(( 2**64 - 1 ))

if [[ $1 == "total" ]]; then
	printf %u "${BOARDTOTAL}"
	exit 0
fi

# Standard chess boards have 64 squares
if [[ $1 -lt 1 || $1 -gt 64 ]]; then
	printf "Error: invalid input\n" >&2
	exit 1
fi

# unsigned integer with %u for handling later squares
# such as 2^(64-1)
printf %u "$((2**(${1}-1)))"
