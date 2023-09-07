lst=[3,55,6,2,4,10,999,14,22,-2]
sum=int(input())
#first method
def normal(lst,sum):
    for i in lst:
        if sum-i in lst:
            print("Found:{x} and {y}".format(x=i,y=sum-i))
            return
    print("Not found")
    return
def two_pointers(lst,sum):
    lst=sorted(lst)
    i=0
    j=len(lst)-1
    while i<j:
        if lst[i]+lst[j]==sum:
            print("Found:{x} and {y}".format(x=lst[i],y=lst[j]))
            return
        elif lst[i]+lst[j]>sum:
            j-=1
        else:
            i+=1
    print("Not found")
    return

def binary_search(lst,num):
    first=0
    last=len(lst)-1
    while first<=last:
        mid=first+(last-first+1)//2
        if lst[mid]==num:
            return mid
        elif lst[mid]<num:
            first=mid+1
        else:
            last=mid-1
    return -1

def sum_by_binsearch(lst,sum):
    lst=sorted(lst)
    for i in lst:
        if binary_search(lst,sum-i)!= -1:
            print("Found:{x} and {y}".format(x=i,y=sum-i))
            return
        else:
            continue
    print("Not found")
    return

two_pointers(lst,sum)
normal(lst,sum)
sum_by_binsearch(lst,sum)