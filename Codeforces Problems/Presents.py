# Link of the problem :  https://codeforces.com/problemset/problem/136/A

# Presents 
n=int(input(""))
p=input("")

listing = list(map(int, p.split()))
result = [0] * n

for i in range(1, n + 1):  # Start from 1 to n
    p=listing[i - 1] - 1
    result[p] = i

result=" ".join(map(str,result))
print(result)
    


 
