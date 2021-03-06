# -*- coding: gbk -*-
import os
import os.path
import time
import sys
import subprocess
contents = 'I:\\迅雷下载'
print(contents)
pass_lists = os.listdir(contents)
pass_lists2 =[]
for i in pass_lists:
    j  = i.replace('星号','*')
    pass_lists2.append(j)
print(pass_lists2)
s =[]
error_files=[]
for root, dirs, files in os.walk(contents):
    for name in files:
        
        if ('rar' in name[-4:] ) :
            print('    --------')
            END_ = 0
            #print(f'    name ={name}')
            a_ = root[len(contents):]
            #print(f'a_ ={a_}')
            a2_ = a_.split('\\')
            #print(a2_)
            PASSWORD1_ = a2_[1]
            if "星号" in PASSWORD1_:
                PASSWORD1_ = PASSWORD1_.replace('星号','*')
            #print(f'    password ={PASSWORD1_}')
            #print(a2_)
            ex_dir = root  +"\\"
            ex_dir = '\"' + ex_dir  + '\"'
            #ex_dir = ex_dir.replace('&','`&')
            #print(f'    exdir={ex_dir}')
            #print(ex_dir.split(':'))
            FILENAME1_ = root +'\\'+ name
            FILENAME2_ = '\"' + FILENAME1_  + '\"'
            print(f'    filename1 ={FILENAME1_}')
            
            #解压流程
            SSTR = ' '.join(["unrar.exe","x",FILENAME2_,f"-p{PASSWORD1_}","-o+",ex_dir])
            #print(f"    SSTR = {SSTR}")
            obj = subprocess.Popen(SSTR ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            cmd_out,cmd_error = obj.communicate()
            if ("All OK" in cmd_out):
                print(f'')
                print(f'')
                print(f'')
                print('\033[1;32m' + '解压成功' + '\033[0m')
                print(f'解压成功,删除文件{FILENAME1_}')
                print(f'')
                os.remove(FILENAME1_)
            else:
                #print(cmd_error)
                errot_2 = cmd_error.strip()[:50]
                print("             ",errot_2)
                print(f'                文件夹密码失效 ')
                if ("Incorrect password" in cmd_error) or ('error' in cmd_error):
                    for i in pass_lists2:
                        SSTR = ' '.join(["unrar.exe","x",FILENAME2_,f"-p{i}","-o+",ex_dir])
                        #print(f"SSTR = {SSTR}")
                        #print('')
                        print(f"                                   尝试密码  {i}                ",end='\r')
                        obj = subprocess.Popen(SSTR,bufsize=1 , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                        cmd_out,cmd_error = obj.communicate()
                        if ("All OK" in cmd_out):
                            print('')
                            print('')
                            print('')
                            print('\033[1;32m' + '解压成功' + '\033[0m')
                            print(f'解压成功！！！！！！！！密码=    {i}     ！！！！！！！！')
                            print(f'删除文件{FILENAME1_}')
                            with open(FILENAME1_+f"成功密码{i}.txt",mode="w",encoding="utf-8") as f:  #写文件,当文件不存在时,就直接创建此文件
                                pass
                            END_ = 1
                            os.remove(FILENAME1_)
                            #print(f'-----------')
                            #time.sleep(1)
                            break
                    #所有密码均尝试， 尝试无密码解压
                    if END_ == 1:
                        continue #下一文件
                    if END_ == 0:
                        #print('     尝试无密码解压')
                        SSTR = ' '.join(["unrar.exe","x",FILENAME2_,f"-p{i}","-o+",ex_dir])
                        obj = subprocess.Popen(SSTR,bufsize=1 , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                        cmd_out,cmd_error = obj.communicate()
                        if ("All OK" in cmd_out):
                            print("")
                            print("")
                            print("")
                            print('\033[1;32m' + '解压成功' + '\033[0m')
                            print(f'解压成功！！！！！！！！无密码解压！！！！！！！！')
                            print(f'删除文件{FILENAME1_}')
                            with open(FILENAME1_+f"无密码解压.txt",mode="w",encoding="utf-8") as f:  #写文件,当文件不存在时,就直接创建此文件
                                pass
                            os.remove(FILENAME1_)
                            continue
                        else:
                            print("")
                            print("")
                            print("")
                            print(f"                解压失败 密码未知")
                            error_files.append(FILENAME1_)
                            continue#下一文件
                        

                    #print("不应执行此行")
print('=============================================')
print('end \n\r 未解压文件如下')
for i in error_files:
    print(i)
