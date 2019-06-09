
#-*- coding=utf-8 -*-
"""
知乎图片下载器
"""
import requests
import re
import json
import time
# from PIL import Image
# import cStringIO
# import cookielib
import urllib
import os

api_url='https://www.zhihu.com/node/QuestionAnswerListV2'
login_url='https://www.zhihu.com/login/'
topic_url='https://www.zhihu.com/question/'


headers={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

print("project pachong001")



