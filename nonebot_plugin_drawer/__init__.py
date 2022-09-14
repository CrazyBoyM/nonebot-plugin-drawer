import asyncio
from multiprocessing import managers
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Message, MessageSegment
from nonebot.params import CommandArg, RawCommand
from .drawer import get_token, get_taskId, get_img
from .limiter import limiter
from .config import wenxin_config

drawer = on_command("画画", aliases={'画画帮助', '油画', '水彩画', '卡通画', '粉笔画', '儿童画', '蜡笔画'}, priority=5)

@drawer.handle()
async def _(matcher: Matcher, event: GroupMessageEvent, command = RawCommand(), args = CommandArg()):
    # 判断是否触发帮助 或 绘画主题任务描述为空
    if  command == '画画帮助' or str(args).strip() == '': 
        help_msg = '当前支持油画、水彩画、卡通画、粉笔画、儿童画、蜡笔画\n主要擅长风景写意画,请尽量给定“比较明确的意象”\n如: 油画 江上落日与晚霞'
        await matcher.finish(help_msg)
        return
    
    # 判断用户是否触发频率限制
    user_id = event.user_id
    managers = wenxin_config.wenxin_manager_list # 管理员列表(不触发冷却时间限制)
    if not limiter.check(user_id):
        left_time = limiter.left_time(user_id)
        await matcher.finish(f'咦，人类，你刚画了一次唉。需要等待{left_time}秒再找俺画画！冷却期间可临时到网页（https://wenxin.baidu.com/moduleApi/ernieVilg?from=baicai）进行体验哦')
        return 
    
    # 启动画画任务
    command_str = str(command)
    style = '油画' # 绘画时style默认为油画
    style_list = ['油画', '水彩', '卡通', '粉笔画', '儿童画', '蜡笔画']
    for keyword in style_list:
        if keyword in command_str:
            style = keyword
            break  
    text = args # 绘画的任务描述文字
    await matcher.send(f'飞桨文心AI开始绘制主题为“{text}”的{style}(预计2-5分钟)...')
    
    try:
        access_token = await get_token()
        taskId = await get_taskId(access_token, text, style)
        if taskId == None:
            await matcher.finish(f'主题“{text}”违规，请重新给定任务描述')
            return      
        
        if not str(user_id) in managers: 
            limiter.start_cd(user_id) # 启动冷却时间限制
        await asyncio.sleep(30) # 模型画画大概要30秒，等待一会儿
        images = await get_img(access_token, taskId)
        if images == None:
            await matcher.finish(f'无法绘制主题为“{text}”的{style}!')
            return
        
        image_count = wenxin_config.wenxin_image_count # 每次发送的图片数量
        # 判断图片数量是否少于配置的图片数量
        if len(images) < image_count:
            image_count = len(images)
            
        msg = Message(f'文心原创绘画：主题为“{text}”的{style}') 
        for i in range(image_count): 
            msg += MessageSegment.image(images[i]['image'])
        await matcher.finish(msg)
        
    except Exception as e:
        print(e)