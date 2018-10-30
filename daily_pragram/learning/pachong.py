# import requests
# res = requests.get('https://news.sina.cn/gn?vt=4&pos=3')
# res.encoding='utf-8'
# # print(res.text)
#
#
# from bs4 import BeautifulSoup
# html_sample= """
#  <html><head><title>The Dormouse's story</title></head>
#  <body>
#  <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
#  <p class="story">Once upon a time there were three little sisters; and their names were
#  <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
#  <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
#  <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
#  and they lived at the bottom of a well.</p>
#  <p class="story">...</p>
#  """
# soup = BeautifulSoup(html_sample,'html.parser')
# header = soup.select('title')
# # print(type(soup))
# print(soup.text)
# # print(header.text)
#
#
# m_f_con_t cm_tit

import requests
from bs4 import BeautifulSoup
res = requests.get('https://news.sina.cn/gn?vt=4&pos=3')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
# print(soup)
for news in soup.select('.m_f_con_t'):
    print(news)
    if len(news.select('h2')) > 0:
        h2 = news.select('h2')[0].text
        print(h2)
for news1 in soup.select('.m_f_con_add'):
    print(news)



# res_1 = requests.get('https://mjs.sinaimg.cn/wap/custom_html/wap/20181015/5bc42f97c28ee.html')
# soup_1= BeautifulSoup(res_1.text,'html.parser')
# print(soup_1)