#!/usr/bin/env bash
GIGASECOND=1000000000

# If running BSD date, make sure it doesn't modify the time
if [ $(uname -s) != "Linux" ]; then
	alias date="date -ju"
fi

date -ju -f %s $(($(date -ju -f "%Y-%m-%dZ" $1 +%s) + $GIGASECOND))
