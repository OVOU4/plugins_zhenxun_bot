#  Package acgimage 随机图片
from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from utils.message_builder import image
from services.log import logger
import random
from utils.manager import withdraw_message_manager
from configs.config import Config


__zx_plugin_name__ = "随机图片"
__plugin_usage__ = """
usage：
    随机图片
    指令: 
	随机图片
	直接随机(无r18检测，务必小心，非常危险)
""".strip()
__plugin_des__ = "随机图片"
__plugin_cmd__ = ["随机图片", "直接随机"]
__plugin_type__ = ("来点好康的",)
__plugin_version__ = 0.1
__plugin_author__ = "ZeroBot-Plugin"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["随机图片"],
}

__plugin_configs__ = {
    "WITHDRAW_随机图片_MESSAGE": {
        "value": (0, 2),
        "help": "自动撤回，参1：延迟撤回色图时间(秒)，0 为关闭 | 参2：监控聊天类型，0(私聊) 1(群聊) 2(群聊+私聊)",
        "default_value": (0, 2),
    },
}

suiji = on_command("随机图片", aliases={"随机图片"}, priority=5, block=True)

#suijir18 = on_command(
#    "直接随机图片", aliases={"直接随机图片"}, priority=5, block=True
#)

#url = 'https://sayuri.fumiama.top/dice/?class=1&loli=true'
url1 = 'https://img.xjh.me/random_img.php'
url2 = 'https://api.btstu.cn/sjbz/api.php?lx=dongman&format=images'
url3 = 'https://api.yimian.xyz/img?type=moe'
url4 = 'https://api.yimian.xyz/img?type=moe&size=1920x1080'
url5 = 'https://img.xjh.me/random_img.php?return=302'
url6 = 'https://t.lizi.moe/pc'
url7 = 'https://img.paulzzh.com/touhou/random'
#urlr18 = 'https://sayuri.fumiama.top/dice/?class=1&loli=true&r18=ture'
foo = [url2, url1, url3, url4, url6, url5, url7]


# 随机图片
@suiji.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        await bot.send(event=event, message="少女祈祷中....")
        msg_id = await suiji.send(image(random.choice(foo)))
        withdraw_message_manager.withdraw_message(
                event,
                msg_id["message_id"],
                Config.get_config("suiji", "WITHDRAW_随机图片_MESSAGE"),
            )
    except Exception as e:
        await suiji.send("你冲得太多了，休息一下吧！")
        logger.error(f"随机图片 发送了未知错误 {type(e)}：{e}")


# 直接随机图片(含R18)
#@suijir18.handle()
#async def _(bot: Bot, event: MessageEvent, state: T_State):
#    try:
#        await bot.send(event=event, message="少女祈祷中....")
#        await suijir18.send(image(urlr18))
#    except Exception as e:
#        await suijir18.finish("你冲得太多了，休息一下吧！")
#        logger.error(f"直接随机图片 发送了未知错误 {type(e)}：{e}")

# 设置随机图片网址
# @shezhisuiji.handle()
# async def _(bot: Bot, event: MessageEvent, state: T_State):
#    try:
#        args = str(event.get_message()).strip()
#        if args:
#            state["words"] = args
#        url = state["words"]
#        global url
#    except Exception as e:
#        await suijir18.finish("你冲得太多了，休息一下吧！")
#        logger.error(f"直接随机图片 发送了未知错误 {type(e)}：{e}")


# 撤回图片
# @taisele.handle()
# async def _(bot: Bot, event: MessageEvent, state: T_State):
#    try:
#        withdraw_message_manager.withdraw_message(
#            event,
#            msg_id["message_id"])
#    except Exception as e:
#        await suijir18.finish("你冲得太多了，休息一下吧！")
#        logger.error(f"随机图片 发送了未知错误 {type(e)}：{e}")
