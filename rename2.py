# -*- coding: gbk -*-
path1 = u'K:\\选择删除\\' #所需修改文件夹所在路径
import os
import zhconv
for parent, dirnames, filenames in os.walk(path1):
    for filename in filenames:
        try:
            os.rename(os.path.join(parent, filename), os.path.join(parent, zhconv.convert(filename, 'zh-cn')))
            #print(zhconv.convert(filename, 'zh-cn'))
        except:
            print("文件重命名错误" + str(filename))

		
import os, sys


dirs = os.listdir(path1)
 

for dir in dirs:
    try:
        os.rename(path1+str(dir),path1+zhconv.convert(dir, 'zh-cn'))
        #print(zhconv.convert(dir, 'zh-cn'))
    except:
        print("目录重命名错误" + path1+str(dir))
