# -*- coding: utf-8 -*-
# Author:haiyuchiluomeng
#冒泡排序法
#时间复杂度(优化过的）:最好O(n) 最坏O(n^2) 稳定
def bubble_sort(li):
    n=len(li)
    for j in range(0,n-1):#总共要进行的循环次数
        count=0
        for i in range(0,n-j-1):#每一次下标要到达的
            if li[i]>li[i+1]:
                li[i],li[i+1]=li[i+1],li[i]
                count+=1
        if count==0:
            return
if __name__=="__main__":
    m=[89,33,12,75,64,28,2,36]
    bubble_sort(m)
    print(m)