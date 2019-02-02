#!/usr/bin/env bash

usage() {
	echo "Usage: leap.sh <year>"
}

# Only one arg permitted
if [ $# -ne 1 ]; then
	usage
	exit 1
fi

# Make sure only integers are excepted
if [[ ! "${1}" =~ ^[[:digit:]]+$ ]]; then
	usage
	exit 1
fi

declare -i year="${1}"
if (( year % 4 == 0 )); then
	if (( year % 100 == 0 )) ; then
		if (( year % 400 == 0)); then
			echo true
			exit 0
		fi
		echo false
		exit 0
	fi
	echo true
	exit 0
fi

echo false
