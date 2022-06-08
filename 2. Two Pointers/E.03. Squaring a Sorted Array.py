def make_squares(arr):
    left, right = 0, len(arr) - 1
    index = len(arr) - 1
    newArr = [0 for x in range(len(arr))]

    while left <= right:
        leftS = arr[left] * arr[left]
        rightS = arr[right] * arr[right]

        if leftS > rightS:
            newArr[index] = leftS
            left += 1
        else: 
            newArr[index] = rightS
            right -= 1

        index -= 1

    return newArr

def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()

# time: O(N)
# space: O(N)