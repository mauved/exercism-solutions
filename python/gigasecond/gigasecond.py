# 
# Solution for gigasecond
# Written by Sofia Nieves
#

import datetime

def add_gigasecond(birthdate):
   GIGASECOND = datetime.timedelta(seconds=10**9) 
   return birthdate + GIGASECOND
