import asyncio
from pydoc import describe
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.params import Arg, CommandArg, ArgPlainText, RawCommand
from .drawer import get_token, get_taskId, get_img

drawer = on_command("画画", aliases={"绘画", "油画", "水彩画", "中国画"}, priority=5)


@drawer.handle()
async def handle_first_receive(matcher: Matcher, command = RawCommand(), args = CommandArg()):
    print("#############")
    print(command) # 匹配结果
    print(args)
    print("##############")
    if command != '画画':
        style = command
        text = args
        await matcher.send(f'开始创作主题为{text}的{style}(预计两分钟)')
        access_token = await get_token()
        print(access_token)
        taskId = await get_taskId(access_token, text, style)
        print(taskId)
        await asyncio.sleep(60) # sleep
        images = await get_img(access_token, taskId)
        print(images)
        msg = Message(f'原创绘画：主题为{text}的{style}') \
                + MessageSegment.image(images[0]['image']) \
                + MessageSegment.image(images[1]['image']) \
                + MessageSegment.image(images[2]['image']) 
        print("#################")
        print(msg)
        print("#################")
        await matcher.finish(msg)
        
    else:
        await matcher.finish('当前支持 "油画", "水彩画", "中国画", 主要擅长风景写意画，请尽量给定比较明确的意象，如：油画 江上落日与晚霞')