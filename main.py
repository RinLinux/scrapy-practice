# encoding: utf-8

"""
time: 2019/03/16/01/36
function: 用来启动爬虫项目
"""

from scrapy.cmdline import execute
import sys
import os

print(os.path.dirname(os.path.abspath("__file__")))
sys.path.append(os.path.dirname(os.path.abspath("__file__")))
# execute(['scrapy', 'crawl', ''])
