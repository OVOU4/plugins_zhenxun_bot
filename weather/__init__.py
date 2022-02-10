from nonebot import on_regex
from .data_source import weatherx ,weatherweb
from nonebot.adapters.cqhttp import Bot, MessageEvent, GroupMessageEvent
from jieba import posseg
from services.log import logger
from nonebot.typing import T_State
import re
from utils.utils import get_message_text


__zx_plugin_name__ = "天气查询"
__plugin_usage__ = """
usage：
    普普通通的查天气吧
    指令：
        [城市]天气/天气[城市]
""".strip()
__plugin_des__ = "出门要看看天气，不要忘了带伞"
__plugin_cmd__ = ["[城市]天气/天气[城市]"]
__plugin_type__ = ("一些工具",)
__plugin_version__ = 0.1
__plugin_author__ = "HibiKier"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["查询天气", "天气", "天气查询", "查天气"],
}


weather = on_regex(r".{0,10}市?的?天气.{0,10}", priority=5, block=True)

@weather.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    msg = get_message_text(event.json())
    msg1 = re.search(r".*?(.*)市?的?天气.*?", msg)
    msg2 = re.search(r".*?天气(.*).*?", msg)
    msg1 = msg1.group(1)
    msg2 = msg2.group(1)
    msg = msg1 if msg1 else msg2
    #if msg[-1] == "的":
    #    msg = msg[:-1]
    #if msg[-1] != "市":
    #    msg += "市"
    city = ""
    if msg:
        for word in posseg.lcut(msg):
            city = str(word.word).strip()
            break
        if word.word == "火星":
            await weather.finish(
                "没想到你个小呆子还真的想看火星天气！\n火星大气中含有95％的二氧化碳,气压低，加之极度的干燥，"
                "就阻止了水的形成积聚。这意味着火星几乎没有云,冰层覆盖了火星的两极，它们的融化和冻结受到火星与太"
                "阳远近距离的影响,它产生了强大的尘埃云，阻挡了太阳光，使冰层的融化慢下来。\n所以说火星天气太恶劣了，"
                "去过一次就不想再去第二次了"
            )
    try:
        city_weather_url = await weatherx(city)
        city_weather = await weatherweb(city_weather_url)
        await weather.send(city_weather)
        logger.info(
            f'(USER {event.user_id}, GROUP {event.group_id if isinstance(event, GroupMessageEvent) else "private"} ) '
            f"查询天气:" + city
        )
    except Exception:  # 错误抛出(可能无法查询到城市)
        await weather.finish("没查到！！试试查查火星天气？")
