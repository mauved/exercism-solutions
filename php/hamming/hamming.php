<?php

//
// This is only a SKELETON file for the "Hamming" exercise. It's been provided as a
// convenience to get you started writing code faster.
// Completed by Sofia Nieves
// Mon 30 May 04:56:34 UTC 2016
//

function distance($a, $b)
{
    $distance = 0;

    if (strlen($a) != strlen($b))
    {
        throw new InvalidArgumentException('DNA strands must be of equal length.');
    }

    for ($i = 0; $i < strlen($a); $i++)
    {
        if (substr($a, $i, 1) != substr($b, $i, 1))
        {
            $distance++;
        }
    }

    return $distance;
}
