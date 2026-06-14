N = int(input())
arr = []

for i in range(N):
    temp = input().split()
    temp.append(i)
    arr.append(temp)

arr.sort(key=lambda x: (int(x[0]), x[2]))

for element in arr:
    print(int(element[0]), element[1])