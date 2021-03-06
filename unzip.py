# -*- coding: gbk -*-
import os
import os.path
import time
import sys
import subprocess
contents = 'I:\\迅雷下载'
print(contents)


s =[]
error_files=[]
pass_lists = os.listdir(contents)
pass_lists2 =[]
for i in pass_lists:
    j  = i.replace('星号','*')#.replace('&','^&')
    pass_lists2.append(j)
print(pass_lists2)
for root, dirs, files in os.walk(contents):
    nested_levels = root.split('\\')
    #if len(nested_levels) ==4:
    #    del dirs[:]
    #del dirs[:]将删除列表的内容，而不是用对新列表的引用替换dirs。这样做时，就地修改列表很重要。

    for name in files:

        if ('7z' in name[-4:] ) or('zip' in name[-4:] )  :
        
            print('         --------')
            END_ = 0
            #print(f'name ={name}')
            #print(f'dirs ={dirs}')
            #print(f'root ={root}')
            a_ = root[len(contents):]
            #print(f'a_ ={a_}')
            a2_ = a_.split('\\')
            #print(a2_)
            PASSWORD1_ = a2_[1]
            if "星号" in PASSWORD1_:
                PASSWORD1_ = PASSWORD1_.replace('星号','*')
            #print(f'        password ={PASSWORD1_}')
            
            ex_dir = root  +"\\"
            ex_dir = '\"' + ex_dir  + '\"'
            FILENAME1_ = root +'\\'+ name
            FILENAME2_ = '\"' + FILENAME1_  + '\"'
            print(f'        filename1 ={FILENAME1_}')

            #解压流程
            SSTR = ' '.join(["7z.exe","x -aoa ",FILENAME2_,f"-p{PASSWORD1_}",f"-o{ex_dir}",])
            print(f"        SSTR = {SSTR}")
            obj = subprocess.Popen(SSTR,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            cmd_out,cmd_error = obj.communicate()
            #print(cmd_out)
            if "Everything is Ok" in cmd_out:
                #print(f'解压成功')
                print('\033[1;32m' + '解压成功' + '\033[0m')
                print(f'删除文件{FILENAME1_}')
                os.remove(FILENAME1_)
            else:
                errot_2 = cmd_error.strip()[:50]
                print("             ",errot_2)
                print(f'                文件夹密码失效 ')
                if "Wrong password" in cmd_error:
                    for i in pass_lists2:#
                        SSTR = ' '.join(["7z.exe","x -aoa ",FILENAME2_,f"-p{i}",f"-o{ex_dir}",])
                        print(f"                                   尝试密码  {i}                ",end='\r')
                        obj = subprocess.Popen(SSTR,bufsize=1 , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                        cmd_out,cmd_error = obj.communicate()
                        #print(cmd_error)
                        if "Everything is Ok" in cmd_out:
                            print("")
                            print("")
                            print("")
                            print('\033[1;32m' + '解压成功' + '\033[0m')
                            print(f'解压成功！！！！！！！密码={i}！！！！！！！！')
                            with open(FILENAME1_+f"成功密码{i}.txt",mode="w",encoding="utf-8") as f:  #写文件,当文件不存在时,就直接创建此文件
                                pass
                            print(f'删除文件{FILENAME1_}')
                            os.remove(FILENAME1_)
                            END_ =1
                            print(f'')
                            time.sleep(1)
                            break
                        else:
                            pass
                    if END_ == 1:
                        continue #下一文件
                    if END_ == 0:
                        print("")
                        print("")
                        SSTR = ' '.join(["7z.exe","x -aoa ",FILENAME2_,f"-o{ex_dir}",])
                        #print(f"                                 尝试无密码解压                ",end='\r')
                        obj = subprocess.Popen(SSTR,bufsize=1 , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                        cmd_out,cmd_error = obj.communicate()
                        #print(cmd_error)
                        if "Everything is Ok" in cmd_out:
                            print('\033[1;32m' + '解压成功' + '\033[0m')
                            #print(f'解压成功')
                            print(f'！！！！！！！！无密码！！！！！！！！')
                            with open(FILENAME1_+f"无密码.txt",mode="w",encoding="utf-8") as f:  #写文件,当文件不存在时,就直接创建此文件
                                pass
                            print(f'删除文件{FILENAME1_}')
                            os.remove(FILENAME1_)
                            continue##下一文件
                        else:
                            print("")
                            print("")
                            print("")
                            print(f"                解压失败 密码未知")
                            error_files.append(FILENAME1_)
                            continue#下一文件
                    #print("此行")

print('=============================================')
print('end \n\r 未解压文件如下')
for i in error_files:
    print(i)
    