# 只爬取了第一页的内容
# from bs4 import BeautifulSoup
# import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
# }
# url = 'https://www.kuaidaili.com/free'
# page_text = requests.get(url=url, headers=headers).text
# soup = BeautifulSoup(page_text, 'lxml')
# trs = soup.select('tbody > tr')
# for tr in trs:
#     t1 = tr.findAll('td')[0]
#     t2 = tr.findAll('td')[1]
#     ip = t1.string
#     port = t2.string
#     print(ip, port)


# 爬取多页内容
from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
# 爬取多页
# 1.创建一个通用的url(可以变换成任意页码的url)
url = 'https://www.kuaidaili.com/free/inha/%d/'

# 2.通过循环以此生成不同页码的url
for page in range(1,11):
    print('----------正在爬取第%d页的数据！-----------' % page)
    # format用来格式化字符串的（不可以修改url这个字符串本身）
    new_url = format(url%page)
    print(new_url)
    # 循环发送每一页的请求
    # 注意：get方法是一个阻塞方法！(感觉不像是)
    # page_res = requests.get(url=new_url, headers=headers).text
    # 感觉下面这两行代码可以解决数据解析太快的问题，也就是代替上面一行的代码
    page_res = requests.get(url=new_url, headers=headers)
    page_text = page_res.text
    time.sleep(1)   # 防止数据解析太快
    soup = BeautifulSoup(page_text,'lxml')
    trs = soup.select('tbody > tr')
    for tr in trs:
        t1 = tr.findAll('td')[0]
        t2 = tr.findAll('td')[1]
        ip = t1.string
        port = t2.string
        print(ip, port)
