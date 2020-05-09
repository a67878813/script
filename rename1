# -*- coding: gbk -*-
path1 = u'K:\\选择删除\\'  #所需修改文件夹所在路径
import os
import zhconv
for parent, dirnames, filenames in os.walk(path1):
    for filename in filenames:
        try:
            os.rename(os.path.join(parent, filename), os.path.join(parent, filename.replace(' ', '')))
        except:
            print(u"文件重命名错误" + str(filename))

		
import os, sys


dirs = os.listdir(path1)
 

for dir in dirs:
    try:
        os.rename(path1+str(dir),path1+dir.replace(' ', ''))
    except:
        print(u"目录重命名错误" + path1+str(dir))
