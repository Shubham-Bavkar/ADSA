INF = float("inf")


def floyd_warshall(graph, n):
    dist = [row[:] for row in graph]        # copy of the input matrix

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (dist[i][k] != INF and dist[k][j] != INF
                        and dist[i][k] + dist[k][j] < dist[i][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def display(dist, n):
    print("Shortest distance matrix:")
    for i in range(n):
        print(" ".join("INF".rjust(4) if dist[i][j] == INF else str(dist[i][j]).rjust(4)
                       for j in range(n)))


if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    print("Enter adjacency matrix (use INF for no edge):")
    graph = []
    for _ in range(n):
        row = [INF if x.upper() == "INF" else int(x) for x in input().split()]
        graph.append(row)

    display(floyd_warshall(graph, n), n)
