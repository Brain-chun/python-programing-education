import heapq
import sys

input = sys.stdin.readline
INF =int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[INF] for _ in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        #최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있으면 무시
        if distance[now] < dist:
            continue
        
dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])
