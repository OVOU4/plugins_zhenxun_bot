from .lunar_python import Lunar
from datetime import datetime
import re
from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
# 基于lunar项目的黄历演算
# github项目地址：https://github.com/6tail/lunar-python
# gitee项目地址：https://gitee.com/6tail/lunar-python
# 官方API文档地址：http://6tail.cn/calendar/api.html#overview.html

__zx_plugin_name__ = "每日老黄历"
__plugin_usage__ = """
usage：
    出门前肯定要看看今日的老黄历啦
    指令:
    老黄历
""".strip()
__plugin_des__ = "基于lunar项目的黄历演算"
__plugin_cmd__ = ["老黄历"]
__plugin_type__ = ("一些工具",)
__plugin_version__ = 0.1
__plugin_author__ = "6tail"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["老黄历"],
}

laohuangli = on_command("老黄历", aliases={"老黄历"}, priority=5, block=True)


async def huang():
    huangli = ''
    ji = '吉神宜趋：'
    xiong = '凶煞宜忌：'
    time = datetime.now()
    lunar = Lunar.fromDate(time)
    a = lunar.toFullString()  # 黄历
    b = lunar.getSolar().toFullString()  # 星期星座
    # 吉神凶煞
    # 吉神宜趋
    x = lunar.getDayJiShen()
    for s in x:
        ji += s + ' '
    # 凶煞宜忌
    y = lunar.getDayXiongSha()
    for s in y:
        xiong += s + ' '
    c = re.split(' ', a)
    # 黄历构建
    huangli += b + '\n'  # 当前时间
    huangli += c[0] + ' ' + c[9] + '\n'  # 日期
    huangli += c[1] + ' ' + c[2] + ' ' + c[3] + ' ' + c[4] + '\n'  # 阴历
    huangli += "五行：" + c[5] + ' ' + c[6] + ' ' + c[7] + ' ' + c[8] + '\n'  # 五行
    huangli += '冲煞：' + c[11] + ' ' + c[10] + '\n'  # 冲煞
    huangli += c[12] + ',' + c[13] + '\n'  # 彭祖
    huangli += c[15] + ' ' + c[16] + '\n' + c[14] + ' ' + c[17] + ' ' + c[18] + '\n'  # 神位
    huangli += ji + '\n'
    huangli += xiong
    # print(b)
    # print(xiong)
    # print(x.toFullString())
    return huangli


@laohuangli.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    try:
        await bot.send(event=event, message="小真寻正在翻阅老黄历......")
        result = await huang()
        await laohuangli.send(result)
    except Exception:
        await laohuangli.finish("小真寻查不到今日老黄历呢QAQ")


if __name__ == "__main__":
    laohuangli()
