# def find_happy_number(num):
#     sum_list = []
#     sum = square_sum(num)
#     while sum != 1:
#         sum_list.append(sum)
#         new_sum = square_sum(sum)

#         if new_sum in sum_list:
#             return False
#         else:
#             sum = new_sum

#     return True

# def square_sum(num):
#     sum = 0
#     for i in range(len(str(num))):
#         sum += int(str(num)[i]) ** 2

#     return sum

########################################################

def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = square_sum(slow)
        fast = square_sum(square_sum(fast))
        if slow == fast:
            break
    
    return slow == 1

def square_sum(num):
    _sum = 0
    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num //= 10

    return _sum


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()