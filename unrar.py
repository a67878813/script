# -*- coding: gbk -*-
import os
import os.path
import time
import sys
import subprocess
contents = 'I:\\Ѹ������'
print(contents)
pass_lists = os.listdir(contents)
pass_lists2 =[]
for i in pass_lists:
    j  = i.replace('�Ǻ�','*')
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
            if "�Ǻ�" in PASSWORD1_:
                PASSWORD1_ = PASSWORD1_.replace('�Ǻ�','*')
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
            
            #��ѹ����
            SSTR = ' '.join(["unrar.exe","x",FILENAME2_,f"-p{PASSWORD1_}","-o+",ex_dir])
            #print(f"    SSTR = {SSTR}")
            obj = subprocess.Popen(SSTR ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            cmd_out,cmd_error = obj.communicate()
            if ("All OK" in cmd_out):
                print(f'')
                print(f'')
                print(f'')
                print('\033[1;32m' + '��ѹ�ɹ�' + '\033[0m')
                print(f'��ѹ�ɹ�,ɾ���ļ�{FILENAME1_}')
                print(f'')
                os.remove(FILENAME1_)
            else:
                #print(cmd_error)
                errot_2 = cmd_error.strip()[:50]
                print("             ",errot_2)
                print(f'                �ļ�������ʧЧ ')
                if ("Incorrect password" in cmd_error) or ('error' in cmd_error):
                    for i in pass_lists2:
                        SSTR = ' '.join(["unrar.exe","x",FILENAME2_,f"-p{i}","-o+",ex_dir])
                        #print(f"SSTR = {SSTR}")
                        #print('')
                        print(f"                                   ��������  {i}                ",end='\r')
                        obj = subprocess.Popen(SSTR,bufsize=1 , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                        cmd_out,cmd_error = obj.communicate()
                        if ("All OK" in cmd_out):
                            print('')
                            print('')
                            print('')
                            print('\033[1;32m' + '��ѹ�ɹ�' + '\033[0m')
                            print(f'��ѹ�ɹ���������������������=    {i}     ����������������')
                            print(f'ɾ���ļ�{FILENAME1_}')
                            with open(FILENAME1_+f"�ɹ�����{i}.txt",mode="w",encoding="utf-8") as f:  #д�ļ�,���ļ�������ʱ,��ֱ�Ӵ������ļ�
                                pass
                            END_ = 1
                            os.remove(FILENAME1_)
                            #print(f'-----------')
                            #time.sleep(1)
                            break
                    #������������ԣ� �����������ѹ
                    if END_ == 1:
                        continue #��һ�ļ�
                    if END_ == 0:
                        #print('     �����������ѹ')
                        SSTR = ' '.join(["unrar.exe","x",FILENAME2_,f"-p{i}","-o+",ex_dir])
                        obj = subprocess.Popen(SSTR,bufsize=1 , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                        cmd_out,cmd_error = obj.communicate()
                        if ("All OK" in cmd_out):
                            print("")
                            print("")
                            print("")
                            print('\033[1;32m' + '��ѹ�ɹ�' + '\033[0m')
                            print(f'��ѹ�ɹ������������������������ѹ����������������')
                            print(f'ɾ���ļ�{FILENAME1_}')
                            with open(FILENAME1_+f"�������ѹ.txt",mode="w",encoding="utf-8") as f:  #д�ļ�,���ļ�������ʱ,��ֱ�Ӵ������ļ�
                                pass
                            os.remove(FILENAME1_)
                            continue
                        else:
                            print("")
                            print("")
                            print("")
                            print(f"                ��ѹʧ�� ����δ֪")
                            error_files.append(FILENAME1_)
                            continue#��һ�ļ�
                        

                    #print("��Ӧִ�д���")
print('=============================================')
print('end \n\r δ��ѹ�ļ�����')
for i in error_files:
    print(i)
