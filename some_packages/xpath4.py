from lxml import etree
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
url = 'https://sc.chinaz.com/jianli/free.html'
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
page_text = response.text

# 数据解析:简历名称+详情页的url
tree = etree.HTML(page_text)
div_list = tree.xpath('//*[@id="container"]/div')       # 在元素页面中右键->复制->复制xpath

for div in div_list:
    title = div.xpath('./p/a/text()')[0] + '.rar'
    detail_url = div.xpath('./p/a/@href')[0]
    print(title, detail_url)
    # 对详情页的url发起请求
    detail_page_text = requests.get(url=detail_url, headers=headers).text
    # 数据解析：下载地址
    tree = etree.HTML(detail_page_text)
    download_url = tree.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
    # 在下载请求建立模板
    data = requests.get(url=download_url, headers=headers).content
    with open(title, 'wb') as fp:       # 在当前文件夹写入爬取的简历
        fp.write(data)
    print(title, '保存下载成功！')
