def fruits_into_baskets(arr):
    windowStart, count, maxFruits = 0, 0, 0

    for windowEnd in range(len(arr)):
        if arr[windowEnd] not in arr[windowStart: windowEnd]:
            count += 1

        while count > 2:
            if arr[windowStart] not in arr[windowStart + 1: windowEnd]:
                count -= 1
            windowStart += 1

        maxFruits = max(maxFruits, windowEnd - windowStart + 1)

    return maxFruits
       
def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()

#time: O(N)
#space: O(1)