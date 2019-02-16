#!/usr/bin/env bash

# Characters separated by whitespace and dashes
# are separate words.
IFS+="-"
words="${1}"

for word in $words; do
	acronym+="${word:0:1}"
done

# Uppercase all output
echo "${acronym^^}"
