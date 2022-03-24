import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 갯수 간선의 갯수 입력받기
n, m = map(int, input().split())
#시작 노드 번호 입력
start = int(input())
#노드 정보에대한 리스트 만들기
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

#간선 정보 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_val = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    #시작 노드를 제외한 노드 반복
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
        
