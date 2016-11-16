# -*- coding:utf-8 -*-

import time

str = u'请输入时间戳===>'
value = raw_input(str.encode('gbk'))
print value
x = time.mktime(time.strptime(value,'%Y-%m-%d %H:%M:%S'))
print x
