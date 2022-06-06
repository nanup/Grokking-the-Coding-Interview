def max_sum_subarray_of_size_k(arr, k):

    maxWindowSum, windowSum, windowStart = 0, 0, 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] #addig elements of a subarray

        if windowEnd >= k:
            windowSum -= arr[windowStart] #sliding the window
            windowStart += 1
            maxWindowSum = max(maxWindowSum, windowSum)

    return maxWindowSum

def main():
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    print("The maximum sum of subarray of size " + str(k) + " is " + str(max_sum_subarray_of_size_k(arr, k)))

main()

#time: O(N)
#space: O(1)