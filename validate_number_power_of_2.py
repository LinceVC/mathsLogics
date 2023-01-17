## Code to validate if the given number is Power of 2 or not ? 
## Solution is to divide number 2 half and check if it is divisible by 2 at each stage till it reaches 1
## Author: Lince V Chandy


x = int(input())
#YOUR CODE GOES HERE
ans = "Yes"
if x == 0:
    ans = "No"
    
while(x>1):
    if (x%2!=0):
        ans = "No"
        break
    else:
        x = x//2

print(ans)
