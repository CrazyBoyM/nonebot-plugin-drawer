import asyncio
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.params import Arg, CommandArg, ArgPlainText, RawCommand
from .drawer import get_token, get_taskId, get_img

drawer = on_command("画画", aliases={'油画', '水彩画', '卡通画', '粉笔画', '儿童画', '蜡笔画'}, priority=5)


@drawer.handle()
async def handle_first_receive(matcher: Matcher, command = RawCommand(), args = CommandArg()):
    print("#############")
    print(command) # 匹配结果
    print(args)
    print("##############")
    if  command == '画画': 
        help_msg = '当前支持油画、水彩画、卡通画、粉笔画、儿童画、蜡笔画\n主要擅长风景写意画，请尽量给定比较明确的意象\n如：油画 江上落日与晚霞'
        await matcher.finish(help_msg)
        
    else:
        style = '油画' # 绘画时style默认为油画
        style_list = ['油画', '水彩画', '卡通画', '粉笔画', '儿童画', '蜡笔画']
        for keyword in style_list:
            if keyword in command:
                style = keyword
                break  
        text = args
        await matcher.send(f'AI开始绘制主题为{text}的{style}(预计两~五分钟)...')
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
                + MessageSegment.image(images[3]['image']) \
                + MessageSegment.image(images[6]['image']) \
                + MessageSegment.image(images[9]['image']) 
        print("#################")
        print(msg)
        print("#################")
        await matcher.finish(msg)