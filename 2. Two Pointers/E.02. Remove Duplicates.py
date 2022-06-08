def remove_duplicates(arr):
    left, right = 1, 1

    while right < len(arr):
        if arr[left - 1] != arr[right]:
            arr[left] = arr[right]
            left += 1
        right += 1

    return left

def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()

# time: O(N)
# space: O(1)