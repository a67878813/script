
# coding: utf-8

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
#contents为预计遍历flv目录
contents = "/mnt2"

#******************************


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
    print("donelist不存在，正在初始化")
    done_list = []
    with open(contents+'/done_list.json', 'w') as f:
        f.write(json.dumps(done_list))
        
        
for line in s:
#未修复的flv文件，追加到end_list中
    if (".flv" in line) and (line not in done_list):
        end_list.append(line)
print(end_list)


#子进程相关模块
import subprocess
#判断临时目录是否存在
if os.path.isdir(contents+"/_temp"):
    pass
else:
    os.mkdir(contents+"/_temp")
    print("临时目录已建立")
    
#清空临时目录。风险高
#os.remove(contents+"/_temp")
for line in end_list:
    #增加随机数 避免临时文件冲突
    salt = random.randint(11000, 88000)
    print(line)
    child = subprocess.Popen(["yamdi","-i",line,"-o",contents+"/_temp/output"+str(salt)])
    child.wait()
    child2 = subprocess.Popen(["mv",contents+"/_temp/output"+str(salt),line])
    child2.wait()
    #等待子进程结束，父进程继续
    print("next")
    
    
   #更新 完成列表 

    
    with open(contents+'/done_list.json', 'r') as r:
        done_list = json.load(r)
    
    done_list.append(line)
    
    with open(contents+'/done_list.json', 'w') as f:  
        f.write(json.dumps(done_list))
print("全部完成")



