
def solve(pos, n, graph, path):
    
    if pos == n:
        if graph[path[n - 1]][path[0]] == 1:
            print("Hamiltonian cycle:", *path, path[0])
            return True
        return False

    for v in range(1, n):
        if graph[path[pos - 1]][v] == 1 and v not in path:
            path[pos] = v
            if solve(pos + 1, n, graph, path):
                return True
            path[pos] = -1                      # backtrack
    return False


def hamiltonian(n, graph):
    path = [-1] * n
    path[0] = 0
    if not solve(1, n, graph, path):
        print("No Hamiltonian cycle exists.")


if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    print("Enter adjacency matrix (row by row, space separated):")
    graph = [list(map(int, input().split())) for _ in range(n)]
    hamiltonian(n, graph)
