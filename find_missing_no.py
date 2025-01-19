complete_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
missing_list = [1, 2, 3, 4, 6, 7, 8, 9, 10]

def find_missing_number(complete_list, missing_list):
    complete_list.sort()
    missing_list.sort()
    missing=[]
    print(complete_list)
    print(missing_list)
    for i in complete_list:
        if i not in missing_list:
            missing .append(i)
    return"Missing numbers= ",missing
print(find_missing_number(complete_list, missing_list))
