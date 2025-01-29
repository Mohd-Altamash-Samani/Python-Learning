# Link of the problem : https://codeforces.com/problemset/problem/451/A

# Game With Sticks
stick=list(map(int,input("").split(" ")))
count=0
no_int=1
i=0
while(no_int!=0):
    count+=1
    i+=1
    no_int=(stick[0]-i)*(stick[1]-i)

print(count)
result="Malvika" if count % 2 == 0 else "Akshat"
print(result)