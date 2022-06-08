def search_triplets(arr):
    arr.sort()

    triplets = []

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]: #skip element to avoid dups
            continue

        search_pair(arr, -arr[i], i + 1, triplets)

    return triplets

def search_pair(arr, target, left, triplets):
    right = len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]
        if target == sum:
            triplets.append([-target, arr[left], arr[right]])
            left += 1
            right -= 1

            while left < right and arr[left] == arr[left - 1]:
                left += 1

            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        elif target > sum:
            left += 1
        else:
            right -= 1

def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()

# time: O(N^2)
# space: O(N)