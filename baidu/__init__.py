# coding=utf-8
from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message
from nonebot.params import CommandArg
from configs.config import NICKNAME, Config
import httpx
import re

__zx_plugin_name__ = "百度"
__plugin_usage__ = """
usage：
    普普通通的百度百科
    *为懒癌设计*
    指令：
        百度 [词条]
""".strip()
__plugin_des__ = "普普通通的在线百度"
__plugin_cmd__ = ["百度 [词条]"]
__plugin_type__ = ("一些工具",)
__plugin_version__ = 0.1
__plugin_author__ = "yangyangjiejie"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["百度", "百度百科"],
}

baidu = on_command("百度", aliases={"百度百科"}, priority=5, block=True)


@baidu.handle()
async def _(state: T_State, arg: Message = CommandArg()):
    args = arg.extract_plain_text().strip()
    if args:
        state["words"] = args


@baidu.got("words", prompt="想百度什么呢?")
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        await bot.send(event=event, message=f"{NICKNAME}正在搜素......")
        key_words = state["words"]
        url = f'https://baike.baidu.com/item/{key_words}'
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'
        }
        html = httpx.get(url, headers=header, follow_redirects=True)  # 跟踪重定向
        text = str(re.compile(r'<meta name="description" content="(.*?)">').findall(html.text)[0])  # 正则匹配第一段话
        result = text + "\n" + f'词条来源百度百科:{html.url}'
        await baidu.send(result)
    except Exception:
        await baidu.finish(f"{NICKNAME}暂时查不到哦~")
