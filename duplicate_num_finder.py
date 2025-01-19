numbers = [1, 2, 3, 2, 7, 8, 1, 5, 3]
def duplicates(arr):
    dupes=[]
    for i in arr:
        if arr.count(i)>1:
            dupes.append(i)
    return set(dupes)
print(duplicates(numbers))
