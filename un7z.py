#!/usr/bin/python3
# coding: utf-8
import os
import os.path
import time
#import subprocess
contents = 'I:\\迅雷下载'
ex_contents = 'B:\\baidu\\动画_extracted\\'
print(contents)
print(len(contents))
import py7zr
error_files=[]
pass_lists = os.listdir(contents)
pass_lists2 =[]
for i in pass_lists:
    j  = i.replace('星号','*')#.replace('&','^&')
    pass_lists2.append(j)
print(pass_lists2)
s =[]
for root, dirs, files in os.walk(contents):
    for name in files:
        if ('.7z' in name[-4:] ):
            END_ = 0
            print(f'name ={name}')
            #print(f'dirs ={dirs}')
            a_ = root[len(contents):]
            #print(a_)
            a2_ = a_.split('\\')
            #print(a2_)
            PASSWORD1_ = a2_[1]
            if "星号" in PASSWORD1_:
                PASSWORD1_ = PASSWORD1_.replace('星号','*')
            
            
            print(f'password ={PASSWORD1_}')
            PATH2_ = a2_[1:]
            PATH2str = '\\'.join(PATH2_)
            #print(f'path2 = {PATH2str}')
            #print(a2_)
            ex_dir = root  +"\\"
            print(f'exdir={ex_dir}')
            
            
            FILENAME1_ = root +'\\'+ name
            print(f'filename1 ={FILENAME1_}')
            #print(f'dirs ={dirs}')
            #print(f'files ={files}')
            #s.append(os.path.join(root, name))
            
            print('--------')
            
            
            #解压流程
            
            try:
                with py7zr.SevenZipFile(FILENAME1_, "r", password=PASSWORD1_) as szf:

                    cc2 = szf.getnames()
                    print(f'正在解压{FILENAME1_}')
                    szf.extractall(path = ex_dir)
                    print(f'解压成功')
                print(f'删除文件{FILENAME1_}')
                os.remove(FILENAME1_)
            except Exception as err :
                print(f'        错误{FILENAME1_}')
                print(f"        {err}")
                for i in pass_lists2:
                    try:
                        print(f"        FILE={FILENAME1_[10:30]}，尝试密码{i}                ",end='\r')
                        with py7zr.SevenZipFile(FILENAME1_, "r", password=i) as szf:

                            cc2 = szf.getnames()
                            #print(f'正在解压{cc2}')
                            szf.extractall(path = ex_dir)
                            print(f'解压成功')
                        print(f'删除文件{FILENAME1_}')
                        os.remove(FILENAME1_)
                        with open(FILENAME1_+f"成功密码{i}.txt",mode="w",encoding="utf-8") as f:  #写文件,当文件不存在时,就直接创建此文件
                            print("		创建文件成功")
                        END_ = 1
                        break
                    except Exception as err :
                        #print(f'        错误{FILENAME1_}')
                        #print(f"        {err}")
                        pass
                
                if END_ == 0:
                    print("尝试无密码解压")
                    print("")
                        
                    try:
                        print(f"        FILE={FILENAME1_[10:30]}，无密码                ",end='\r')
                        with py7zr.SevenZipFile(FILENAME1_, "r") as szf:

                            cc2 = szf.getnames()
                            #print(f'正在解压{cc2}')
                            szf.extractall(path = ex_dir)
                            print(f'解压成功')
                        print(f'删除文件{FILENAME1_}')
                        os.remove(FILENAME1_)
                        with open(FILENAME1_+f"无密码解压.txt",mode="w",encoding="utf-8") as f:  #写文件,当文件不存在时,就直接创建此文件
                            print("		创建文件成功")
                        break
                    except Exception as err :
                        #print(f'        错误{FILENAME1_}')
                        #print(f"        {err}")
                        pass
                
                
                        print("")
                        print("未尝试出密码")
                        print("")
                        print("")
                        print("")
                        error_files.append(FILENAME1_)
                    pass
            
            
print('=============================================')
print('end \n\r 未解压文件如下')
for i in error_files:
    print(i)
