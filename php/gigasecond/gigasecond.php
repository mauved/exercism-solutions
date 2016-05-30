<?php

//
// Solution file for Gigasecond
// Written by Sofia Nieves
// Mon 30 May 09:55:50 UTC 2016
//

function from($start_date)
{
    $GIGASECOND = new DateInterval('PT1000000000S');
    $gs_date = clone $start_date;
    return $gs_date->add($GIGASECOND);
}
