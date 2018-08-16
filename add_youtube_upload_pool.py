#!/usr/bin/python3
# coding: utf-8

import os
import os.path
import json
import subprocess,signal
import time
#s new_attch_list
s =[]
for root, dirs, files in os.walk("/mnt/yifa"):
    for name in files:
        s.append(os.path.join(root, name))


uploaded_list = []

with open('/mnt/un_upload.json', 'r') as r:
    un_upload_list = json.load(r)
with open('/mnt/uploaded.json', 'r') as r:
    uploaded_list = json.load(r)

for line in s:
#若不在完成列表中的flv or mp4文件，追加到list中
    if ((".flv" in line) or (".mp4" in line)) and (".png" not in line) and (line not in un_upload_list) and (line not in uploaded_list):
        un_upload_list.append(line)



for line in un_upload_list:
    print(line)

#print(uploaded_list)

with open('/mnt/un_upload.json', 'w') as f:  
    f.write(json.dumps(un_upload_list))
