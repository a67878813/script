# -*- coding: GB18030 -*-
import os
import os.path
import time
import sys
import subprocess
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--x", help="��ѹԴ", type=str,default="default")
parser.add_argument("--target", help="��ѹĿ��", type=str,default="default")
args = parser.parse_args()

#contents = "I:\\Ѹ������"
if args.x == 'default':
    contents = "W:\\b\\0020210209\\video"
else:
    contents = args.x
    

#contents = "Z:\\b\\0020191211"
print(contents)
#aim = "default"
if args.target == 'default':
    aim = "default"
else:
    aim = args.target
    
print(contents)
print(aim)

#exit()
#aim =  'L:\\��ѹ2'#������Ҫ���Ľ�ѹĿ�� ע�͵�����


s =[]
error_files=[]
#pass_lists = os.listdir("I:\\Ѹ������")# ����Ӵ�·�����ļ�������



pass_lists2 =[]


def append_pass_list(pass_lists):
    global pass_lists2
    for i in pass_lists:
        j  = i.replace('�Ǻ�','*').replace('[��б]','/')
        if "[]" in j:
            pass_lists2.append(j.split('[]')[0].strip())
            
        if "����" in j:
            pass_lists2.append(j.split("����")[0].strip())
            pass_lists2.append(j.split("����")[1].strip())
        if "��" in j:
            pass_lists2.append(j.split("��")[0].strip())
            pass_lists2.append(j.split("��")[1].strip())
        if " " in j:
            pass_lists2.append(j.split(" ")[0].strip())
            pass_lists2.append(j.split(" ")[1].strip())
        pass_lists2.append(j.replace(' ',''))
    for i in pass_lists:
        j  = i.replace('�Ǻ�','*')#.replace('&','^&')
        pass_lists2.append(j)
        
        

#append_pass_list(os.listdir("Z:\\b\\0020191211"))
#append_pass_list(os.listdir("B:\\����"))
#append_pass_list(os.listdir("I:\\Ѹ������"))
#if contents != 'I:\\Ѹ������':
append_pass_list(os.listdir(contents))
print(pass_lists2)


def delete_serial_files(_filename):
    if _filename[-2:] == "01":
        for j in range(2,20):
            try:
                if j  < 10 :
                    os.remove(_filename[:-1] + str(j)  )
                else:
                    os.remove(_filename[:-2] + str(j)  )
            except:
                print(f"                 ɾ��ֹͣ�� {j}")
                break
    if _filename[-6:] == "t1.rar":
        for j in range(2,20):
            try :
                if j  <= 10 :
                    os.remove(_filename[:-6] + "t" +  str(j)  + ".rar" )
                else:
                    os.remove(_filename[:-6] + "t" +  str(j)   + ".rar" )
            except:
                print(f"                 ɾ��ֹͣ�� {j}")
                break
    return 0 

def need_unzip(_name):
    name_ = _name.lower()
    if "ding" in name_:#downloading
        return 0
    if "rent" in name_:#torrent
        return 0
    if "mkv" in name_:
        return 0
    if "flv" in name_:
        return 0
    if "ssa" in name_:
        return 0
    if "wmv" in name_:
        return 0    
    if "mts" in name_:
        return 0    
    if "jfif" in name_:
        return 0    
    if "3gp" in name_:
        return 0    
    if "rmvb" in name_:
        return 0    
    if "htm" in name_:
        return 0    
    if "psd" in name_:
        return 0    
    if "mp4" in name_:
        return 0
    if "mp3" in name_:
        return 0
    if "jpg" in name_:
        return 0
    if ".cc" in name_:
        return 0
    if "jpeg" in name_:
        return 0
    if "webp" in name_:
        return 0
    if "ass" in name_:
        return 0
    if "heic" in name_:
        return 0
    if "png" in name_:
        return 0
    if "txt" in name_:
        return 0
    if ".ts" in name_:
        return 0
    if "avi" in name_:
        return 0
    if "mpg" in name_:
        return 0
    if "mov" in name_:
        return 0
    if "webm" in name_:
        return 0
    if "mobi" in name_:
        return 0
    if "srt" in name_:
        return 0
    if "bmp" in name_:
        return 0
    if "gif" in name_:
        return 0
    if "url" in name_:
        return 0
    if "lnk" in name_:
        return 0
    if "pdf" in name_:
        return 0
    if ".db" in name_:
        return 0
    
    return 1
    
