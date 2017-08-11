#!/usr/bin/python3
#可用于crontab 定时任务
import os
import subprocess,signal
import time

process_name_to_kill = []
process_name_to_kill.append('script')
process_name_to_kill.append('bash')
process_name_to_kill.append('xterm')

#check kill list
p = subprocess.Popen(['ps','-A'],stdout=subprocess.PIPE)
out,err = p.communicate()

for line in out.splitlines():
#   print(line)
    vars = line.split()

#    print(vars)
#    pid = int(line.split())
    try:
        pid = int(vars[0])
        proc_name = str(vars[3])
        for name in process_name_to_kill:
            if name in proc_name:
                print(pid, proc_name)
            
    except:
        continue

#kill among kill_list


for name in process_name_to_kill:
    try:
        kill_proc = os.system('pkill '+name)
    except:
        print('error')

#flvrepair
#import os
#import multiprocessing
#/usr/bin/gnome-software --gapplication-service
os.popen('xterm  -T 111 -display :0 +cm -geometry 50x35 -hold -e "cd /home/e001/SC2/;python3 /home/e001/SC2/flvrepair.py;exec bash;"')

#long_time_task(1)
time.sleep(30)

#restart
#inf_command = 'xterm  -T {0} -display :0 -hold -e "cd /home/e001/SC2/;./script'
#sup_command = ';exec bash;"'
for t in range(1,150):
    bash_command = 'xterm  -T {0} -display :0 +cm -geometry 100x10 -hold -e "export PATH=$PATH:/usr/local/bin;cd /home/e001/SC2/;./script{1};exec bash;"'.format('sc'+str(t),t)
    print(bash_command)
    time.sleep(0.6)
    os.popen(bash_command)
