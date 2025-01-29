# Link of the problem : https://codeforces.com/problemset/problem/160/A

# Twins
n = int(input(""))
seq = input("")
 
coins = list(map(int, seq.split()))  
coins.sort(reverse=True)
 
total_sum = sum(coins)
selected_sum = 0
count = 0
for coin in coins:
    selected_sum += coin
    count += 1
    # Stop when the sum of selected coins is greater than half the total sum
    if selected_sum > total_sum / 2:
        break
        
print(count)