def find_missing_number(arr):
    i = 0
    while i < len(arr):
        j = arr[i]
        if arr[i] < len(arr) and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    for i in range(len(arr)):
        if arr[i] != i:
            return i

    return len(arr)

def main():
  print(find_missing_number([4, 0, 3, 1]))
  print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()