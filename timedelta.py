# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 20:11:11 2018

@author: DD
"""

from datetime import timedelta, datetime
import time

a = timedelta(days=2, hours=6)
d = datetime.now()
pd = timedelta(days=1)
d1 = d - pd
dw = d1.weekday()
print(dw)


print(a)
print(a.seconds)
