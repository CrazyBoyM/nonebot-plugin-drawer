# nonebot-plugin-drawer
基于文心大模型的AI机器人画画插件。


### 通过nb-cli安装（推荐）
nb plugin install nonebot-plugin-drawer
### 通过pip安装
1.pip install nonebot-plugin-drawer 进行安装  
2.在bot.py添加nonebot.load_plugin('nonebot-plugin-drawer')
### 配置env.*
请在env.*配置文件中加入如下两行
```
wenxin_ak = "xxxxxxxxxxxxxxxx"
wenxin_sk = "xxxxxxxxxxxxxxxx"
```
文心的ak和sk申请链接：https://wenxin.baidu.com/younger/apiDetail?id=20008
### 使用方法
当前支持 "油画", "水彩画", "中国画", 主要擅长风景写意画，请尽量给定比较明确的意象  
如：油画 江上落日与晚霞

![51addc86ce22c5ff99a12b36cd5834c](https://user-images.githubusercontent.com/35400185/184457437-e22e3f84-69bd-467b-b158-2e3dccce00c1.jpg)

![3a83453d5d28d1eedf0a0ddb5c90d29](https://user-images.githubusercontent.com/35400185/184457906-4c1c656f-d125-49c6-8923-f5cfc2898d87.jpg)
