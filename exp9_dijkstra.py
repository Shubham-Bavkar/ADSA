
INF = float('inf')


def dijkstra(graph, source, n):
    distance = [INF] * n
    visited = [False] * n

    distance[source] = 0

    for _ in range(n):
        # pick the unvisited vertex with minimum distance
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or distance[i] < distance[u]):
                u = i

        # no more reachable vertices
        if u == -1 or distance[u] == INF:
            break

        visited[u] = True

        # relax edges going out of u
        for v in range(n):
            if (not visited[v] and graph[u][v] != 0
                    and distance[u] + graph[u][v] < distance[v]):
                distance[v] = distance[u] + graph[u][v]

    return distance


def main():
    n = int(input("Enter number of vertices: "))

    print("Enter weighted adjacency matrix (row by row, 0 = no edge):")
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    source = int(input("Enter source vertex: "))

    distance = dijkstra(graph, source, n)

    print("Vertex \tDistance from source")
    for i in range(n):
        d = distance[i] if distance[i] != INF else "INF"
        print(f"{i} \t{d}")


if __name__ == "__main__":
    main()