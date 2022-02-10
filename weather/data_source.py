import httpx
import re
import psutil
import os
import asyncio

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
}


async def weatherx(city: str) -> str:
    """
    获取城市天气网址
    :param city: 城市
    """
    url = 'https://www.tianqi.com/tianqi/ctiy?keyword=' + city
    result = httpx.get(url, headers=header)
    try:
        a = str(re.compile(r'url":"(.*?)/"}').findall(result.text)[0])
        b = re.sub(r'\\', '', a)  # 获取查询城市的地址
    except Exception:  # 错误抛出(可能无法查询到城市)
        b = '没查到！！试试查查火星天气？'
        print(b)
    return b


async def weatherweb(url: str) -> str:
    """
    获取城市天气数据
    :param url: 城市网址地址
    """
    # 获取城市天气页面
    city_weather_web = httpx.get(url, headers=header).text
    try:
        c = str(re.compile(r'/chinacity.html" title="(.*?)">').findall(city_weather_web)[1])  # 获取标题(查询为一个城市时，例如柳州市)
    except IndexError:
        c = str(re.compile(r'<dd class="name"><h2>(.*?)</h2><i><a href="/chinacity.html">').findall(city_weather_web)[
                    0]) + '天气'  # 获取标题(查询为一个城市的某块区域，例如柳北区)
    except Exception:
        c = '当前城市天气'
    d = str(re.compile(r'<dd class="week">(.*?) </dd>').findall(city_weather_web)[0])  # 获取时间

    # 获取当前气温
    e = str(re.compile(r'<p class="now"><b>(.*?)</i></p>').findall(city_weather_web)[0])
    i = '当前气温:' + re.sub(r'</b><i>', '', e)

    # 获取今天天气情况和温度
    f = str(re.compile(r'<span><b>(.*?)</span>').findall(city_weather_web)[0])
    j = '今日' + re.sub(r'</b>', ' 气温:', f)

    # 获取今天湿度和风力
    g = str(re.compile(r'<dd class="shidu"><b>(.*?)</b></dd>').findall(city_weather_web)[0])
    k = re.sub(r'</b><b>', ' ', g)

    # 获取今日空气质量与日出情况
    h = str(re.compile(r'<dd class="kongqi" ><h5 style="background-color:#79b800;">(.*?)</span></dd>').findall(
        city_weather_web)[0])
    l = re.sub(r'</h5><h6>|</h6><span>|<br />', ' ', h)

    # 获取未来天气情况(城市未来6小时天气)(过于耗时暂不加入)
    #    try:
    #        m = str(re.compile(r'<li class="w95">(.*?)</li>').findall(city_weather_web)) # 获取城市未来天气状态,和风向
    #        n = str(re.compile(r'<li class="w95"><span>(.*?)</span></li>').findall(city_weather_web))  # 获取城市未来气温
    #        o = str(re.compile(r'<li class="w95 mgtop5">(.*?)</li>').findall(city_weather_web))  # 获取城市未来风力
    #        p = str(re.compile(r'<li class="w95">(.*?)</li>').findall(city_weather_web)) # 获取城市未来时间
    #    except:
    #        m=0
    #        n=0
    #        o=0
    #        p=0
    #        pass
    x = c + "\n" + d + "\n" + i + "\n" + j + "\n" + k + "\n" + l
    # print(u'当前进程的内存使用：%.4f GB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024 / 1024))
    # print(city_weather_web)
    return x


if __name__ == "__main__":
    url = weatherx(city)
    weatherweb(url)
