def dutch_flag_sort(arr):
    left, right = 0, len(arr) - 1

    i = 0

    while i < right:
        if arr[i] == 0:
            arr[i], arr[left] = arr[left], arr[i]
            i += 1
            left += 1

        elif arr[i] == 1:
            i += 1

        else:
            arr[i], arr[right] = arr[right], arr[i]
            high -= 1

