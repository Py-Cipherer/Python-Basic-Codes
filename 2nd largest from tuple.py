"""
We are using Bubble sorting technique.
Bubble Sort is the simplest sorting algorithm that works by 
repeatedly swapping the adjacent elements if they are in the wrong order.
* This algorithm is not suitable for large data sets because its average and worst-case time complexity are quite high.
"""

def Bubble_sort(tup):
    l=list(tup)    #Explicit type conversion to list bcoz tuples are immutable.
    b=len(l)     #<---- you can skip this and write len(l) directly in place of b in range.
    for reference in range(b-1):     #<--- Loop reference pointer which moves towards 1st element sorting each value behind it by swapping adjacent values.
        for j in range(b-reference-1):    
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    print("Original Tuple= ",tup)
    print("Sorted tuple= ",tuple(l))
    print("2nd Largest value= ",l[-2])
Bubble_sort(5,62,6,781,112)
