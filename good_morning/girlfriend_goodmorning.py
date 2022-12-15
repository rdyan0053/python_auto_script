# coding=utf-8
"""
    截至2022年10月，此版本仍然生效
"""
import time
import datetime

import requests

from email.mime.text import MIMEText
import smtplib
from smtplib import SMTP_SSL  # 加密邮件内容，防止中途被截获

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

host_server = "smtp.163.com"
mail_user = "xxx@163.com"  # 此处填你的邮箱
mail_girl = "xxx@qq.com"  # 你女票的邮箱
# mail_girl = "xxx@qq.com" #你女票的邮箱
pwd = "xxx"  # 授权码

name_girl = "xxx"  # 你女票的名字
mail_port = 465


def getWeather():
    r = requests.get('http://www.jcznedu.com:5000/weather/now/?city=%E8%B5%A3%E5%B7%9E', verify=False)
    if 'success' in r.text:
        r = r.json()['data']
        name = r['location']['name']
        temperature = r['now']['temperature']
        return f'地区：{name} 当前温度：{temperature}'
    return '哎鸭，他忘了天气:('


def getTime():
    today = datetime.datetime.now() + datetime.timedelta(hours=+8)
    date2 = time.strptime('2022-12-24', "%Y-%m-%d")
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    t = today.timetuple()
    days = (date2 - today).days
    return f'今天是{t.tm_year}年{t.tm_mon}月{t.tm_mday}日 星期{t.tm_wday + 1} 考研倒计时：{days}天'


def getSoup():
    r = requests.get('https://www.iowen.cn/jitang/api/', verify=False)
    if '数据获取成功' in r.text:
        return r.json()['data']['content']['content']
    return '高考在昨天，考研在明天，今天没有什么事儿。'


def getPi():
    r = requests.get('https://api.shadiao.pro/chp', verify=False)
    if 'data' in r.text:
        res = r.json()['data']['text']
        return res
    else:
        return '你上辈子一定是碳酸饮料吧，为什么我一看到你就开心的冒泡' + '\t:(想不出其他的话来了'


def morning():
    return '\n'.join([getTime(), getSoup(), getWeather(), getPi()])


def night():
    return '\n'.join([getSoup(), getPi(), f'晚安，{name_girl}同学，今天你也是最棒的，继续加油鸭！'])


def getTimeX():
    t = int(time.strftime("%H", time.localtime())) + 8
    if t > 24:
        t = t - 24
    return 'morning' if t < 11 else ('noon' if t < 17 else 'afterNoon')


def main_handler(event=None, context=None):
    smtp = SMTP_SSL(host_server)  # SSL登录  创建SMTP对象
    try:
        smtp.login(mail_user, pwd)      # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
    except smtplib.SMTPException as e:
        print(e)
        logger.info(e)
        return False
    content = night() if getTimeX() == 'afterNoon' else morning()
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = mail_user
    message['To'] = mail_girl
    message['Subject'] = f'早安，{name_girl}' if getTimeX() != 'afterNoon' else '晚安，xxx'
    try:
        smtp.sendmail(mail_user, [mail_girl], message.as_string())  # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
        logger.info("send email success")
    except smtplib.SMTPException as e:
        logger.info(e)
        logger.info("Error: send email fail")
    logger.info(content)
    smtp.quit()  # 关闭SMTP对象
    return content


main_handler()  # 放到云函数上注释此行代码
