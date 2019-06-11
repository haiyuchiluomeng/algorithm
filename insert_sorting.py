# -*- coding: utf-8 -*-
# Author:haiyuchiluomeng
#插入排序法
#时间复杂度:最好O(n) 最坏O(n^2) 不稳定
def insert_sort(li):
    n=len(li)
    for j in range(1,n):
        i=j
        while i>0:#每一次与前面的数相比
            if li[i]<li[i-1]:
                li[i],li[i-1]=li[i-1],li[i]
                i-=1
            else:
                break
if __name__=="__main__":
    m=[89,33,12,75,64,28,2,36]
    insert_sort(m)
    print(m)
