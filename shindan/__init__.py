from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import (
    Bot,
    MessageEvent,
)
from .data_source import jintian, yishijie, maimeng, laopo, huoqu
from utils.message_builder import image

__zx_plugin_name__ = "shindan"
__plugin_usage__ = """
usage：
    来测测你是什么样的人
    指令:
        今天是什么少女[@xxx]
        异世界转生[@xxx]
        卖萌[@xxx]
        抽老婆[@xxx]
""".strip()
__plugin_des__ = "基于 https://shindanmaker.com 的测定小功能"
__plugin_cmd__ = ["今天是什么少女", "异世界转生", "卖萌", "抽老婆"]
__plugin_type__ = ("群内小游戏",)
__plugin_version__ = 0.1
__plugin_author__ = "ZeroBot-Plugin"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["今天是什么少女", "异世界转生", "卖萌", "抽老婆"],
}

yishi = on_command(
    "异世界转生", aliases={"异世界转生"}, priority=5, block=True
)

jin = on_command(
    "今天是什么少女", aliases={"今天是什么少女"}, priority=5, block=True
)

mai = on_command(
    "卖萌", aliases={"卖萌"}, priority=5, block=True
)

chou = on_command(
    "抽老婆", aliases={"抽老婆"}, priority=5, block=True
)


# 异世界转生
@yishi.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        result = await yishijie(event.sender.nickname)
        await yishi.send(result)
    except Exception:
        await huoqu()
        await yishi.finish("小真寻无法为你转生哦~")


# 今天是什么少女
@jin.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        result = await jintian(event.sender.nickname)
        await jin.send(result)
    except Exception:
        await huoqu()
        await jin.finish("小真寻暂时不知道你是什么少女哦~")


# 卖萌
@mai.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        result = await maimeng(event.sender.nickname)
        await mai.send(result)
    except Exception:
        await huoqu()
        await mai.finish("小真寻卖不了萌呢~")


# 抽老婆
@chou.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        x = await laopo(event.sender.nickname)
        result = x[0]
        url = x[1]
        lao = x[2]
        result += image(url)
        result += lao
        await chou.send(result)
    except Exception:
        await huoqu()
        await yishi.finish("小真寻暂时查不到哦~")
