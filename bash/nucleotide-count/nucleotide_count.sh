#!/usr/bin/env bash

strand="${1}"

declare -i A=0
declare -i C=0
declare -i G=0
declare -i T=0

for (( i=0; i < ${#strand}; i++ )); do
	case "${strand:${i}:1}" in
		A) A+=1 ;;
		C) C+=1 ;;
		G) G+=1 ;;
		T) T+=1 ;;
		*)
			echo "Invalid nucleotide in strand"
			exit 1
			;;
	esac
done

echo -e "\
A: ${A}\n\
C: ${C}\n\
G: ${G}\n\
T: ${T}\
"
