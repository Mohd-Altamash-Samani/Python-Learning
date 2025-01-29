# Link of the problem : https://codeforces.com/problemset/problem/118/A

# String Task
n = input("")
n = n.lower()
vow = ['a','o','y','e','u','i']
store = []

for i in n:
    if i not in vow:
        store.append(i)

b="."
add=[]
for i in store:
    word = b + i
    add.append(word)
    
ans=''.join(add)
print(ans)

# OR 

# String Task
n=input("")
vow="aeiouyAEIOUY"
sol=""
for i in n:
    if i not in vow:
        sol=sol + "." + i.lower()
print(sol)    