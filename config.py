# Copyright ©️ 2023 Sanila Ranatunga. All Rights Reserved

import os


class Config(object):
    API_ID = int(os.environ.get("apiid"))
    API_HASH = os.environ.get("apihash")
    BOT_TOKEN = os.environ.get("tk")
