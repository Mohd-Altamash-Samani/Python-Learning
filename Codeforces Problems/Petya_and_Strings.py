# Link of the problem : https://codeforces.com/problemset/problem/112/A

# Petya and Strings
first=input("").lower()
second=input("").lower()

if first<second:
    print(-1)
elif first>second:
    print(1)
else:
    print(0)
    