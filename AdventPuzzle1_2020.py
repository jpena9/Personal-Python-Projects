# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:51:52 2021

@author: artak
"""

read=open('puzzle_input.txt','r')
acct=read.readlines()


nums=[float(line) for line in acct]

sumyear=0
prodyear=0
for i in range(len(nums)):
    for j in range(len(nums)):
        sumyear=nums[i] + nums[j]
        if sumyear == 2020:
            prodyear=nums[i]*nums[j]
            print(nums[i], nums[j])
            print(prodyear)
