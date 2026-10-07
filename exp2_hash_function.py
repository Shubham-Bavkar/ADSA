def hash_function(key, M):
    if isinstance(key, int):
        return key % M

    if isinstance(key, str):
        h = 0
        R = 31
        for ch in key:
            h = (h * R + ord(ch)) % M
        return h

    raise TypeError("Key must be an integer or a string")


if __name__ == "__main__":
    M = int(input("Enter table size M: "))
    n = int(input("Enter number of keys: "))

    table = [[] for _ in range(M)]   # chaining to show where keys land

    for _ in range(n):
        raw = input("Enter key: ").strip()
        key = int(raw) if raw.lstrip("-").isdigit() else raw
        idx = hash_function(key, M)
        table[idx].append(key)
        print(f"  hash({key!r}) = {idx}")

    print("\nHash table:")
    for i, bucket in enumerate(table):
        print(f"  [{i}] -> {bucket}")
