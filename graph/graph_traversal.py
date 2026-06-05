from collections import deque

class Graph:
    def __init__(self):
        num_nodes, num_edeges = map(int, input().split())
        self.directed = int(input("양방향 여부 (1:양방향, 0:단방향) : "))
        self.graph = [[] for _ in range(num_nodes + 1)]
        for _ in range(num_edeges):
            u, v = map(int, input().split())
            self.graph[u].append(v)
            if self.directed:
                self.graph[v].append(u)

    def dfs(self, node, visited=[]):
        print(node, end=" ")
        visited.append(node)
        for adj_node in self.graph[node]:
            if adj_node not in visited:
                self.dfs(adj_node)

    def bfs(self, start):
        visited = []
        queue = deque()
        # 시작 노드에 대해 작업
        queue.append(start)
        visited.append(start)
        print(start, end=" ")
        # 다음에 방문할 노드 찾아서 처리
        # 방문한 노드를 찾을 노드를 queue에서 가져와서 찾기
        while queue:
            prev_node = queue.popleft()
            for node in self.graph[prev_node]:
                if node not in visited:
                    queue.append(node)
                    visited.append(node)
                    print(node, end=" ")

if __name__ == "__main__":
    g = Graph()
    start = int(input("시작 노드 번호 : "))
    g.dfs(start)
    print()
    g.bfs(start)