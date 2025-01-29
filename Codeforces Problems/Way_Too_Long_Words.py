# Link of the problem : https://codeforces.com/problemset/problem/71/A

# Way Too Long Words
no=int(input(""))

for i in range(no):
 n=input("")   
 if len(n)<=10:
    print(n)
 else:
    first=n[0]
    last=n[-1]
    final=first + str(len(n[1:-1])) + last
    print(final)