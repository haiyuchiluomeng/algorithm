# -*- coding: utf-8 -*-
# Author:haiyuchiluomeng
#直接选择排序法
#时间复杂度：最好O(n) 最坏O(n^2) 不稳定
def selection_sort(li):
    n=len(li)
    for j in range(0,n-1):
        min_index=j#最小值坐标
        for i in range(j+1,n):
            if li[i]<li[min_index]:
                min_index=i
            li[j],li[min_index]=li[min_index],li[j]
if __name__ =="__main__":
    m=[89,33,12,75,64,28,2,36,1]
    selection_sort(m)
    print(m)