# -*- coding:utf-8 -*-
# **********************************
# ** http://weibo.com/lixiaodaoaaa #
# ** create at 2017/12/29   11:38 ***
# ****** by:lixiaodaoaaa ***********
# !/usr/bin/env bash
# webHeader="http://"
# ipLine=$(ifconfig en0   | grep   "inet" | grep "broadcast" | grep "10")
# deleteRightIpLine=${ipLine% n*}
# ipResult=${deleteRightIpLine#* }
# fullWebAddress=${webHeader}${ipResult}/apk/
#                             echo ${fullWebAddress}  | pbcopy
# echo ${fullWebAddress}
# open ${fullWebAddress}


import sys
import os
import subprocess
import json
import pyperclip
import types





# 将clipboard中有 "\u552e\u8d27\u673a\u76d1\u63a7\u4fe1\u606f\u683c\u5f0f\u6709\u8bef"
# 转化为中文
def changeClipStrToGBKChars(data):

    myJson = json.loads(str(data, encoding = "utf-8"))
    newJson = json.dumps(myJson, ensure_ascii=False)
    return  newJson





