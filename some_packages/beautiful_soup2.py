"""
    在使用vpn魔法上网的时候，下面的代码就会报错，具体错误如下：
    Max retries exceeded with url: /book/sanguoyanyi.html (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:852)'),))
    还不知道为什么会这样！！！
"""
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46'
}
# 首页地址
main_url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
# 发起请求，获取了主页页面源码

response = requests.get(url=main_url, headers=headers)
response.encoding = 'utf-8'
page_text = response.text
# 数据解析：章节标题+详情页链接
soup = BeautifulSoup(page_text, 'lxml')  # 还是和本地html解析有点像
a_list = soup.select('.book-mulu > ul > li > a')
fp = open('./sanguo.txt', 'w', encoding='utf-8')
for i, a in enumerate(a_list):
    # if i > 9:
    #     break
    title = a.string  # 章节标题
    detail_url = 'https://www.shicimingju.com' + a['href']  # 详情页地址
    # 请求详情页的页面源码数据
    response = requests.get(url=detail_url, headers=headers)
    response.encoding = 'utf-8'
    detail_page_text = response.text
    # 解析：解析章节内容
    d_soup = BeautifulSoup(detail_page_text, 'lxml')
    div_tag = d_soup.find('div', class_='chapter_content')
    content = div_tag.text  # 章节内容
    fp.write(title + ':' + content + '\n')
    print(title, '爬取保存成功！')
fp.close()
