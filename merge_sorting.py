# -*- coding: utf-8 -*-
# Author:haiyuchiluomeng
#归并排序法
#时间复杂度：最优O(nlogn) 最坏O(nlogn) 稳定
def merge_sort1(li):
    n = len(li)
    if n<=1:
        return li
    mid=n//2
    left_li = merge_sort1(li[:mid])
    right_li = merge_sort1(li[mid:])
    left_pointer,right_pointer=0,0
    result=[]
    while left_pointer<len(left_li) and right_pointer<len(right_li):
        if left_li[left_pointer]<right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer+=1
        else:
            result.append(right_li[right_pointer])
            right_pointer+=1
    result+=left_li[left_pointer:]
    result+=right_li[right_pointer:]
    return result
def merge_sort2(li):
    # 不断递归调用自己一直到拆分成成单个元素的时候就返回这个元素，不再拆分了
    if len(li)==1:
        return li
    mid=len(li)//2#取拆分的中间位置
    left=li[:mid]
    right=li[mid:]#拆分过后左右两侧子串
    l1 = merge_sort2(left)
    r1 = merge_sort2(right)#对拆分过后的左右再拆分 一直到只有一个元素为止
    # 最后一次递归时候ll和lr都会接到一个元素的列表
    #对返回的两个拆分结果进行排序后合并再返回正确顺序的子列表
    return merge(l1,r1)# 调用一个函数帮助我们按顺序合并ll和lr

def merge(left,right):
    result=[]
    while len(left)>0 and len(right)>0:
        if left[0]<=right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result+=left
    result+=right
    return result
if __name__=="__main__":
    m=[89,33,12,75,64,28,2,36,7]
    x=merge_sort1(m)
    print(x)


