from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N + 1)) # 1부터 N까지 한 번에 넣기

count = 1
print('<', end='')

# 큐에 숫자가 1개 남을 때까지 반복 (마지막 숫자는 쉼표 없이 출력하려고)
while len(queue) > 1:
    person = queue.popleft()
    
    if count != K:
        queue.append(person)
        count += 1
    else:
        # K번째라면 숫자와 쉼표를 같이 출력
        print(person, end=', ')
        count = 1

# 마지막 남은 1개는 쉼표 없이 '>'만 붙여서 마무리!
print(queue.popleft(), end='>')