arr = [1, -2, 3, 4, -1, 2, 8, 1, -5, 4]
target = 6

def find_longest_subarray(arr,target):
    visited = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (sum(arr[i:j]) < target) or sum(arr[i:j]) == target :
                visited.append(arr[i:j])
    maxx=0
    arr2=[]
    for k in visited:
        if len(k)>maxx:
            maxx=len(k)
            arr2=k
    return maxx,arr2
print(find_longest_subarray(arr, target))
