# Link of the problem : https://codeforces.com/problemset/problem/339/A

# Helpful Maths
s=input("")
p=s.replace("+", ",")
p=p.split(",")
p=[int(x) for x in p]

def minimum(num):
    min=num[0]
    for i in num:
      if min>i:
        min=i
    return min

def sort(num):
    sort=[]
    while len(num)>0:
        min=minimum(num)
        sort.append(min)
        num.remove(min)
    return sort

ans=sort(p)
ans=[str(x) for x in ans]
ans=",".join(ans)
ans=ans.replace(",","+")
print(ans)