# -*- coding: utf-8 -*- 

#---------------------------------------  
#   程序：排序总控程序
#   版本： 
#   作者：WuChong
#   日期：2014-01-28
#   语言：Python 3.3 
#   说明：自动随机50个1-99之间数，并调用排序算法进行排序
#---------------------------------------

import random
import Sort.BubbleSort
import Sort.InsertionSort
import Sort.ShellSort
import Sort.SelectionSort
import Sort.MergeSort
import Sort.QuickSort
import Sort.HeapSort

arry = [random.randint(1,99) for i in range(20)]

print("排序前："+str(arry))

sorted_arry = Sort.HeapSort.heap_sort(arry)

print("排序后："+str(sorted_arry))