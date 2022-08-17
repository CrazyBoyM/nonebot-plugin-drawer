import nonebot
from pydantic import BaseSettings


class Config(BaseSettings):
    wenxin_ak: str = ""  # 文心大模型的ak
    wenxin_sk: str = ""  # 文心大模型的sk
    cd_time: int = 60  # cd时间，单位秒
    
    class Config:
        extra = "ignore"


global_config = nonebot.get_driver().config
wenxin_config = Config(**global_config.dict())  # 载入配置
