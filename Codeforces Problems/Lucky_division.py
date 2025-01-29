# Link of the problem : https://codeforces.com/problemset/problem/122/A

# Lucky Division
n=int(input(""))

seq="12356890"
flag=True
for i in str(n):
    if i in seq:
        flag=False        

l=[4,7,44,77,47,74,444,447,474,744,777,774,747,477]
if flag:
    print("YES")
else:
    for i in l:
        if n%i==0:
            print("YES")  
            break
    else:
        print("NO")