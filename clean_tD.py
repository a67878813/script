import os 
import shutil
err_list = []
"""
高效率下载目录整理脚本
使用前自行测试，请勿用于非下载文件夹。
曾误操作3秒删除5T内容。。。增加部分防呆措施，效果自行测试


del_name_set
    文件名含有任意项目 ->删除文件

    项目 in 文件名


del_dir_set
    文件夹名完全匹配 ->删除文件夹及全部内容

    项目 == 文件夹名

rename_file_set
    文件名含有的项目， 删除文件名的指定部分

    项目 in 文件名

rename_dir_set

    文件夹名有的项目， 删除文件夹名的指定部分

    项目 in 文件名


    
fun：
    re_search_1()
    正则匹配删除文件
"""











del_name_set = {
"x u u 6",
".htm",
".url",
".txt",
"二维码",
"最新地址",
"扫码获取",
"美女荷官",
"kcf9.com",
".chm",
"扫码下载",
"社区t66y.com.jpg",
"最新网址",
".apk",
".mht",
"手机网址",
"强力推荐",
"广告位招商",
"扫码安装",
"禁手游",
"社 區 最 新 情 報.mp4",
"新 片 首 發 ",
"臺 灣 妹 妹 直 播"

}



del_dir_set = {
"宣傳文件",
"論壇文宣",
"2048",
"文宣",
"成人免费吃瓜"
}


import re
"""
\s 匹配空白字符
[]内匹配 单个或成组字符


"""
def re_search_1(in_name):
    aa = re.search("[a-z]uu[0-9][0-9].com",  in_name ) #Xuu00.com
    if aa ==None:
        aa = re.search("uu[a-z][0-9][0-9].com",  in_name ) #uuX00.com
    if aa ==None:
        aa = re.search("[uU][uU][a-zA-Z][0-9][0-9].mp4",  in_name ) #uuX00.com
    if aa ==None:
        aa = re.search("[a-zA-Z]\s[uU]\s[uU]\s[0-9]\s[0-9]\s",  in_name ) #X u u 0 0
    # n X  re.express
    if aa != None:
        print(in_name)
        #print(aa)
        return 1
    return 0
def del_names(in_name):
    #delete file
    for i in del_name_set:
        if i !="":
            if i in in_name:
                return 1
    #not del file
    return 0


def remove_dir(dir):
    if os.path.isdir(dir):
        shutil.rmtree(dir)

def del_dir_name(in_name):

    for i in del_dir_set:
        if i != "":
            if i == in_name:
                #del dir
                return 1
    #not del dir
    return 0

rename_file_set = {
"[fbzip.com]",
"[BT-btt.com]",
"hhd800.com@",
"[44x.me]",
"[Thz.la]"
}

rename_dir_set ={
"[BT-btt.com]",
"[7sht.me]",
"[44x.me]",
"[Thz.la]"

}

def rename_files(in_name,_root):
    for i in rename_file_set:
        if i !="":
            if i in in_name:
                #rename
                os.rename(_root +r'\\' + in_name, _root +r'\\' + in_name.replace(i,""))

def rename_dirs(in_name, _root):
    for i in rename_dir_set:
        if i !="":
            if i in in_name:
                #rename dir
                #print("here")
                #print(in_name)
                #print(_root)
                    
                try:
                    os.rename(_root +r'\\' + in_name, _root +r'\\' + in_name.replace(i,""))
                except FileExistsError:
                    #print(f"DIR Existed : {_root +'//' + in_name}")
                    err_list.append(f"target DIR Existed : {_root +'//' + in_name}")


def walk_del(dir_path):
    for root,dirs, files in os.walk(dir_path):
        #print("m",root)
        #print("dir",dirs)
        #print('f',files)
        
        for i_d in dirs:
            if del_dir_name(i_d):
                print(f"remove dir: {root+i_d}")
                remove_dir(root +r'\\' + i_d)
            
            #rename  父目录重命名后当次无法walk，需重命名的目录层次多，则需多运行几次。

            rename_dirs(i_d,root)


        for i_f in files:

            if re_search_1(i_f):
                print(f"remove file: {root+ '//' + i_f}")
                os.remove(root +r'\\' + i_f)
            if del_names(i_f):
                print(f"remove file: {root+ '//' + i_f}")
                os.remove(root +r'\\' + i_f)
            
            rename_files(i_f,root)

if __name__ == '__main__':
    print("BIGIN::")
    path_d= r"E:\\tD"
    walk_del(path_d)

    #path2= r"F:\\tD"
    #walk_del(path2)


    print("===============Err list ===========")
    for i in err_list:
        print(i)

