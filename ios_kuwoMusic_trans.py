
# coding: utf-8

# In[118]:


__author__ = ''
import sqlite3
import os
conn=sqlite3.connect("//mnt2/无损音乐/0000/cloud.db")
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# In[119]:

def GetNewFilename(filename):
    try:
        cu = conn.cursor()
        cu.execute("select artist,title,album,file,format from musicResource where file='%s'"%filename)
        r = cu.fetchone()
    except IOError:
        print "Error: 没有找到文件或读取文件失败"  
        
    else:
        print "内容写入文件成功"


    if r is not None:
        artist,title,album,filename,format=r
        newfilename2 = "%s-%s.%s"%(artist,title,format)
        print(newfilename2)
        newfilename2.replace("&","").replace(":","").replace(" ","").replace("/","")
        print(newfilename2)
        
        return newfilename2

def ConvertFiles(path):
    if not os.path.exists(path):
        exit()
    pl = os.listdir(path)
    print(pl)
    for file in pl:
#如果不是目录就移动
#计算新文件名
        print(file)
        if os.path.isfile(os.path.join(path,file)) :
            newfilename = GetNewFilename(file)
            if newfilename is not None:
                print(path)
                print(os.path.join(path,file),"-->",os.path.join(path,newfilename))
            
                os.rename(os.path.join(path,file),os.path.join(path,newfilename))


# In[120]:


ConvertFiles('//mnt2/无损音乐/0000/Music/')


conn.close()


# In[ ]:




# In[ ]:




# In[ ]:



