#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#冒泡排序

#排序函数
def bubbling_sort(mylist):
	size = len(mylist)
	i = 0
	while i < size:
		j = i
		while  j < size:
			if(mylist[i] > mylist[j]):
				temp = mylist[j]
				mylist[j] = mylist[i]
				mylist[i] = temp
			j = j + 1
		i = i + 1
	return mylist


#调用函数
mylist = [89, 76, 11, 99, 54, 33, 66, 78, 80]

print(bubbling_sort(mylist))