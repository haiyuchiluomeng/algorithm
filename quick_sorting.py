# -*- coding: utf-8 -*-
# Author:haiyuchiluomeng
#快速排序法
#时间复杂度：最好O(nlogn) 最坏O(n^2) 不稳定
def quick_sort(li,first,last):
    if first>=last:
        return
    mid_value=li[first]
    low=first
    high=last
    while low<high:
        while low<high and li[high]>=mid_value:
            high-=1
        li[low]=li[high]
        while low<high and li[low]<mid_value:
            low+=1
        li[high]=li[low]
    li[low]=mid_value
    quick_sort(li,first,low-1)
    quick_sort(li,low+1,last)
if __name__=="__main__":
    m=[89,33,12,75,64,28,2,36]
    quick_sort(m,0,len(m)-1)
    print(m)


