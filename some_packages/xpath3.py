"""
    @time: 2022/12/14
    @author: rdyan0053
"""
from lxml import etree
import requests

url = 'https://www.aqistudy.cn/historydata/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X)'
}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)

# 解析热门城市
hot_li_list = tree.xpath('//div[@class="bottom"]/ul[@class="unstyled"]/li')
for li in hot_li_list:
    city_name = li.xpath('./a/text()')[0]
    print(city_name)
print('=' * 50)

# 解析全部城市
all_li_list = tree.xpath('//div[@class="all"]/div[@class="bottom"]//li/a')
for li in all_li_list:
    city_name = li.xpath('./text()')[0]
    print(city_name)
print('=' * 50)

# 解析热门城市+所有城市
# 此处xpath表达式的管道符（|）可以是的xpath表达式更加具有通用性
li_list = tree.xpath('//div[@class="bottom"]/ul/li | //div[@class="bottom"]/ul/div[2]/li')
for li in li_list:
    city_name = li.xpath('./a/text()')[0]
    print(city_name)
