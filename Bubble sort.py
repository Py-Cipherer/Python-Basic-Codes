"""
Bubble Sort is the simplest sorting algorithm
that works by repeatedly swapping the adjacent elements 
if they are in the wrong order. 
The time complexity of bubble sort is O(n^2), where n is the number of elements in the array.
Average and Worst case time complexity is Quadratic.
"""

#sample list named l
l=[12,75,8,36,4,98,52,14,]
#user defined function named "bubble_sort"
def bubble_sort(l):
    for i in range(len(l)):                #This loop iterates till the end of list
        for j in range(0,len(l)-i-1):      #On every iteration of "i" loop, "j" iterates (i+1) times less than length of list.
            if l[j]>l[j+1]:                #If an element is greater than the element after it then,
                l[j],l[j+1]=l[j+1],l[j]    #it swaps those elements with each other.
    return l                               #Finally it returns the sorted list.

print(bubble_sort(l))
