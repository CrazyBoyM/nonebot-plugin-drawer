# nonebot-plugin-drawer
基于文心大模型的AI机器人画画插件。


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
cd_time = 120 # 技能冷却时间，以秒为单位
```
文心的ak和sk申请链接：https://wenxin.baidu.com/younger/apiDetail?id=20008
### 使用方法
当前支持 "油画", "水彩画", "中国画", 主要擅长风景写意画，请尽量给定比较明确的意象  
如：油画 江上落日与晚霞

![3a83453d5d28d1eedf0a0ddb5c90d29](https://user-images.githubusercontent.com/35400185/185073989-d4cd1118-cddb-4588-a210-b6d001a049f1.jpg)![8887badee1c74c8488b613e4ceb83c2](https://user-images.githubusercontent.com/35400185/185074011-49b7bad1-e7d3-4385-afd5-a82163b0eebc.jpg)
