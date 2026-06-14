N = int(input())
arr = []

for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)

arr.sort(key=lambda x: (x[0], x[1]))

for element in arr:
    print(element[0], element[1])