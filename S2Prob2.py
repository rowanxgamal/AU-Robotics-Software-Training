#Sorting algorithms

#Bubble sort
def bubblesort(lst):
    for i in range (len(lst)):
        for j in range (len(lst)-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
#Selection sort
def selectionsort(lst):
    for i in range (len(lst)):
        index=i
        for j in range (i+1,len(lst)):
            if lst[j]<lst[index]:
                index=j
        lst[i],lst[index]=lst[index],lst[i]
    return lst

lst=[3,7,8,4,1,1,2,-99000]
lst2=[3,7,8,4,1,1,2,-99000]
print(bubblesort(lst))
print(selectionsort(lst2))

