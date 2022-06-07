import math

def smallest_subarray_with_given_sum(s, arr):
    windowSum, windowStart, minLength = 0, 0, math.inf

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        while windowSum >= s:
            windowSum -= arr[windowStart]
            minLength = min(minLength, windowEnd - windowStart + 1)
            windowStart += 1

    if minLength == math.inf:
        return 0

    return minLength

def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()

#time: O(N)
#space: O(1)