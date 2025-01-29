# Link of the problem : https://codeforces.com/problemset/problem/451/A

# Games

n=int(input(""))

home=[]
guest=[]

for i in range(n):
    h,a =map(int,input().split())
    
    home.append(h)
    guest.append(a)

conf=0
for i in home:
    for j in guest:
        if i==j:
            conf +=1
print(conf)            