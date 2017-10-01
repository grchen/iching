# -*- coding:utf-8 -*-


import random
gua_map_64 = {
        "111111":["䷀","1","乾","乾为天"],
        "000000":["䷁","2","坤","坤为地"],
        "010001":["䷂","3","屯","水雷屯"],
        "100010":["䷃","4","蒙","山水蒙"],
        "010111":["䷄","5","需","水天需"],
        "111010":["䷅","6","讼","天水讼"],
        "000010":["䷆","7","师","地水师"],
        "010000":["䷇","8","比","水地比"],
        "110111":["䷈","9","小畜","风天小畜"],
        "111011":["䷉","10","履","天泽履"],
        "000111":["䷊","11","泰","天地泰"],
        "111000":["䷋","12","否","地天否"],
        "111101":["䷌","13","同人","天火同人"],
        "101111":["䷍","14","大有","火天大有"],
        "000100":["䷎","15","谦","地山谦"],
        "001000":["䷏","16","豫","雷地豫"],
        "011001":["䷐","17","随","泽雷随"],
        "100110":["䷑","18","蛊","山风蛊"],
        "000011":["䷒","19","临","地泽临"],
        "110000":["䷓","20","观","风地观"],
        "101001":["䷔","21","噬嗑","火雷噬嗑"],
        "100101":["䷕","22","贲","山火贲"],
        "100000":["䷖","23","剥","山地剥"],
        "000001":["䷗","24","复","地雷复"],
        "111001":["䷘","25","无妄","天雷无妄"],
        "100111":["䷙","26","大畜","山天大畜"],
        "100001":["䷚","27","颐","山雷颐"],
        "011110":["䷛","28","大过","泽风大过"],
        "010010":["䷜","29","坎","坎为水"],
        "101101":["䷝","30","离","离为火"],
        "011100":["䷞","31","咸","泽山咸"],
        "001110":["䷟","32","恒","雷风恒"],
        "111100":["䷠","33","遯","天山遯"],
        "001111":["䷡","34","大壮","雷天大壮"],
        "101000":["䷢","35","晋","火地晋"],
        "000101":["䷣","36","明夷","地火明夷"],
        "110101":["䷤","37","家人","风火家人"],
        "101011":["䷥","38","睽","火泽睽"],
        "010100":["䷦","39","蹇","水山蹇"],
        "001010":["䷧","40","解","雷水解"],
        "100011":["䷨","41","损","山泽损"],
        "110001":["䷩","42","益","风雷益"],
        "011111":["䷪","43","夬","泽天夬"],
        "111110":["䷫","44","姤","天风姤"],
        "011000":["䷬","45","萃","泽地萃"],
        "000110":["䷭","46","升","地风升"],
        "011010":["䷮","47","困","泽水困"],
        "010110":["䷯","48","井","水风井"],
        "011101":["䷰","49","革","泽火革"],
        "101110":["䷱","50","鼎","火风鼎"],
        "001001":["䷲","51","震","震为雷"],
        "100100":["䷳","52","艮","艮为山"],
        "110100":["䷴","53","渐","风山渐"],
        "001011":["䷵","54","归妹","雷泽归妹"],
        "001101":["䷶","55","丰","雷火丰"],
        "101100":["䷷","56","旅","火山旅"],
        "110110":["䷸","57","风","巽为风"],
        "011011":["䷹","58","泽","兑为泽"],
        "110010":["䷺","59","涣","风水涣"],
        "010011":["䷻","60","节","水泽节"],
        "110011":["䷼","61","中孚","风泽中孚"],
        "001100":["䷽","62","小过","雷山小过"],
        "010101":["䷾","63","既济","水火既济"],
        "101010":["䷿","64","未济","火水未济"],
        }

gua_map_8 = {
        "111":["☰","1","乾","天"],
        "011":["☱","2","兑","泽"],
        "101":["☲","3","离","火"],
        "001":["☳","4","震","雷"],
        "110":["☳","5","巽","风"],
        "010":["☵","6","坎","水"],
        "100":["☶","7","艮","山"],
        "000":["☷","8","坤","地"],
}

def get_bi_str(index):
    result = ""

    value = bin(index).replace("0b","00")
    length = len(value)

    if length < 6:
        for x in range(6 - length):
            result = result + "0"
        result = result + value
    else:
        result = value[length-6:length]
    return result

def get_up_gua(gua_str):
    return gua_str[0:3]

def get_down_gua(gua_str):
    return gua_str[3:6]

def get_xxx(xxx):
    return ""


def get_one_chage(default_number):
    random_number = random.randint(1, default_number)

    number1 = random_number - 1
    number2 = default_number - number1 - 1

    result1 = 4 if number1%4 == 0 else number1%4
    result2 = 4 if number2%4 == 0 else number2%4
    return 1 + result1 + result2

def get_one_yao():
    result = get_one_chage(49)
    result1 = get_one_chage(49 - result)
    result2 = get_one_chage(49 - result - result1)
    return (49 - result - result1 - result2)/4

def get_one_gua():
    result=[]
    for x in range(6):
        result.append(get_one_yao())
    return result

def get_gua_name(gua_data):

    return gua_map_64[get_ben_gua(gua_data)][0]

def get_ben_gua(gua_data):
    result = ""
    for x in range(6):
        if gua_data[x] == 9: result = result + "1"
        if gua_data[x] == 6: result = result + "0"
        if gua_data[x] == 7: result = result + "1"
        if gua_data[x] == 8: result = result + "0"
    return result

def get_zhi_gua(gua_data):
    result = ""
    for x in range(6):
        if gua_data[x] == 9: result = result + "0"
        if gua_data[x] == 6: result = result + "1"
        if gua_data[x] == 7: result = result + "1"
        if gua_data[x] == 8: result = result + "0"
    return result


def print_gua(gua_data):
    chang_yao_number = 0
    bengua = get_ben_gua(gua_data)
    zhigua = get_zhi_gua(gua_data)

    for x in range(5, -1, -1):
        if gua_data[x] == 9: print("---    ->    - - XX")
        if gua_data[x] == 6: print("- -    ->    --- XX")
        if gua_data[x] == 7: print("---    ->    ---")
        if gua_data[x] == 8: print("- -    ->    - -")

        if gua_data[x] == 9 or gua_data[x] == 6:
           chang_yao_number = chang_yao_number + 1

    print("本卦:", gua_map_64[bengua][0],gua_map_64[bengua][3])
    print("之卦:", gua_map_64[zhigua][0],gua_map_64[zhigua][3])

    sum_number = sum(gua_data)
    number = 55 - sum_number
    result1 = number/6
    result2 = number%6

    forcast_change_yao = 1
    if result2%2 == 0:
        if result1%2 == 0:
            forcast_change_yao = 1
        else:
            forcast_change_yao = 6
    else:
        if result1%2 == 0:
            forcast_change_yao = result2
        else:
            forcast_change_yao = 6 - result2 + 1

    print("宜变爻位:", forcast_change_yao)

    if gua_data[int(forcast_change_yao) - 1] == 9 or gua_data[int(forcast_change_yao) - 1] == 6:
        print("实际宜变变爻:", forcast_change_yao)
    else:
        print("变爻个数:", chang_yao_number)
        if chang_yao_number <= 3:
            print("使用本卦卦辞断卦:", get_ben_gua(gua_data),get_gua_name(gua_data))
        else:
            print("使用之卦卦辞断卦:", get_zhi_gua(gua_data),get_gua_name(gua_data))



print_gua(get_one_gua())
print(get_bi_str(3))
print(get_up_gua("101001"))
print(get_down_gua("101001"))
