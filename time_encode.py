# -*- coding:utf-8 -*-

import time

str = u'请输入时间戳===>'
value = input(str.encode('gbk'))
print value
x = time.localtime(value)
print time.strftime('%Y-%m-%d %H:%M:%S',x)
