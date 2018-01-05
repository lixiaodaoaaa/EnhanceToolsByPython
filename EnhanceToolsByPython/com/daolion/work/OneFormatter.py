# -*- coding:utf-8 -*-
# **********************************
# ** http://weibo.com/lixiaodaoaaa #
# ** create at 2018/1/5   16:52 ***
# ****** by:lixiaodaoaaa ***********


import sys
import os
import subprocess
import json
import pyperclip
import types


def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    # 这里的data为bytes类型，之后需要转成utf-8操作
    return data


def changeClipStrToGBKChars(data):
    myJson = json.loads(str(data, encoding="utf-8"))
    newJson = json.dumps(myJson, ensure_ascii=False)
    return newJson


def setToClipboard(str):
    pyperclip.copy(str)





if __name__ == '__main__':
    # clipBoardData = getClipboardData()
    # newData = changeClipStrToGBKChars(clipBoardData)
    # setToClipboard(newData)
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    myJson = json.loads(str(data, encoding="utf-8"))
    newJson = json.dumps(myJson, ensure_ascii=False)
    pyperclip.copy(str)
