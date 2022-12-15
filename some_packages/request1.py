# import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
# }
# url = 'https://xueqiu.com/statuses/hot/listV2.json'
# param = {
#     "since_id": "-1",
#     "max_id": "311519",
#     "size": "15",
# }
# response = requests.get(url=url, headers=headers, params=param)
# data = response.json()
# print(data)
# 发现没有拿到我们想要的数据


import requests

# 1.创建一个空白的session对象
session = requests.Session()

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
}
main_url = 'https://xueqiu.com/'        # 第一次请求的url

# 2.使用session发起的请求，目的是为了捕获到cookie，且将其存储到session对象中
session.get(url=main_url, headers=headers)

url = 'https://xueqiu.com/statuses/hot/listV2.json'
param = {
    "since_id": "-1",
    "max_id": "311519",
    "size": "15",
}

# 3.就是使用携带了cookie的session对象发起的请求（就是携带者cookie发起的请求）
response = session.get(url=url, headers=headers, params=param)
data = response.json()
print(data)

"""
    最后得到的结果是：{'next_max_id': -1, 'items': [], 'next_id': -1}
    也不知道为什么session不起作用
"""