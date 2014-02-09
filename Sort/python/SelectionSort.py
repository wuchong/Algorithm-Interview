# -*- coding: utf-8 -*- 

#---------------------------------------  
#   程序：选择排序
#   版本：
#   作者：WuChong
#   日期：2014-02-08
#   语言：Python 3.3 
#   说明：
#---------------------------------------

def select_sort(ary):
    n = len(ary)
    for i in range(0,n):
        min = i                         #找到最小值的下标
        for j in range(i+1,n):
            if ary[j] < ary[min] :
                min = j
        ary[min],ary[i] = ary[i],ary[min]   #交换两者
    return ary


