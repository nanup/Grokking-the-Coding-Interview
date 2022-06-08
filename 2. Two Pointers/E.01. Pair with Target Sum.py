def pair_with_targetsum(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]

        if sum < target:
            left += 1

        if sum > target:
            right -= 1

        else:
            break

    return [left, right]

def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))


main()

# time: O(N)
# space: O(1)