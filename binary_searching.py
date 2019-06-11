# -*- coding: utf-8 -*-
# Author:haiyuchiluomeng
#二分查找
def binary_search1(li,item):
    n=len(li)#传入的列表长度
    if n>0:
        mid=n//2#列表中间位置
        if li[mid]==item:
            return True
        elif li[mid]>item:
            return binary_search1(li[:mid],item)#左边列表继续递归
        else:
            return binary_search1(li[mid+1:],item)#右边列表递归
    else:
        return False
def binary_search2(li,item):
    n=len(li)
    first=0
    last=n-1
    while first<last:
        mid = (first + last) // 2
        if li[mid] == item:
            return True
        elif li[mid] > item:
            last=mid-1
        else:
            first=mid+1
    return False
if __name__=="__main__":
    m=[2,15,19,77,90,95,100]
    print(binary_search1(m,43))
    print(binary_search1(m,90))

