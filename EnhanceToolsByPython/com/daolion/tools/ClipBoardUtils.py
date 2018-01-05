# -*- coding:utf-8 -*-
# **********************************
# ** http://weibo.com/lixiaodaoaaa #
# ** create at 2017/12/29   16:33 ***
# ****** by:lixiaodaoaaa ***********

import pyperclip

import sys
import os
import subprocess
import json
import pyperclip
import types


def setToClipboard(str):
    pyperclip.copy(str)



def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    # 这里的data为bytes类型，之后需要转成utf-8操作
    return data


def getClipBoard():
    myClipboard = pyperclip.paste
    print(myClipboard)
