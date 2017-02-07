#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#冒泡排序

mylist = [89, 76, 11, 99, 54, 33, 66, 78, 80]

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
print(mylist)