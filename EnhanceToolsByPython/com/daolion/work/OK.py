# -*- coding:utf-8 -*-
# **********************************
# ** http://weibo.com/lixiaodaoaaa #
# ** create at 2018/1/5   17:20 ***
# ****** by:lixiaodaoaaa ***********


# -*- coding:utf-8 -*-
# **********************************
# ** http://weibo.com/lixiaodaoaaa #
# ** create at 2018/1/5   16:52 ***
# ****** by:lixiaodaoaaa ***********


import sys
import os
import subprocess
import json
import types

p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
retcode = p.wait()
data = p.stdout.read()
myJson = json.loads(str(data))
newJson = json.dumps(myJson, ensure_ascii=False)

p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
retcode = p.wait()
p.stdout.write(data)
