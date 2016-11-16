# -*- coding:utf-8 -*-
import os,sys
old = sys.argv[1]
new = sys.argv[2]
file = sys.argv[3]
file2 = sys.argv[3]
tmp_file ="tmpfile.txt"
f = open(file,"r")
f2 = open(tmp_file,"w")
for line in f:
    if old in line:
        line= str.replace(line,old,new)
        f2.write(line)
    f2.flush()
f.close()
f2.close()

os.remove(file)
os.rename(tmp_file,file2)