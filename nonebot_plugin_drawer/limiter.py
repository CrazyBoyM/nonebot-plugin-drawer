# 引用自https://github.com/Ice-Cirno/HoshinoBot
from collections import defaultdict
import time
from .config import wenxin_config

class FreqLimiter:
    def __init__(self, default_cd_seconds):
        self.next_time = defaultdict(float)
        self.default_cd = default_cd_seconds

    def check(self, key) -> bool:
        return bool(time.time() >= self.next_time[key])

    def start_cd(self, key, cd_time=0):
        self.next_time[key] = time.time() + (cd_time if cd_time > 0 else self.default_cd)

    def left_time(self, key) -> float:
        return self.next_time[key] - time.time()

cd_time = wenxin_config.wenxin_cd_time
limiter = FreqLimiter(cd_time)