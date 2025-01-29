# Link of the problem : https://codeforces.com/problemset/problem/144/A

# Arrival of the General
i=int(input(""))
s=input("")
ls=list(map(int,s.split(" ")))

n=len(ls)
maxi=ls.index(max(ls))
mini=len(ls)-1 - ls[::-1].index(min(ls))

if maxi > mini:
    position = maxi + (n - 1 - mini) -1 # (overlaps)
else:
    position = maxi + (n - 1 - mini)  
    
print(position)


# # Input number of soldiers
# n = int(input())
# # Input the list of soldier heights
# s = input()

# # Convert the input string of heights into a list of integers
# ls = list(map(int, s.split()))

# # Find the index of the tallest soldier (first occurrence of max height)
# maxi = ls.index(max(ls))

# # Find the index of the shortest soldier (first occurrence of min height)
# mini = ls.index(min(ls))

# # Steps to bring the tallest to the front: 'maxi' swaps to bring to the front
# # Steps to bring the shortest to the back: (n - 1 - mini) swaps to bring to the back
# if maxi > mini:
#     # If the tallest soldier is to the right of the shortest soldier, we subtract 1 for overlap
#     swaps = maxi + (n - 1 - mini) - 1
# else:
#     # If they don't overlap, just sum the swaps
#     swaps = maxi + (n - 1 - mini)

# # Output the result (minimum number of swaps)
# print(swaps)
