"""
    测试：访问如下网址，返回自己本机ip
    网址：https://www.baidu.com/s?wd=ip
    注意：不使用cookie无法获取正确数据（这里使用的是手动获取获取cookie）
"""

# import requests
# from lxml import etree
# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
#     'cookie': 'BIDUPSID=639D53467E9DE6F5572EB3EB1373C92E; PSTM=1658652098; BAIDUID=639D53467E9DE6F5BCE0675020CDCFBF:FG=1; BD_UPN=12314753; newlogin=1; MCITY=-189:; BDUSS=Hg0VTVlfk43dXMzOWItakd4S1JmYk9OcWxwfko1d1ZrVzRiRXc3LUlFMFRjTFpqSVFBQUFBJCQAAAAAAAAAAAEAAADvwhy8TUlESU5JREkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABPjjmMT445jU; BDUSS_BFESS=Hg0VTVlfk43dXMzOWItakd4S1JmYk9OcWxwfko1d1ZrVzRiRXc3LUlFMFRjTFpqSVFBQUFBJCQAAAAAAAAAAAEAAADvwhy8TUlESU5JREkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABPjjmMT445jU; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_NDk5MzUzMjFkMTFiNTdlMDJiYmU4MDc0ZjY3MjZkNzNiNDk5YTYyOWY2ZDg5YTMxZDAwMWRhNjQ2MGYwMzY0MDQ4NzAzMTA1OTMwZTRjY2RhMDA2OGNiYzBiOTdjMWY5NmRiN2Q1NDZkOTJkNjJlODhjOTZlYzA1NDRkMjNlZDI4ZGU0YTdmNjFkZjg0ODBmMDlhOTRmM2E2MWJiOTUxYTM3YjMyODk1ZThhNWFiNjIwYWJkOTZkNjcyZTMxNmYx; H_PS_PSSID=37855_36557_36920_37909_37835_37872_37883_36805_37921_37758_37901_26350_37957_37789_37881; BAIDUID_BFESS=639D53467E9DE6F5BCE0675020CDCFBF:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=3; H_PS_645EC=dc3euynBUZ05LSFkFZwijKJKRQKZHyr8Z1AN+DntFeG57di4Kf7sElingYg; BA_HECTOR=a001000lak8k8501al00ajtp1hpjkja1g; ZFY=:B1GZzdGIcREeWlH6NTV316yOod:BUkJs8mVIo82uzG6s:C; baikeVisitId=f5095188-a7fa-4288-b5cc-ca928383a65c; B64_BOT=1'
# }
# url = 'https://www.baidu.com/s?wd=ip'
# page_text = requests.get(url=url, headers=headers).text
# tree = etree.HTML(page_text)
# data = tree.xpath('//*[@id="1"]/div[1]/div[1]/div[2]//span[@class="c-gap-right"]/text()')[0]
# print(data)


"""
    使用session自动获取cookie并访问的方式
"""
# import requests
# from lxml import etree
# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
# }
# main_url = 'https://www.baidu.com'
# session = requests.Session()
# # 使用session发起的请求，目的是为了捕获到cookie，且将其存储到session对象中
# session.get(url=main_url, headers=headers)
# url = 'https://www.baidu.com/s?wd=ip'
# # 使用携带了cookie的session对象发起的请求（就是携带者cookie发起的请求）
# response = session.get(url=url, headers=headers)
# page_text = response.text
# tree = etree.HTML(page_text)
# data = tree.xpath('//*[@id="1"]/div[1]/div[1]/div[2]//span[@class="c-gap-right"]/text()')[0]
# print(data)


"""
    第三段代码，使用的是ip代理方式
"""
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
}
url = 'https://www.sogou.com/web?query=ip'
# 使用代理服务器发起请求
# proxies={'代理类型':'ip:port'}
page_text = requests.get(url=url, headers=headers, proxies={'https': '42.57.150.150:4278'}).text
tree = etree.HTML(page_text)
data = tree.xpath('//*[@id="ipsearchresult"]/strong/text()')[0]
print(data)
