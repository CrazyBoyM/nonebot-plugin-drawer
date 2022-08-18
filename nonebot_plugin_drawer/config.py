import nonebot
from pydantic import BaseSettings


class Config(BaseSettings):
    wenxin_ak: str = ""  # 文心大模型的ak
    wenxin_sk: str = ""  # 文心大模型的sk
    wenxin_cd_time: int = 60  # cd时间，单位秒
    wenxin_image_count: int = 3  # 画画的图片数量
    wenxin_manager_list: list = []  # 文心大模型的管理员列表（不受冷却时间限制）
    class Config:
        extra = "ignore"


global_config = nonebot.get_driver().config
wenxin_config = Config(**global_config.dict())  # 载入配置
