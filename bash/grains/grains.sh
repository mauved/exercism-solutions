#!/usr/bin/env bash

# This function counts the number of grains
# received in total up to a certain square
grain_count () {
	bin_total=$(
		for ((i=0; i < ${1}; i++)); do
			printf 1
		done
	)
	echo "${bin_total}"
}

# Tried to not use bc but 2^64 is too large a number
# for bash to handle on its own. Calculation assumes 64 squares.
readonly BOARDTOTAL=$(bc << END
2^64 - 1
END
)

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
# printf %u "$((2**(${1}-1)))"
printf %u "$((1<<(${1}-1)))"
