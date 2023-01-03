from utils.http_utils import httpx
import re
import os
from configs.path_config import TEXT_PATH

url = 'https://shindanmaker.com/'


# 获取token和cookie
async def huoqu():
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
    }
    session = httpx.get('https://shindanmaker.com/587874', headers=header)
    # 获取token
    token = re.compile(r'<meta name="csrf-token" content="(.*?)">').findall(session.text)[0]
    a = str(session.cookies)
    x = re.compile(r'XSRF-TOKEN=(.*?) for .shindanmaker.com').findall(a)[0]
    y = re.compile(r'_session=(.*?) for .shindanmaker.com').findall(a)[0]
    cookie = '_session=' + y + ';' + 'name=' + x
    # 写入token
    filename = TEXT_PATH / 'token.txt'
    COOKIE = TEXT_PATH / "COOKIE.txt"
    with open(filename, 'w') as file_object:
        file_object.write(token)
        file_object.close()
    # 写入cookie
    with open(COOKIE, 'w') as u:
        u.write(cookie)
        u.close()


# 异世界转生
async def yishijie(id):
    tr = open(TEXT_PATH / "token.txt", 'r')
    fr = open(TEXT_PATH / "COOKIE.txt", 'r')
    cookie = fr.read()
    token = tr.read()
    tr.close()
    fr.close()
    params = ({
        '_token': token,
        'shindanName': id,
        'hiddenName': '名無しのY'
    })
    header = {
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
    }
    urls = url + "587874"
    r = httpx.post(urls, headers=header, params=params)
    e = str(re.compile(r'id="copy-textarea-all" rows="5">(.*?)&#10;#shindanmaker&#10;').findall(r.text)[0])
    x = re.sub(r'&#10;', "\n", e)
    y = re.sub(r"</span>|amp;", "", x)
    return y


# 今天是什么少女
async def jintian(id):  #
    tr = open(TEXT_PATH / "token.txt", 'r')
    fr = open(TEXT_PATH / "COOKIE.txt", 'r')
    cookie = fr.read()
    token = tr.read()
    tr.close()
    fr.close()
    params = ({
        '_token': token,
        'shindanName': id,
        'hiddenName': '名無しのY'
    })
    header = {
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
    }
    urls = url + "162207"
    r = httpx.post(urls, headers=header, params=params)
    e = str(re.compile(r'textarea" id="copy-textarea-140" rows="5">(.*?)&#10;#shindanmaker&#10;').findall(r.text)[0])
    return e


# 卖萌
async def maimeng(id):
    tr = open(TEXT_PATH / "token.txt", 'r')
    fr = open(TEXT_PATH / "COOKIE.txt", 'r')
    cookie = fr.read()
    token = tr.read()
    tr.close()
    fr.close()
    params = ({
        '_token': token,
        'shindanName': id,
        'hiddenName': '名無しのY'
    })
    header = {
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
    }
    urls = url + "360578"
    r = httpx.post(urls, headers=header, params=params)
    e = str(re.compile(r'style="display: none;">(.*?)&#10;&#10;#kaomoji #shindanmaker&#10;').findall(r.text)[0])
    return e


# 抽老婆
async def laopo(id):
    tr = open(TEXT_PATH / "token.txt", 'r')
    fr = open(TEXT_PATH / "COOKIE.txt", 'r')
    cookie = fr.read()
    token = tr.read()
    tr.close()
    fr.close()
    params = ({
        '_token': token,
        'shindanName': id,
        'hiddenName': '名無しのY'
    })
    header = {
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
    }
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
    tr = open(TEXT_PATH / "token.txt", 'r')
    fr = open(TEXT_PATH / "COOKIE.txt", 'r')
    cookie = fr.read()
    token = tr.read()
    tr.close()
    fr.close()
    params = ({
        '_token': token,
        'shindanName': id,
        'hiddenName': '名無しのY'
    })
    header = {
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
    }
    urls = url + "1110781"
    r = httpx.post(urls, headers=header, params=params)
    e = str(re.compile(r'class="shindanResult_name">(.*?)</span>                </span>').findall(r.text)[0])
    y = re.sub(r"</span>", "", e)
    text = re.sub(r"<br />", "\n", y)
    return text
