matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

def rotate_matrix(matrix):
    final=[]
    for i in range(len(matrix)):
        temp=[]
        for j in range(len(matrix[i])):
            temp.append(0)
        final.append(temp)
        
    if Square_Matrix(matrix) != True:
        return "Enter a Square Matrix."
    
    if Square_Matrix (matrix) == True:
        for i in range(0,len(matrix)):
            for j in range(len(matrix),0,-1):
                final[i][j-1]=matrix[len(matrix)-j][i]
        return final
                
        
def Square_Matrix (matrix):
    for i in matrix:
        if len(i)!=len(matrix):
            return False
    return True

print(rotate_matrix(matrix))
