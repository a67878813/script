#!/usr/bin/python3
# coding: utf-8
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
        time.sleep(0.5)
    except:
        print('error')
print("wait 60s")
time.sleep(60)
#flvrepair
#import os
#import multiprocessing
#/usr/bin/gnome-software --gapplication-service
os.popen('xterm  -T 111 -display :0 +cm -geometry 50x35 -hold -e "cd /home/u2/SC2/;python3 /home/u2/SC2/flvrepair.py;exec bash;"')
print("wait 30s")
#long_time_task(1)
time.sleep(30)

#restart
#inf_command = 'xterm  -T {0} -display :0 -hold -e "cd /home/e001/SC2/;./script'
#sup_command = ';exec bash;"'
os.popen('xterm  -T 111 -display :0 +cm -geometry 50x35 -hold -e "cd /home/u2/SC2/;echo placeholder;exec bash;"')
for t in range(1,121):
    bash_command = 'xterm  -T {0} -display :0 +cm -geometry 100x10 -iconic -hold -e "export PATH=$PATH:/home/u2/.local/bin;cd /home/u2/SC2/;xdotool windowminimize $(xdotool getactivewindow);./script{1};exec bash;" &'.format('sc'+str(t),t,'sc'+str(t-1))
    path_temp = '/home/u2/SC2/script{0}'.format(t)
#aa = $(xdotool search --sync --name sc3)
#xdotool windowminimize $(xdotool search --sync --name sc2| head -n 1)
    print(bash_command)
    time.sleep(2.5)
    print(path_temp)
    if os.path.exists(path_temp):
        os.popen(bash_command)
        
