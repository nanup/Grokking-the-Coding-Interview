def longest_substring_with_k_distinct(str, k):
    windowStart, maxLength, count = 0, 0, 0

    str = list(str)

    for windowEnd in range(len(str)):
        if str[windowEnd] not in str[windowStart: windowEnd]:
            count += 1

        while count > k:
            if str[windowStart] not in str[windowStart + 1: windowEnd]:
                count -= 1
            windowStart += 1

        maxLength = max(maxLength, windowEnd - windowStart + 1)

    return maxLength

def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))

main()

#time: O(N)
#space: O(1)