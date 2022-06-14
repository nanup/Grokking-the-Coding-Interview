def find_corrupt_pair(arr):
    i = 0

    while i < len(arr):
        j = arr[i] - 1

        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

        else:
            i += 1

    print(arr)

    for i in range(len(arr)):

        if arr[i] != i + 1:
            return [arr[i], i + 1]

    return [-1, -1]

print(find_corrupt_pair([3, 1, 2, 3, 6, 4]))

    