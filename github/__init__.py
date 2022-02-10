from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import (
    Bot,
    MessageEvent,
)
import httpx

__zx_plugin_name__ = "github仓库查询"
__plugin_usage__ = """
usage：
    快速查询github项目并返回start第一个
    指令:
    >github [项目名称]
""".strip()
__plugin_des__ = "基于github API仓库查询"
__plugin_cmd__ = [">github"]
__plugin_type__ = ("一些工具",)
__plugin_version__ = 0.1
__plugin_author__ = "ZeroBot-Plugin"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": [">github"],
}

github = on_command(">github", aliases={">github"}, priority=5, block=True)

url = 'https://api.github.com/search/repositories'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34'

}

@github.handle()
async def _h(bot: Bot, event: MessageEvent, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["words"] = args


@github.got("words", prompt="想查询什么呢?")
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        await bot.send(event=event, message="小真寻正在搜素仓库......")
        key_words = state["words"]
        params = ({
            'q': key_words,
        })
        response = httpx.get(url, headers=header, params=params)
        # 获取页面源码
        urls = response.json().get('items')[0]
        # 获取项目介绍和url
        dizhi = '项目地址：' + urls.get('html_url')
        mingcheng = urls.get('description')
        print("小真寻真正搜素仓库")
        await github.send(mingcheng + "\n" + dizhi)
    except Exception:
        await github.finish("小真寻暂时查不到哦~")
