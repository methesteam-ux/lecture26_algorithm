N = int(input())
arr = []

for _ in range(N):
    arr.append(input())

arr.sort(key=lambda x: (len(x), x))

for word in arr:
    print(word)