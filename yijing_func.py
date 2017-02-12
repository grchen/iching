# -*- coding:utf-8 -*-
import sys,collections
reload(sys)
sys.setdefaultencoding('utf-8')

gua_8_map = collections.OrderedDict()
gua_64_map = collections.OrderedDict()
gua_64_all_map = collections.OrderedDict()
gua_yilin_map = collections.OrderedDict()
# 乾:{""}
gua_index = ["彖曰","初九","初六","九二","六二","九三","六三","九四","六四","九五","六五","上九","上六","用六","用九",]

def dump_dict(dict):
    import json;
    return json.dumps(dict,indent=1);

def get_bi_str(index,base=6):
    count = 64
    if base <> 6:
        count = 8
        base = 3

    result = ""
    theindex = index % count
    value = bin(theindex).replace("0b","00")
    length = len(value)

    if length < base:
        for x in range(base - length):
            result = result + "0"
        result = result + value
    else:
        result = value[length-base:length]
    return result

def get_up_gua(gua_str):
    return gua_str[0:3]

def get_down_gua(gua_str):
    return gua_str[3:6]

def print_gua_8():
    for (k,v) in gua_8_map.items():
        print k, v[0],v[1],v[2],v[3]

def print_gua_64():
    for (k,v) in gua_64_map.items():
        print k, v[0],v[1],v[2],v[3]

def read_gua_8(file):
    f = open(file)
    line = f.readline()

    while line:
        line = line.rstrip().lstrip().split(",")
        gua_8_map[line[0].rstrip().lstrip()] = [line[1].rstrip().lstrip(),line[2].rstrip().lstrip(),line[3].rstrip().lstrip(),line[4].rstrip().lstrip()]
        line = f.readline()
    f.close()

    #print_gua_8()

def read_gua_64(file):
    f = open(file)
    line = f.readline()

    while line:
        line = line.rstrip().lstrip().split(",")
        gua_64_map[line[0].rstrip().lstrip()] = [line[1].rstrip().lstrip(),line[2].rstrip().lstrip(),line[3].rstrip().lstrip(),line[4].rstrip().lstrip()]
        line = f.readline()
    f.close()

    #print_gua_64()

def read_gua_all(file):
    f = open(file)
    line = f.readline()
    while line:
        line = line.rstrip().lstrip()
        if "第" in line and '卦' in line:
            read_one_gua(line, f)
        line = f.readline()
    f.close()

    #print_gua_all()


def read_wenyan(gua_name, line, file):
    while line:
        line = line.rstrip().lstrip()
        if line <> "":
            gua_64_all_map[gua_name]["文言曰"].append(line)
        line = file.readline()
        if "第" in line and '卦' in line:
            read_one_gua(line, file)
            break

def read_one_gua(line, file):
    old_line = line.rstrip().lstrip()
    line = line.split(" ")
    gua_name = line[1].rstrip().lstrip()
    gua_64_all_map[gua_name] = {}
    gua_64_all_map[gua_name][gua_name] = old_line

    line = file.readline()


    while line:
        line = line.rstrip().lstrip()

        gua_name_str = gua_name + "："

        if gua_name_str in line:
            if not gua_64_all_map[gua_name].has_key("卦辞"):
                gua_64_all_map[gua_name]["卦辞"] = line

        if "象曰：" in line:
            is_xiangyue = True
            for x in gua_index:
                if x+"：" in line:
                    is_xiangyue = False
            if is_xiangyue:
                gua_64_all_map[gua_name]["象曰"] = line

        for x in gua_index:
            if x+"：" in line:
                gua_64_all_map[gua_name][x] = line

        if "文言曰：" in line:
            gua_64_all_map[gua_name]["文言曰"] = []
            read_wenyan(gua_name, line, file)

        if "第" in line and '卦' in line:
            read_one_gua(line, file)

        line = file.readline()

def print_gua(gua):
    v=gua_64_all_map[gua]
    print(gua_64_all_map[gua][gua])
    print(gua_64_all_map[gua]["卦辞"])
    print(gua_64_all_map[gua]["象曰"])
    for x in gua_index:
        if gua_64_all_map[gua].has_key(x):
            print(gua_64_all_map[gua][x])

    if gua_64_all_map[gua].has_key("文言曰"):
        for x in gua_64_all_map[gua]["文言曰"]:
            print x
def print_gua_all(gua = None):
    if gua == None:
        for (k,v) in gua_64_all_map.items():
            print_gua(k)
    else:
        print_gua(gua)

def read_yilin_one_gua(line, file):
    line = line.rstrip().lstrip().split("'")
    gua_name = line[1].rstrip().lstrip()
    gua_yilin_map[gua_name]=collections.OrderedDict()

    line = file.readline()
    while line:
        line = line.rstrip().lstrip()
        if "':'" in line:
            line = line.split("'")
            gua_yilin_map[gua_name][line[1]] = line[3]
        if ":{" in line:
            read_yilin_one_gua(line, file)

        line = file.readline()

def read_yinli_file(file):
    f = open(file)
    line = f.readline()

    while line:
        line = line.rstrip().lstrip()
        if ":{" in line:
            read_yilin_one_gua(line, f)
        line = f.readline()
    f.close()

    #print_yilin("1")


def print_yilin(gua=None):
    if gua == None:
        for (k,v) in gua_yilin_map.items():
            print_yilin_one_gua(k)
    else:
        print_yilin_one_gua(gua)


def get_gua_name_64(index):
    for (k,v) in gua_64_map.items():
        if v[1] == str(index):
            return v[2]

def print_yilin_one_gua(gua):
    gua_name = get_gua_name_64(int(gua))
    print gua_name + "卦："
    for (k,v) in gua_yilin_map[gua].items():
        zhi_gua_name = get_gua_name_64(int(k))
        name = gua_name + "之" + zhi_gua_name + ":"
        name = name.ljust(12)
        print name, v



read_gua_8(r"/Users/macpro/git_work/code/iching/buagua.txt")
read_gua_64(r"/Users/macpro/git_work/code/iching/64gua.txt")
read_gua_all(r"/Users/macpro/git_work/code/iching/64gua_all.txt")
read_yinli_file(r"/Users/macpro/git_work/code/iching/yinlindict.js")

# print_gua_8()
# print_gua_64()
# print_gua_64()
# print_gua_all()
# print_yilin()
