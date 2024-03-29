from utils.http_utils import httpx
import re
import os
from configs.path_config import TEXT_PATH

url = 'https://shindanmaker.com/'


# 获取token和cookie
async def huoqu():
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47'
    }
    session = httpx.get('https://shindanmaker.com/587874', headers=header)
    # 获取token
    token = re.compile(r'<meta name="csrf-token" content="(.*?)">').findall(session.text)[0]
    shindan_token = re.compile(r'name="shindan_token" value="(.*?)">').findall(session.text)[0]
    a = str(session.cookies)
    x = re.compile(r'XSRF-TOKEN=(.*?) for .shindanmaker.com').findall(a)[0]
    y = re.compile(r'_session=(.*?) for .shindanmaker.com').findall(a)[0]
    cookie = '_session=' + y + ';' + '__dui=' + x
    # 写入token
    filename = TEXT_PATH / 'token.txt'
    COOKIE = TEXT_PATH / "COOKIE.txt"
    shindan_tokentxt = TEXT_PATH / 'shindan_token.txt'
    with open(filename, 'w') as file_object:
        file_object.write(token)
        file_object.close()
    # 写入cookie
    with open(COOKIE, 'w') as u:
        u.write(cookie)
        u.close()
    # 写入shindan_token
    with open(shindan_tokentxt, 'w') as u:
        u.write(shindan_token)
        u.close()


#填入请求头
def cookietoken(id):
    tr = open(TEXT_PATH / "token.txt", 'r')
    fr = open(TEXT_PATH / "COOKIE.txt", 'r')
    ur = open(TEXT_PATH / "shindan_token.txt", 'r')
    cookie = fr.read()
    token = tr.read()
    shindan_token = ur.read()
    tr.close()
    fr.close()
    ur.close()
    params = ({
        '_token': token,
        'shindanName': id,
        'hiddenName': '名無しのY',
        'type': 'name',
        'shindan_token': shindan_token
    })
    header = {
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47'
    }
    return params, header


# 异世界转生
async def yishijie(id):
    x = cookietoken(id)
    params = x[0]
    header = x[1]
    urls = url + "587874"
    r = httpx.post(urls, headers=header, params=params)
    e = str(re.compile(r'<span class="shindanResult_name">(.*?)</span> </span>').findall(r.text)[0])
    x = re.sub(r'<br />', "\n", e)
    y = re.sub(r"&nbsp;|</span>", " ", x)
    z = re.sub(r'&amp;', '&', y)
    return z


# 今天是什么少女
async def jintian(id):  #
    x = cookietoken(id)
    params = x[0]
    header = x[1]
    urls = url + "162207"
    r = httpx.post(urls, headers=header, params=params)
    e = str(re.compile(r'class="post_result bg-light py-2 px-3 text-break">(.*?)</div>').findall(r.text)[0])
    return e


# 卖萌
async def maimeng(id):
    x = cookietoken(id)
    params = x[0]
    header = x[1]
    urls = url + "360578"
    r = httpx.post(urls, headers=header, params=params)
    e = str(re.compile(r'class="post_result bg-light py-2 px-3 text-break">(.*?)</div>').findall(r.text)[0])
    y = re.sub(r"&nbsp;", " ", e)
    return y


# 抽老婆
async def laopo(id):
    x = cookietoken(id)
    params = x[0]
    header = x[1]
    urls = url + "1075116"
    r = httpx.post(urls, headers=header, params=params)
    text = str(
        re.compile(r'<span class="shindanResult_name">(.*?)<img class="d-block shindanResult_image').findall(r.text)[0])
    img = str(
        re.compile(r'img class="d-block shindanResult_image rounded my-1 mx-auto" src="(.*?)">『').findall(r.text)[0])
    lao = str(re.compile(r'.jpg">(.*?)</span>').findall(r.text)[0])
    y = re.sub(r"</span>", "", text)
    return y, img, lao


# 特殊能力
async def power(id):
    x = cookietoken(id)
    params = x[0]
    header = x[1]
    urls = url + "1110781"
    r = httpx.post(urls, headers=header, params=params)
    e = str(re.compile(r'class="shindanResult_name">(.*?)</div></div>').findall(r.text)[0])
    y = re.sub(r"</span>", "", e)
    text = re.sub(r"<br />", "\n", y)
    return text