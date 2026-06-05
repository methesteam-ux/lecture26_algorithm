num, k = map(int, input().split())
arr = list(range(1, num+1))
death = []
temp = 0
    
while arr:
    temp = (temp + k-1) % len(arr)
    death.append(arr.pop(temp))

print("<", end="")  
for i in range(len(death)-1):
    print(death[i], end=", ")
print(death[-1], end="")
print(">", end="")