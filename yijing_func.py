# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def ConvertCN(s):
    return s.encode('gb18030')


bugua_map = {   }



def read_bagua(file):
    f = open(file)
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
    f.close()

read_bagua(r"/Users/macpro/git_work/code/iching/buagua.txt")
