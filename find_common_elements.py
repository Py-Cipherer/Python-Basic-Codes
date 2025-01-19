list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 7, 9, 11]
def find_common_elements(list1, list2):
    newlist=[]
    for i in list1:
        for j in list2:
            if i==j:
                newlist.append(i)
    return newlist

print(find_common_elements(list1, list2))
