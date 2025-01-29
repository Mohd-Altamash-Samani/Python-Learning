# Link of the problem : https://codeforces.com/problemset/problem/263/A

# Beautiful Matrix
matrix=[]

for i in range(5):
    row=list(map(int,input().split()))
    matrix.append(row)

for i in range(5):
    for j in range(5):
        if matrix[i][j]==1:
            position=[i+1,j+1]

# using manhattan distance
row=abs(position[0]-3)
column=abs(position[1]-3)
print(row+column)
