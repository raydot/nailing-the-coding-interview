def permute(arr):
    result = []
    n = len(arr)
    c = [0] * n  # Initialize the counter array
    result.append(arr.copy())

    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]  # Swap for even index
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]  # Swap for odd index
            result.append(arr.copy())
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

    return result

animals = ["lion", "tiger", "bear", "dog", "guppy"]
permutations = permute(animals)

for perm in permutations:
    print(perm)