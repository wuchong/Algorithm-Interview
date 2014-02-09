# -*- coding: utf-8 -*- 

#---------------------------------------  
#   程序：直接插入排序
#   版本：0.1
#   作者：WuChong
#   日期：2014-01-29
#   语言：Python 3.3 
#   说明：  
#---------------------------------------

def insert_sort(ary):
    n = len(ary)
    for i in range(1,n):
        if ary[i] < ary[i-1]:
            temp = ary[i]
            index = i           #待插入的下标
            for j in range(i-1,-1,-1):  #从i-1 循环到 0 (包括0)
                if ary[j] > temp :
                    ary[j+1] = ary[j]
                    index = j   #记录待插入下标
                else :
                    break
            ary[index] = temp
    return ary
