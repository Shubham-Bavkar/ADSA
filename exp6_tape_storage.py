def optimal_storage_on_tape(length):
    n = len(length)

    # Sort ascending (selection-style exchange sort, as in the pseudocode)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if length[i] > length[j]:
                length[i], length[j] = length[j], length[i]

    total = 0
    retrieval = 0
    for i in range(n):
        retrieval += length[i]      # time to reach end of file i
        total += retrieval

    average = total / n
    return length, total, average


if __name__ == "__main__":
    n = int(input("Enter number of files: "))
    length = [int(input(f"Enter length of file {i + 1}: ")) for i in range(n)]

    order, total, average = optimal_storage_on_tape(length)

    print("Optimal order          :", order)
    print("Total Retrieval Time   :", total)
    print("Average Retrieval Time :", round(average, 2))
