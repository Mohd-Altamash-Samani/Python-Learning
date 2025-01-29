# Link of the problem :  https://codeforces.com/problemset/problem/58/A

# Chat Room
s=input("")
check="hello"
position=0

for i in s:
    if i == check[position]:
        position +=1
    if len(check) == (position):
        break  

if position==len(check):
    print("YES")
else:
    print("NO")
 
