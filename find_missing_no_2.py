complete_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
missing_list = [1, 2, 3, 4, 6, 7, 10]

def missing(complete_list,missing_list):
    complete_list= set(complete_list)
    missing_list= set(missing_list)
    missing_numbers = complete_list - missing_list
    return missing_numbers
print(missing(complete_list,missing_list))
