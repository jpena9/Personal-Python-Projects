# -*- coding: utf-8 -*-
read=open('2020puzzle1_input.txt','r')
acct=read.readlines()


nums=[float(line) for line in acct]

## Part 1
sumyear=0
prodyear=0
for i in range(len(nums)):
    for j in range(len(nums)):
        sumyear=nums[i] + nums[j]
        if sumyear == 2020:
            prodyear=nums[i]*nums[j]
            print(nums[i], nums[j])
            print(prodyear)

## Part 2
sumyear=0
prodyear=0
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            sumyear=nums[i] + nums[j] + nums[k]
            if sumyear == 2020:
                prodyear=nums[i]*nums[j]*nums[k]
                print(nums[i], nums[j], nums[k])
                print(prodyear)
