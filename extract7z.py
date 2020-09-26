#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/python3
# coding: utf-8
import os
import os.path
#import json
#import random
#import pickle
import time
#import subprocess


#import os
#import subprocess,signal


# In[2]:


contents = 'B:\\baidu\\0000动画\\'
ex_contents = 'B:\\baidu\\动画_extracted\\'
print(contents)
print(len(contents))


# In[3]:


import py7zr


# In[ ]:


s =[]
for root, dirs, files in os.walk(contents):
    for name in files:
        if ('7z' in name )and ('downloading' not in name ) :
            #print(f'neme ={name}')
            #print(f'root ={root}')
            a_ = root[len(contents):]
            a2_ = a_.split('\\')
            PASSWORD1_ = a2_[0]
            print(f'password ={PASSWORD1_}')
            PATH2_ = a2_[1:]
            PATH2str = '\\'.join(PATH2_)
            #print(f'path2 = {PATH2str}')
            #print(a2_)
            ex_dir = root  +"\\"
            print(f'exdir={ex_dir}')
            
            FILENAME1_ = root +'\\'+ name
            print(f'filename ={FILENAME1_}')
            #print(f'dirs ={dirs}')
            #print(f'files ={files}')
            #s.append(os.path.join(root, name))
            
            
            #解压流程
            try:
                with py7zr.SevenZipFile(FILENAME1_, "r", password=PASSWORD1_) as szf:

                    cc2 = szf.getnames()
                    print(f'正在解压{cc2}')
                    szf.extractall(path = ex_dir)
                    print(f'解压成功{cc2}')
                print(f'删除文件{FILENAME1_}')
                os.remove(FILENAME1_)
            except:
                print(f'错误{FILENAME1_}')
                pass


# In[ ]:




