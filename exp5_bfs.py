MAX = 100
queue = [0] * MAX
front = -1
rear = -1
visited = [0] * MAX


def enqueue(vertex):
    global front, rear
    if rear == MAX - 1:
        return                      # queue full
    if front == -1:
        front = 0
    rear += 1
    queue[rear] = vertex


def dequeue():
    global front, rear
    if front == -1:
        return -1                   # queue empty
    vertex = queue[front]
    if front >= rear:
        front = -1
        rear = -1
    else:
        front += 1
    return vertex


def bfs(graph, start_vertex, vertices):
    for i in range(vertices):
        visited[i] = 0

    enqueue(start_vertex)
    visited[start_vertex] = 1

    print("BFS Traversal:", end=" ")
    while front != -1:
        current = dequeue()
        print(current, end=" ")
        for i in range(vertices):
            if graph[current][i] == 1 and visited[i] == 0:
                enqueue(i)
                visited[i] = 1
    print()


if __name__ == "__main__":
    vertices = int(input("Enter number of vertices: "))

    print("Enter adjacency matrix (row by row, space separated):")
    graph = [list(map(int, input().split())) for _ in range(vertices)]

    start = int(input("Enter start vertex: "))
    bfs(graph, start, vertices)
