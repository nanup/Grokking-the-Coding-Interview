def cyclic_sort(nums):
    i = 0
    while i < len(nums):
      j = nums[i] - 1
      if nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]  # swap
      else:
        i += 1
    return nums

# time: O(N)
# space: O(1)

def main():
    nums = [1, 5, 6, 4, 3, 2]
    newnums = cyclic_sort(nums)
    print(newnums)

main()