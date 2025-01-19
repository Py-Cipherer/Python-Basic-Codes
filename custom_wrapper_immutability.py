class immutability:

    
    def __init__(self,data):
        self.data = data

        
    def __getitem__(self,index):
        return self.data[index]


    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)


l=[1,2,2,3,5,6]
l=immutability(l)
#l[2]=5         #--gives error beacuse the wrapper is restricting the mutability.
print(l[:len(l):])
print(l)
