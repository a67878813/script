# -*- coding: gbk -*-
import os
import os.path
import time
import sys
import subprocess
contents = 'I:\\Ѹ������'
print(contents)


s =[]
error_files=[]
pass_lists = os.listdir(contents)
pass_lists2 =[]
for i in pass_lists:
    j  = i.replace('�Ǻ�','*')#.replace('&','^&')
    pass_lists2.append(j)
print(pass_lists2)
for root, dirs, files in os.walk(contents):
    nested_levels = root.split('\\')
    #if len(nested_levels) ==4:
    #    del dirs[:]
    #del dirs[:]��ɾ���б�����ݣ��������ö����б�������滻dirs��������ʱ���͵��޸��б����Ҫ��

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
            if "�Ǻ�" in PASSWORD1_:
                PASSWORD1_ = PASSWORD1_.replace('�Ǻ�','*')
            #print(f'        password ={PASSWORD1_}')
            
            ex_dir = root  +"\\"
            ex_dir = '\"' + ex_dir  + '\"'
            FILENAME1_ = root +'\\'+ name
            FILENAME2_ = '\"' + FILENAME1_  + '\"'
            print(f'        filename1 ={FILENAME1_}')

            #��ѹ����
            SSTR = ' '.join(["7z.exe","x -aoa ",FILENAME2_,f"-p{PASSWORD1_}",f"-o{ex_dir}",])
            print(f"        SSTR = {SSTR}")
            obj = subprocess.Popen(SSTR,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            cmd_out,cmd_error = obj.communicate()
            #print(cmd_out)
            if "Everything is Ok" in cmd_out:
                #print(f'��ѹ�ɹ�')
                print('\033[1;32m' + '��ѹ�ɹ�' + '\033[0m')
                print(f'ɾ���ļ�{FILENAME1_}')
                os.remove(FILENAME1_)
            else:
                errot_2 = cmd_error.strip()[:50]
                print("             ",errot_2)
                print(f'                �ļ�������ʧЧ ')
                if "Wrong password" in cmd_error:
                    for i in pass_lists2:#
                        SSTR = ' '.join(["7z.exe","x -aoa ",FILENAME2_,f"-p{i}",f"-o{ex_dir}",])
                        print(f"                                   ��������  {i}                ",end='\r')
                        obj = subprocess.Popen(SSTR,bufsize=1 , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                        cmd_out,cmd_error = obj.communicate()
                        #print(cmd_error)
                        if "Everything is Ok" in cmd_out:
                            print("")
                            print("")
                            print("")
                            print('\033[1;32m' + '��ѹ�ɹ�' + '\033[0m')
                            print(f'��ѹ�ɹ�������������������={i}����������������')
                            with open(FILENAME1_+f"�ɹ�����{i}.txt",mode="w",encoding="utf-8") as f:  #д�ļ�,���ļ�������ʱ,��ֱ�Ӵ������ļ�
                                pass
                            print(f'ɾ���ļ�{FILENAME1_}')
                            os.remove(FILENAME1_)
                            END_ =1
                            print(f'')
                            time.sleep(1)
                            break
                        else:
                            pass
                    if END_ == 1:
                        continue #��һ�ļ�
                    if END_ == 0:
                        print("")
                        print("")
                        SSTR = ' '.join(["7z.exe","x -aoa ",FILENAME2_,f"-o{ex_dir}",])
                        #print(f"                                 �����������ѹ                ",end='\r')
                        obj = subprocess.Popen(SSTR,bufsize=1 , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                        cmd_out,cmd_error = obj.communicate()
                        #print(cmd_error)
                        if "Everything is Ok" in cmd_out:
                            print('\033[1;32m' + '��ѹ�ɹ�' + '\033[0m')
                            #print(f'��ѹ�ɹ�')
                            print(f'���������������������룡��������������')
                            with open(FILENAME1_+f"������.txt",mode="w",encoding="utf-8") as f:  #д�ļ�,���ļ�������ʱ,��ֱ�Ӵ������ļ�
                                pass
                            print(f'ɾ���ļ�{FILENAME1_}')
                            os.remove(FILENAME1_)
                            continue##��һ�ļ�
                        else:
                            print("")
                            print("")
                            print("")
                            print(f"                ��ѹʧ�� ����δ֪")
                            error_files.append(FILENAME1_)
                            continue#��һ�ļ�
                    #print("����")

print('=============================================')
print('end \n\r δ��ѹ�ļ�����')
for i in error_files:
    print(i)
    