v , e = map(int, input().split())
edges = dict()
for i in range(v):
    edges[i] = list()
for i in range(e):
    v1 , v2 = map(int, input().split())
    edges[v1].append(v2)
    edges[v2].append(v1)
queue = list()
queue.append(1)
visited = [False for i in range(v)]
#visited[1] = True
previous = dict
while(len(queue) > 0):
    vertex = queue.pop(0)
    if not visited[vertex]:
        for vertices in edges[vertex]:
            queue.append(vertices)
        visited[vertex] = True
        print(vertex, end='') 
