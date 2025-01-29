# Link of the problem : https://codeforces.com/problemset/problem/69/A
# Young Physicist

n=int(input())
s_x=0
s_y=0
s_z=0

for i in range(n):
    x,y,z = map(int,input().split(" "))
    s_x +=x
    s_y +=y
    s_z +=z
    
if s_x ==0 and s_y==0 and s_z==0:
    print("YES")
else:
    print("NO")