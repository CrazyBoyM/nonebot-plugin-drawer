# nonebot-plugin-drawer
基于文心大模型的AI机器人画画插件。


### 前提: nonebot2的部署
这里推荐两篇机器人部署教程  
1.https://blog.csdn.net/weixin_47113651/article/details/121353191  
2.https://zhuanlan.zhihu.com/p/371264976
### 通过nb-cli安装（推荐）
```
nb plugin install nonebot-plugin-drawer
```
### 通过pip安装
```
1.pip install nonebot-plugin-drawer 进行安装  
2.在bot.py添加nonebot.load_plugin('nonebot_plugin_drawer')
```
### 配置env.*
请在env.*配置文件中加入如下两行
```
wenxin_ak = "xxxxxxxxxxxxxxxx"
wenxin_sk = "xxxxxxxxxxxxxxxx"
wenxin_cd_time = 300 # 技能冷却时间，以秒为单位
wenxin_image_count = 3 # 画画的图片数量
wenxin_manager_list = ["123456789", "98765432"] # 管理员列表(不触发冷却时间限制)
```
文心的ak和sk申请链接：https://wenxin.baidu.com/younger/apiDetail?id=20008
### 使用方法（仅支持群聊）
触发菜单命令：画画帮助
当前支持油画、水彩画、卡通画、粉笔画、儿童画、蜡笔画, 主要擅长风景写意画，请尽量给定比较明确的意象  
如：油画 江上落日与晚霞

![3a83453d5d28d1eedf0a0ddb5c90d29](https://user-images.githubusercontent.com/35400185/185073989-d4cd1118-cddb-4588-a210-b6d001a049f1.jpg)  
油画 江上落日与晚霞  

![8887badee1c74c8488b613e4ceb83c2](https://user-images.githubusercontent.com/35400185/185074011-49b7bad1-e7d3-4385-afd5-a82163b0eebc.jpg)  
油画 思乡
