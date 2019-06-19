
# coding: utf-8

# In[21]:


import requests
import re
from bs4 import BeautifulSoup

class weibo(object):
    def __init__(self):
#         self.url = "https://s.weibo.com/weibo/%25E7%258F%25A0%25E6%25B5%25B7%25E6%259A%25B4%25E9%259B%25A8?q=%E8%A7%86%E8%A7%89%E4%B8%AD%E5%9B%BD&scope=ori&suball=1&timescope=custom:2019-04-02:2019-04-02&Refer=g&page=2"
        self.headers = {'Cookie':"SINAGLOBAL=5015224074870.943.1556867441556; un=setemp@yeah.net; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhCgLHsyBeh.pL6Q6i8gH7d5JpX5KMhUgL.FoMpShe0S0eXeK-2dJLoI7909PxkdP5t; UOR=c.biancheng.net,widget.weibo.com,www.iqiyi.com; SCF=ApxjVIv3l2BVC8ll5XNGQ4-u_vlgoWZW1QtBHeeTgGMixcWPujv2iXYnMD6ABhUHCcD4CCUMxTZG9dxyY0dX1nk.; SUB=_2A25x94PSDeRhGeFP71ES9y3IyjmIHXVShPIarDV8PUNbmtBeLVakkW9NQTZvUgxE4IKr-YQmQT4F_mG3DBEnxpsC; SUHB=0BL4vLDzuQ1REr; _s_tentry=-; Apache=3021409967832.5977.1559491641521; ULV=1559491641868:10:3:2:3021409967832.5977.1559491641521:1559409723133; webim_unReadCount=%7B%22time%22%3A1559491734738%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A11%2C%22msgbox%22%3A0%7D; WBStorage=ce875ff0f41a253d|undefined",'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
       
        
        
    def send_requests(self, url):
        response = requests.get(url, headers = self.headers)
#         print(response.content.decode())
        return response.content.decode()
        
    
    
    # 展开全文c 的行要删掉；O网页链接 删掉
    def data_cleansing(self, data):
        soup = BeautifulSoup(data)
        [s.extract() for s in soup("a", attrs = {'action-type':'fl_fold'})]  # 删除收起全文按钮文本
        txt = soup.select(".txt")
        for comment in txt:
            if "展开全文" in comment.text:
                txt.remove(comment)
#                 print("aaaaaaaaaaaa")
       
     
        return txt  #  返回一页内的内容 
#         for comment in txt:
#             print(comment.text)
          
    
        
    
    
    
    def save_data(self, data, filename):
        file = open(r"Z:\\a\\vcg\\%s.txt" % filename , 'a', encoding="utf-8")
        for i in range(0, data.__len__()):
            data[i].text.encode('utf-8')
            line = data[i].text
            tobereplace = re.compile("O网页链接")
            line = tobereplace.sub("", line)
#             line = line.repalce("O网页链接", "")
#             line = line.repalce("网页链接", "")    # 不知道为什么不能用replace函数
            file.write(line)
        file.close()
        
        
        
    def run(self, url, filename):
        response = self.send_requests(url)
        txt = self.data_cleansing(response)
        self.save_data(txt, filename)

        
if __name__ == '__main__':
    wb = weibo()
    for x in range(1,31):
    url1 = "https://s.weibo.com/weibo/%25E7%258F%25A0%25E6%25B5%25B7%25E6%259A%25B4%25E9%259B%25A8?q=%E8%A7%86%E8%A7%89%E4%B8%AD%E5%9B%BD&scope=ori&suball=1&timescope=custom:2019-04-"
    url2 = str(x)
    url3 = ":2019-04-"
    url4 = "&Refer=g&page="
    url = url1 + url2 + url3 + url2 + url4
    for index in range(1,75):  # 暂定75，需要对pagenum进行处理
        url  = url + str(index)
        filename = url2
        wb.run(url, filename)