for root, dirs, files in os.walk(contents):
    nested_levels = root.split('\\')
    #if len(nested_levels) ==4:
    #    del dirs[:]
    #del dirs[:]��ɾ���б�����ݣ��������ö����б�������滻dirs��������ʱ���͵��޸��б����Ҫ��

    for name in files:
        filename_unfilt =  name[-4:]
        
        if need_unzip(filename_unfilt): #�ų���֪��չ��
        #if ('7z' in name[-4:] ) or('zip' in name[-4:] )  : #ָ����չ��

            print('         --------')
            END_ = 0
            print(f'name ={name}')
            #print(f'dirs ={dirs}')
            #print(f'root ={root}')
            a_ = root[len(contents):]
            #print(f'a_ ={a_}')
            a2_ = a_.split('\\')
            if len(a2_) == 1 :
                PASSWORD1_ = "test"
            else:
                PASSWORD1_ = a2_[1]
            
            PASSWORD1_ = PASSWORD1_.replace('�Ǻ�','*').replace('[��б]','/')
            #print(f'        password ={PASSWORD1_}')
            
            ex_dir = root  +"\\"
            ex_dir = '\"' + ex_dir  + '\"'
            
            
            if aim != "default":
            
            
                #print(root[len(contents):].split('\\')   )
                #temp_list = root[len(contents):].split('\\')
                #temp_list[1] = 'test'
                #print(temp_list)
                #dd = "\\".join(temp_list)
                #print(dd)
                #print(root[len(contents):].split('\\')   )
                
                ex_dir = '\"' + aim  +root[len(contents):]  + '\"'#Ŀ���ļ���
            FILENAME1_ = root +'\\'+ name
            FILENAME2_ = '\"' + FILENAME1_  + '\"'
            print(f'        filename1 ={FILENAME1_}')

            #��ѹ����
            SSTR = ' '.join(["7z.exe","x -aoa ",FILENAME2_,f"-p{PASSWORD1_}",f"-o{ex_dir}",])
            print(f"        SSTR = {SSTR}")
            #continue
            
            obj = subprocess.Popen(SSTR,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            cmd_out,cmd_error = obj.communicate()
            #print(cmd_out)
            if "Everything is Ok" in cmd_out:
                print(f'��ѹ�ɹ�      ')
                print('\033[1;32m' + '��ѹ�ɹ�' + '\033[0m')
                print(f'ɾ���ļ�{FILENAME1_}')
                os.remove(FILENAME1_)
                print("ffffffff",FILENAME1_[-6:])
                delete_serial_files(FILENAME1_)
            else:
                errot_2 = cmd_error.strip()[:50]
                print("             ",errot_2)
                print(f'                �ļ�������ʧЧ ')
                if "Wrong password" in cmd_error:
                    for i in pass_lists2:#
                        if aim != "default":
                            #print(root[len(contents):].split('\\')   )
                            temp_list = root[len(contents):].split('\\')
                            temp_list[1] = i.replace('*','�Ǻ�')
                            #print(temp_list)
                            dd = "\\".join(temp_list)
                            #print(dd)
                            '''
                            root =O:\sex169����\gZu2(b1I0-Dc&3t6\й¶\MJ
                            ['', 'gZu2(b1I0-Dc&3t6', 'й¶', 'MJ']
                            ['', 'test', 'й¶', 'MJ']
                            \test\й¶\MJ
                            
                            '''
                            
                            ex_dir = '\"' + aim  +dd  + '\"'
                            #ex_dir = '\"' + aim  + i.replace('*','�Ǻ�') + '\"'
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
                            with open(FILENAME1_+f"�ɹ�����{i.replace('*','�Ǻ�').replace('/','[��б]')}.txt",mode="w",encoding="utf-8") as f:  #д�ļ�,���ļ�������ʱ,��ֱ�Ӵ������ļ�
                                pass
                            print(f'ɾ���ļ�{FILENAME1_}')
                            os.remove(FILENAME1_)
                            
                            print("ffffffff",FILENAME1_[-5:])
                            delete_serial_files(FILENAME1_)
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
    