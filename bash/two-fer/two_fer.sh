#!/usr/bin/env bash

# Used parameter expansion to substitute string "you"
# if $1 is unset
printf %s "One for ${1:-"you"}, one for me."
