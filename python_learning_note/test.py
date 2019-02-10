
'''#import first 
#from first import find, test
#sys.path.append('/Users/skidnp/Desktop/untitled folder') 如果没有sys在同一个文件夹，此方法适用
from first import *# the same with from first import find, test
#import sys
course=['history','math','dance']

index=find(course,'math')
#print(index)
#print(test)
print(sys.path)

import random

course=['history','math','dance']
random_course=random.choice(course)
print(random_course)


import math
course=['history','math','dance']
rads=math.radians(90)
print(rads.sin(rads))

import datetime
import calendar

today=datetime.date.today()
print(today)
print(calendar.isleap(10000))

import os
print(os.getcwd())
print(os.__file__)

import antigravity
'''

