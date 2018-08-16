#!/usr/bin/python3
# coding: utf-8
import os
import os.path
import json
import subprocess,signal
import time
#s new_attch_list
un_upload_list =[]
uploaded_list = []

with open('/mnt/un_upload.json', 'r') as r:
    un_upload_list = json.load(r)
with open('/mnt/uploaded.json', 'r') as r:
    uploaded_list = json.load(r)


print(un_upload_list)

import subprocess
for line in un_upload_list:
    
    print(line)
    print("filename_str")
    filename_str = line.split("/")[-1]
    print(filename_str)

    print("playlist")
    playlist_str = line.split("/")[-2]
    print(playlist_str)
    
    print("Title")
    title_str = filename_str.split("_")[0]
    print(title_str)
    
    print("time")
    time_str = line.split("_")[-1].split(".")[0]
    print(time_str)
    #print("===========================================")
    command = ["youtube-upload", "--title="+title_str, "--description",time_str,"--default-language","en","--privacy=private", "--client-secrets=/home/e001/Desktop/auth/client_secret.json", "--credentials-file=/home/e001/Desktop/auth/my_credentials.json", "--playlist='"+playlist_str+"'",line]
    child = subprocess.Popen(command)
    child.wait()
    #child2 = subprocess.Popen(["mv","/mnt/_temp/output",line])
    #child2.wait()
    print("===========================================")
    print("next")
    
    
   #读写 完成列表 

    
    with open('/mnt/un_upload.json', 'r') as r:
        un_upload_list = json.load(r)
    
    un_upload_list.remove(line)
    
    with open('/mnt/un_upload.json', 'w') as f:  
        f.write(json.dumps(un_upload_list))

    with open('/mnt/uploaded.json', 'r') as r:
        uploaded_list = json.load(r)
    uploaded_list.append(line)
    
    with open('/mnt/uploaded.json', 'w') as f:  
        f.write(json.dumps(uploaded_list))                              
                              
print("全部完成")
