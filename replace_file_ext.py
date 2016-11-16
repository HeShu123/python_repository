# -*- coding: utf-8 -*-
# Filename: BatchChangeFileName.py

import os
import sys

def TraverseFolder(path):
    print "<----folder&file---->"
    no=0
    for (path,dirs,files) in os.walk(path):
        print
        no += 1
        print "No.%d"%no
        print "path=%s"%path
        if len(dirs)!=0:
            #print type(dirs)
            subfolders = ''
            for dir in dirs:
                subfolders += dir+';'
            subfolders = '[' + subfolders + ']'
            print "subfolders=%s"%subfolders
        if len(files)!=0:
            filenames = ''
            for filename in files:
                filenames += filename+';'
            filenames = '[' + filenames + ']'
            print "files=%s"%filenames
    print "<----folder&file---->"
    

def RenameFile():
    str = u'请输入要处理的文件夹路径====>'
    path = raw_input(str.encode('gbk'))
    print path
    
    str = u'请输入源文件类型(不包括.)====>'
    old_ext = "."+raw_input(str.encode('gbk'))
    print old_ext
    
    str = u'请输入目标文件类型(不包括.)====>'
    new_ext = "."+raw_input(str.encode('gbk'))    
    print new_ext
    
    print   #输出空行占位
    TraverseFolder(path)
    print
    
    str = u'开始批量更名'
    print str
    print '<-----------------'
    changedCount = 0          
    for (path,dirs,files) in os.walk(path):
        for filename in files:
            ext = os.path.splitext(filename)[1] #取得文件类型，注意它还带着点号            
            if (ext == old_ext):
                changedCount += 1
                newname = filename.replace(old_ext, new_ext)
                oldpath = path + "\\" + filename      
                newpath = path + "\\" + newname
                try:
                    os.rename(oldpath, newpath)
                    print 'No.%d'%changedCount, 'change', oldpath, 'to', newpath
                except BaseException, e:  
                    print(str(e))
    print '----------------->'
                                                                               

if __name__ == '__main__':
    RenameFile() 
        
print        
raw_input("press Enter to exit")
sys.exit()