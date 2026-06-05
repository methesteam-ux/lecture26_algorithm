from collections import deque

N = int(input())
queue = deque()

# 1. 1부터 N까지 카드 채우기
for i in range(1, N + 1):
    queue.append(i)

# 2. 카드가 1개 남을 때까지 반복
while len(queue) > 1:
    # 첫 번째 카드는 그냥 버리기 (출력 안 함)
    queue.popleft()
    
    # 그다음 카드는 꺼내서 다시 뒤로 보내기
    person = queue.popleft()
    queue.append(person)

# 3. 마지막으로 남은 딱 한 장만 출력
print(queue.popleft())