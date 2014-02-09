# -*- coding: utf-8 -*- 

#---------------------------------------  
#   程序：希尔排序
#   版本： 0.1
#   作者：WuChong
#   日期：2014-02-08
#   语言：Python 3.3 
#   说明：
#---------------------------------------

def shell_sort(ary):
    n = len(ary)
    gap = round(n/2)       #初始步长 , 用round四舍五入取整
    while gap > 0 :
        for i in range(gap,n):        #每一列进行插入排序 , 从gap 到 n-1
            temp = ary[i]
            j = i
            while ( j >= gap and ary[j-gap] > temp ):    #插入排序
                ary[j] = ary[j-gap]
                j = j - gap
            ary[j] = temp
        gap = round(gap/2)                     #重新设置步长
    return ary