#!/usr/bin/env bash

if [ -z $1 ]; then
	name=World
else
	name=$1
fi

echo "Hello, $name!"
