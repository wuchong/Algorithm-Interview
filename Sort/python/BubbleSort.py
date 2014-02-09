# -*- coding: utf-8 -*- 

#---------------------------------------  
#   程序：冒泡排序
#   版本：0.1
#   作者：WuChong
#   日期：2014-01-28
#   语言：Python 3.3 
#   说明：冒泡排序，从小到大排序，以及加了两种优化
#---------------------------------------

def bubble_sort(arry):
    n = len(arry)                   #获得数组的长度
    for i in range(n):
        for j in range(1,n-i):
            if  arry[j-1] > arry[j] :       #如果前者比后者大
                arry[j-1],arry[j] = arry[j],arry[j-1]       #则交换两者
    return arry


#优化1：某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。
#用一个标记记录这个状态即可。
def bubble_sort2(arry):
    n = len(arry)
    for i in range(n):
        flag = 1                    #标记
        for j in range(1,n-i):
            if  arry[j-1] > arry[j] :
                arry[j-1],arry[j] = arry[j],arry[j-1]
                flag = 0
        if flag :                   #全排好序了，直接跳出
            break
    return arry

#优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序了。
# 因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。
def bubble_sort3(arry):
    n = len(arry)
    k = n                           #k为循环的范围，初始值n
    for i in range(n):
        flag = 1
        for j in range(1,k):        #只遍历到最后交换的位置即可
            if  arry[j-1] > arry[j] :
                arry[j-1],arry[j] = arry[j],arry[j-1]
                k = j               #记录最后交换的位置
                flag = 0
        if flag :
            break
    return arry