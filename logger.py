# 日志记录模块

import logging
from logging import handlers
import os


# 日志名
LOG_FILE_NAME = "log"

# 日志格式
LOG_FORMAT = logging.Formatter("%(levelname)s %(asctime)s %(filename)s %(lineno)d %(message)s")

# 日志级别
LOG_LEVEL = logging.DEBUG

# 创建日志器
logger = logging.getLogger("main")
logger.setLevel(LOG_LEVEL)

# 创建处理器
sh = logging.StreamHandler()
sh.setFormatter(LOG_FORMAT)

# 创建文件处理器
if not os.path.exists("./logs"):
    os.makedirs("./logs")
th = handlers.TimedRotatingFileHandler(filename=f"./logs/{LOG_FILE_NAME}.log", when="D", encoding="utf-8")
th.setFormatter(LOG_FORMAT)

# 添加处理器
logger.addHandler(sh)
logger.addHandler(th)
