import csv

def read_from_csv(path):
    with open(path, "r") as file:
        data = csv.reader(file)
        li_data = [row for row in data if row]  #for avoiding empty lists from being appended
        return li_data

def append_to_csv(path, row):
    with open(path, "a", newline='') as file:
        d = csv.writer(file)
        d.writerow(row)
    return "Row inserted."

def write_to_csv(path, data):
    with open(path, "w", newline='') as file:
        d = csv.writer(file)
        d.writerows(data)
    return "Data written to file successfully."

def insert():
    prod_ID = input("Enter product ID= ")
    prod_nm = input("Enter product name = ")
    prod_mrp = float(input("Enter product MRP = "))
    row = [prod_ID, prod_nm, prod_mrp]
    path = r"C:\Users\Administrator\Desktop\txt files\MRP_rates.csv"
    print(append_to_csv(path, row))

def search():
    n = input("Enter prod ID to search= ")
    path = r"C:\Users\Administrator\Desktop\txt files\MRP_rates.csv"
    d = read_from_csv(path)
    print(d)
    for i in d:
        if i[0] == n:
            print("Match Found")
            return i
    return None

def delete():
    path = r"C:\Users\Administrator\Desktop\txt files\MRP_rates.csv"
    data = read_from_csv(path)
    v = search()
    if v is not None:
        data.remove(v)
        write_to_csv(path, data)
        print("Entry deleted successfully.")


def display():
    path = r"C:\Users\Administrator\Desktop\txt files\MRP_rates.csv" 
    d = read_from_csv(path)
    print("\nThe content of this file is following.\n[<prod_ID>, <prod_name>, <prod_price>]")
    for i in d:
        print(i)

def main_menu():
    while True:
        print("1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit\n")
        ch = int(input("Enter your choice:- "))
        if ch == 1:
            insert()
        elif ch == 2:
            result = search()
            if result:
                print(result)
            else:
                print("No match found.")
        elif ch == 3:
            delete()
        elif ch == 4:
            display()
        elif ch == 5:
            break
        else:
            print("Enter choice in range(1-5).")

main_menu()
