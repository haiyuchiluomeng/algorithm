# -*- coding: utf-8 -*-
# Author:haiyuchiluomeng
#希尔排序法
#时间复杂度:最好O(n) 最坏O(n^2) 平均O(n^1.3) 不稳定
def shell_sort(li):
    n=len(li)
    gap=n//2
    while gap>0:
        for j in range(gap,n):
            i=j
            while i>0:
                if li[i]<li[i-gap]:
                    li[i],li[i-gap]=li[i-gap],li[i]
                    i-=gap
                else:
                    break
        gap=gap//2
if __name__=="__main__":
    m=[89,33,12,75,64,28,2,36]
    shell_sort(m)
    print(m)
