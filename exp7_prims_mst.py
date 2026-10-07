INT_MAX = float("inf")


def min_key(key, mst_set, V):
    min_val = INT_MAX
    min_index = -1
    for v in range(V):
        if not mst_set[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v
    return min_index


def prim_mst(graph, V):
    parent = [-1] * V           # stores constructed MST
    key = [INT_MAX] * V         # min weight edge used to pick next vertex
    mst_set = [False] * V       # vertices already in the MST

    key[0] = 0                  # start from vertex 0
    parent[0] = -1              # root of MST

    for _ in range(V - 1):
        u = min_key(key, mst_set, V)
        mst_set[u] = True

        for v in range(V):
            if graph[u][v] and not mst_set[v] and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]

    print("Edge \tWeight")
    total = 0
    for i in range(1, V):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")
        total += graph[i][parent[i]]
    print("Total weight of MST:", total)


if __name__ == "__main__":
    V = int(input("Enter number of vertices: "))
    print("Enter weighted adjacency matrix (0 = no edge):")
    graph = [list(map(int, input().split())) for _ in range(V)]
    prim_mst(graph, V)
