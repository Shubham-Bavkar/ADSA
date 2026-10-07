def merge_sort(A, lb, ub):
    if lb < ub:
        mid = (lb + ub) // 2
        merge_sort(A, lb, mid)
        merge_sort(A, mid + 1, ub)
        merge(A, lb, mid, ub)


def merge(A, lb, mid, ub):
    B = [0] * len(A)          # auxiliary array
    i, j, k = lb, mid + 1, lb

    while i <= mid and j <= ub:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1

    while i <= mid:
        B[k] = A[i]
        i += 1
        k += 1

    while j <= ub:
        B[k] = A[j]
        j += 1
        k += 1

    for k in range(lb, ub + 1):
        A[k] = B[k]


if __name__ == "__main__":
    A = list(map(int, input("Enter array elements (space separated): ").split()))
    print("Original array:", A)
    merge_sort(A, 0, len(A) - 1)
    print("Sorted array  :", A)
