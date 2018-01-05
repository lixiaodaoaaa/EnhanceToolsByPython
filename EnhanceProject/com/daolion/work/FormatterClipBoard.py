# -*- coding:utf-8 -*-
# **********************************
# ** http://weibo.com/lixiaodaoaaa #
# ** create at 2018/1/4   14:27 ***
# ****** by:lixiaodaoaaa ***********

import com.daolion.tools.FormmaterUtils as FormmaterUtils
import com.daolion.tools.ClipBoardUtils as ClipBoardUtils

if __name__ == '__main__':
    clipData = ClipBoardUtils.getClipboardData()
    newData = FormmaterUtils.changeClipStrToGBKChars(clipData)
    ClipBoardUtils.setToClipboard(newData)
