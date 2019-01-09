#!/usr/bin/env bash

# no such thing as case in scrabble
shopt -s nocasematch

declare -i score=0

for (( i=0; i<${#1}; i++ )); do
	case ${1:$i:1} in 
		[AEIOULNRST])
			score+=1
			;;
		[DG]) 
			score+=2
			;;
		[BCMP])
			score+=3
			;;
		[FHVWY])
			score+=4
			;;
		[K])
			score+=5
			;;
		[JX])
			score+=8
			;;
		[QZ])
			score+=10
			;;
	esac
done

echo "${score}"

