import asyncio
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Message, MessageSegment
from nonebot.params import Arg, CommandArg, ArgPlainText, RawCommand
from .drawer import get_token, get_taskId, get_img
from .limiter import limiter

drawer = on_command("画画", aliases={'油画', '水彩画', '卡通画', '粉笔画', '儿童画', '蜡笔画'}, priority=5)

@drawer.handle()
async def _(matcher: Matcher, event: GroupMessageEvent, command = RawCommand(), args = CommandArg()):
    if  command == '画画': 
        help_msg = '当前支持油画、水彩画、卡通画、粉笔画、儿童画、蜡笔画\n主要擅长风景写意画，请尽量给定比较明确的意象\n如：油画 江上落日与晚霞'
        await matcher.finish(help_msg)
    else:
        # 判断用户是否在限制时间内频繁触发
        user_id = event.user_id
        if not limiter.check(user_id):
            left_time = limiter.left_time(user_id)
            await drawer.finish(f'咦，人类，你需要等待{left_time}秒再找俺画画！')
        # 开始启动画画任务
        limiter.start_cd(event.user_id)
        command_str = str(command)
        style = '油画' # 绘画时style默认为油画
        style_list = ['油画', '水彩', '卡通', '粉笔画', '儿童画', '蜡笔画']
        for keyword in style_list:
            if keyword in command_str:
                style = keyword
                break  
        text = args # 绘画的任务描述文字
        await matcher.send(f'文心AI开始绘制主题为{text}的{style}(预计两~五分钟)...')
        try:
            access_token = await get_token()
            taskId = await get_taskId(access_token, text, style)
            await asyncio.sleep(70) # 模型画画大概要70秒，等待一会儿
            images = await get_img(access_token, taskId)
            msg = Message(f'文心原创绘画：主题为{text}的{style}') \
                    + MessageSegment.image(images[0]['image']) \
                    + MessageSegment.image(images[1]['image']) \
                    + MessageSegment.image(images[3]['image']) \
                    + MessageSegment.image(images[6]['image']) \
                    + MessageSegment.image(images[9]['image']) 
            await matcher.finish(msg)
        except Exception as e:
            print(e)