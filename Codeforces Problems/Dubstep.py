# Link of the problem : https://codeforces.com/problemset/problem/208/A

# Dubstep
n=input()
n=n.upper()
sp=n.split("WUB")
rem=[n for n in sp if n!='']
result=" ".join(rem)
print(result)