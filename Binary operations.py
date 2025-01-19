# Write a menu driven program as following:
#
# Insert record
# Search Record
# Update Record
# Display record
# Exit
# Use cust.dat for this program created in pro3.

import pickle

def insert():
    print()
    with open(r"C:\Users\Administrator\Desktop\txt files\Cust.dat", "ab") as file:
        di = input("Enter ID: ")
        nm = input("Enter Name: ")
        city = input("Enter City: ")
        pickle.dump([di, nm, city], file)
    print()

def search():
    print()
    with open(r"C:\Users\Administrator\Desktop\txt files\Cust.dat", "rb") as file:
        flag = False
        se = input("Enter ID to search: ")
        while True:
            try:
                data = pickle.load(file)
                if data[0] == se:
                    flag = True
                    save = data
            except:
                break
    if flag == True:
        print("Value Found.")
        print(save)
    else:
        print("Value Not found.")
    print()

def update():
    print()
    l=[]
    with open(r"C:\Users\Administrator\Desktop\txt files\Cust.dat", "rb") as file:
        flag = False
        se = input("Enter ID to search: ")
        while True:
            try:
                data = pickle.load(file)
                l.append(data)
            except:
                break
    with open(r"C:\Users\Administrator\Desktop\txt files\Cust.dat", "wb") as file:
        di = input("Enter New ID: ")
        nm = input("Enter New Name: ")
        c = input("Enter New City: ")
        pickle.dump([di,nm,c],file)
        for i in l:
            if se != i[0]:
                pickle.dump(i,file)
        print("Updated.")
    print()


def display():
    print()
    with open(r"C:\Users\Administrator\Desktop\txt files\Cust.dat", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                print(data)
            except:
                break
    print()
def delete():
    print()
    l=[]
    with open(r"C:\Users\Administrator\Desktop\txt files\Cust.dat", "rb") as file:
        se = input("Enter ID to search: ")
        while True:
            try:
                l.append(pickle.load(file))
            except:
                break
    with open(r"C:\Users\Administrator\Desktop\txt files\Cust.dat", "wb") as file:
        for i in l:
            if se != i[0]:
                pickle.dump(i,file)
while True:
    print("1 <---- Insert a new data.")
    print("2 <---- Update an existing data.")
    print("3 <---- Display data.")
    print("4 <---- Search Data.")
    print("5 <---- Delete Data.")
    print('6 <---- Exit.')
    ch = int(input("Enter YOur choice: "))
    if (ch == 1):
        insert()
    elif (ch == 2):
        update()
    elif (ch == 3):
        display()
    elif (ch == 4):
        search()
    elif (ch == 5):
        delete()
    elif (ch == 6):
        break
    else:
        print("Invalid Choice!!")
