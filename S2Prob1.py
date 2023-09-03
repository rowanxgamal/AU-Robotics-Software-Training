def binarySearch(lst,start,end,search):
    if start>end:
        return -1
    else:
        mid=start+(end-start)//2
        if lst[mid]==search:
            return mid
        elif lst[mid]<search:
            start=mid+1
            return binarySearch(lst,mid+1,end,search)
        else:
            return binarySearch(lst,start,mid-1,search)
        
lst=[3,5,6,7,8,9,11,312]
element=int(input())
element=binarySearch(lst,0,len(lst)-1,element)
if element!=-1:
    print("Found {search} at index: {index}".format(search=lst[element],index=element))
else:
    print("Not found")