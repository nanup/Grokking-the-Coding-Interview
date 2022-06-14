import array


def find_smallest_missing_positive_number(arr):
    i = 0

    while i < len(arr):
        j = arr[i] - 1

        if 0 <= arr[i] < len(arr) and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    for i in range(len(arr)):
        if arr[i] != i + 1:
            return (i + 1)

print(find_smallest_missing_positive_number([3, 2, 5, 1]))