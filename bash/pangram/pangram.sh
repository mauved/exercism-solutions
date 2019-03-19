#!/usr/bin/env bash


text=$1

# grep extracts all alphabet chars to separate lines
# all characters set to upper case and sorted
# newlines removed convert to single string
# repeated characters removed from string
charset=$(
	grep -Eo "[[:alpha:]]" <<< "${text}" |
	tr "[:lower:]" "[:upper:]" | sort -d |
	tr -d '\n' | tr -s "[:alpha:]"
)

if (( ${#charset} < 26 )); then
	echo false
else
	echo true
fi
