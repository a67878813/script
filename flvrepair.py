# coding: utf-8
#2019.11.24 refixed in ubuntu19.10
#使用前需安装yamdi
#sudo apt install yamdi
#ubuntu 16.04LTS
#与win机器mount命令示例：
#sudo mount -t cifs -o username="用户名",password="密码",uid=1000 //192.168.2.90/raid5_5-9/直播录像 /mnt2
#若目录不存在,terminal中
#sudo mkdir mnt2
#sudo chown -R linux用户名：linux用户名 mnt2 


#使用方法 ：
#1.修改脚本预计遍历flv的目录（contents变量）后
#2.终端（terminal）中 cd 进入相应目录。 
#python3 flvrepair2.py

import os
import os.path
import json
import random
import pickle
import time
from termcolor import colored
#子进程相关模块
import subprocess
#contents为预计遍历flv目录
contents = "/mnt"

#******************************
error_counts = 0

s =[]
for root, dirs, files in os.walk(contents):
    for name in files:
        s.append(os.path.join(root, name))



#可注释掉
#print(s)


end_list = []

try:
    with open(contents+'/done_list.json', 'r') as r:
        done_list = json.load(r)

    
except FileNotFoundError:
    print("donelist is not exist")
    done_list = []
    with open(contents+'/done_list.json', 'w') as f:
        f.write(json.dumps(done_list))
        


        
for line in s:
#未修复的flv文件，追加到end_list中
    if (".flv" in line) and (line not in done_list):
        end_list.append(line)
print_list=end_list[:3]
for i in print_list:
    print(i)
print(colored(("	未添加meta数据的flv文件数 =  " + str(len(end_list))),"cyan"))

#判断临时目录是否存在
if os.path.isdir(contents+"/_temp"):
    pass
else:
    os.mkdir(contents+"/_temp")
    print("临时目录已建立")
    
#
#os.remove(contents+"/_temp")
for line in end_list:
    #
    try:
        ctime = os.path.getctime(line)
    except :
        error_counts +=1
        continue

#
    salt_ = random.randint(110, 880)
    print(colored("进行meta注入 = "+str(line),"green"))
    try:
        child = subprocess.Popen(["/usr/bin/yamdi","-i",line,"-o",contents+"/_temp/output.tmp"],stderr=subprocess.STDOUT)
        child.wait()
        
    except:
        error_counts +=1
        print(colored("meta信息写入错误","red"))
        print(colored(line,"red"))
        print(child.stderr)
        continue
    time.sleep(10)
    try:
        child2 = subprocess.Popen(["mv","-f",contents+"/_temp/output.tmp",line],stderr=subprocess.STDOUT)
        child2.wait()    #等待子进程结束，父进程继续
    except :
        error_counts +=1
        print(colored("mv错误","red"))
        print(colored(line,"red"))
        continue
    time.sleep(10)
 #   
    try:
        os.utime(line, (ctime,ctime))
    except :
        error_counts +=1
        continue
    print(colored("meta注入完成 = "+str(line),"green"))
    print(colored("next","green"))
    
    
   #更新 完成列表 

    
    try:
        with open(contents+'/done_list.json', 'r') as r:
            done_list = json.load(r)
    except:
        continue
    
    done_list.append(line)
    
    with open(contents+'/done_list.json', 'w') as f:  
        f.write(json.dumps(done_list))
        
    try:
        with open(contents+'/done_list.pik', 'wb') as f:  
            pickle.dump(done_list,f)
    except:
        continue


print(colored(("Error_Counts =" + str(error_counts)),"red"))

if error_counts == 0 :
    print(colored("全部完成","green"))
else:
    print(colored("全部完成 with error = "+str(error_counts),"red"))
