
# coding: utf-8

# In[53]:

#huoqu Url
import requests  
import re  
import os
#下面三行是编码转换的功能  
import sys  
  

  
#hea是我们自己构造的一个字典，里面保存了user-agent。  
#让目标网站误以为本程序是浏览器，并非爬虫。  
#从网站的Requests Header中获取。【审查元素】  
hea = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}  


html_tempfile = 'temphtml.txt'
os.remove(html_tempfile)
for i in range(30,55):
    print(i,"..")
    url_request = 'http://www.iwara.tv/videos?page=' + str(i)

    html = requests.get(url_request,headers = hea)  
  
    html.encoding = 'utf-8' #这一行是将编码转为utf-8否则中文会显示乱码
    
    with open(html_tempfile,"a") as t:
        t.write(html.text + "\n")
        t.close

        
        


# In[80]:

#chuli url
        
#wenjian duqu a
with open(html_tempfile,"r") as t:
        a = t.read()
        print(type(a))
        
print(type(a))

res = r'<a\ href="\/videos\/[^\s]+">'

m_tr = re.findall(res,a,re.S|re.M)

#print(m_tr)

type(m_tr)
#print(m_tr)

endset = set(m_tr) #合并 一样的地址JJ


#print (endset)

for line in endset: 
    temp = line[6:-1]
#    front = 'http://www.iwara.tv'
#    print(line[6:-1])#

file = 'endlist.txt'
with open(file,"w") as f:
    for line in endset: 
        temp = line[9:-2]
        front = 'http://ecchi.iwara.tv'
        end = '\n'
        print(temp)
        f.write(front + temp + end)


# In[ ]:




# In[ ]:


