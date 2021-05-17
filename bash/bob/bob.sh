#!/usr/bin/env bash

banter="${1}"

declare -Ar responses=(
    [QUESTION]="Sure."
    [YELL]="Whoa, chill out!"
    [YELL_QUESTION]="Calm down, I know what I'm doing!"
    [SILENCE]="Fine. Be that way!"
    [STOCK]="Whatever."
)

function answer_question {
    echo "${responses[QUESTION]}"
}

function answer_yell {
    echo "${responses[YELL]}"
}

function answer_yelled_question {
    echo "${responses[YELL_QUESTION]}"
}

function answer_silence {
    echo "${responses[SILENCE]}"
}

function answer_whatever {
    echo "${responses[STOCK]}"
}

# If there're any lowercase characters, then it's not a yell
if [[ ${banter} =~ [[:lower:]]+ ]]
then
    # It's a question if it ends with a question mark
    if [[ ${banter} =~ \?[[:space:][:blank:]]*$ ]]
    then
        answer_question
    # otherwise it's not
    else
        answer_whatever
    fi
# Only uppers and no lowers? Must be a yell.
elif [[ ${banter} =~ [[:upper:]]+ ]]
then
    if [[ ${banter} =~ \?[[:space:][:blank:]]*$ ]]
    then
        answer_yelled_question
    else
        answer_yell
    fi
# special case: Question with no alphanumerics
elif [[ ${banter} =~ \?[[:space:][:blank:]]*$ ]]
then
    answer_question
# catching any other straggling characters
elif [[ ${banter} =~ [[:alnum:][:punct:]]+ ]]
then
    answer_whatever
else
    answer_silence
fi

