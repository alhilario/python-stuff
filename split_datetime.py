#! /usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

now = datetime.now()

print now
print now.year
print now.month
print now.day
print now.hour
print now.minute
print now.second

print str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
