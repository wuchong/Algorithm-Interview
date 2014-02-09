# -*- coding: utf-8 -*- 

#---------------------------------------  
#   程序：归并排序
#   版本：
#   作者：WuChong
#   日期：2014-02-08
#   语言：Python 3.3 
#   说明：归并的思想就是先递归分解，再合并数组
#---------------------------------------

def merge_sort(ary):
    if len(ary) <= 1 : return ary
    num = int(len(ary)/2)       #二分分解
    left = merge_sort(ary[:num])
    right = merge_sort(ary[num:])
    return merge(left,right)    #合并数组

def merge(left,right):
    '''合并操作，
    将两个有序数组left[]和right[]合并成一个大的有序数组'''
    l,r = 0,0           #left与right数组的下标指针
    result = []
    while l<len(left) and r<len(right) :
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result