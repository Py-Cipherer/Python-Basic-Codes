import pickle
import sys
import time

def read_data_from_file(file_path):
    try:
        with open(file_path, "rb") as file:
            data = pickle.load(file)
    except (EOFError, FileNotFoundError):
        data = {}
    return data

def write_data_to_file(data, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(data, file)

def insert():
    file_path = r"C:\Users\Administrator\Desktop\txt files\omg.dat"
    data = read_data_from_file(file_path)
    nw_id = int(input("Enter news Id or Code= "))
    news = input("Enter a brief title for the news= ")
    data[nw_id] = news
    write_data_to_file(data, file_path)
    print("News data has been successfully inserted in the Log.")
    news_log()

def update():
    file_path = r"C:\Users\Administrator\Desktop\txt files\omg.dat"
    data = read_data_from_file(file_path)
    temp = int(input("Enter News ID or Code to find= "))
    if temp in data.keys():
        print("Log found.")
        nw_id = int(input("Enter new news id or code= "))
        news = input("Enter new news title for the news= ")
        data[nw_id] = news
        write_data_to_file(data, file_path)
        print("Data successfully updated.")
        print(nw_id, " = ", data[nw_id])
    else:
        print("No such log found.")
    news_log()

def delete():
    file_path = r"C:\Users\Administrator\Desktop\txt files\omg.dat"
    data = read_data_from_file(file_path)
    nw_id = int(input("Enter news id or code to delete= "))
    if data.pop(nw_id, None) is None:
        print("No such log found. Deletion process terminated.")
    else:
        print("Log deleted successfully. ")
    write_data_to_file(data, file_path)
    news_log()

def search():
    file_path = r"C:\Users\Administrator\Desktop\txt files\omg.dat"
    data = read_data_from_file(file_path)
    nw_id = int(input("Enter news id or code to search log= "))
    if data.get(nw_id, None) is None:
        print("No such log found.")
    else:
        print("Data Found.\n", nw_id, data[nw_id])
    news_log()

def display():
    file_path = r"C:\Users\Administrator\Desktop\txt files\omg.dat"
    data = read_data_from_file(file_path)
    for key, value in data.items():
        print(key, "=", value)
    news_log()

def news_log():
    while True:
        print("1. Insert data\n2. Update data\n3. Delete data\n4. Search data\n5. Display all data\n6. Exit")
        time.sleep(2)
        ch = int(input("Enter your choice [1-6]= "))
        if ch == 1:
            insert()
        if ch == 2:
            update()
        if ch == 3:
            delete()
        if ch == 4:
            search()
        if ch == 5:
            display()
        if ch == 6:
            sys.exit()
        else:
            print("Enter a valid choice!! \n")

news_log()
