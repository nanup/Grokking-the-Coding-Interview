class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


# def find_middle_of_linked_list(head):
#   length = 0
#   pointer1, pointer2 = head, head

#   while pointer1:
#       pointer1 = pointer1.next
#       length += 1
#   if length == 0:
#       return None
#   else:
#     mid_length = (length // 2)

#   while mid_length > 0:
#       pointer2 = pointer2.next
#       mid_length -= 1

#   head = pointer2

#   return head

################################################

def find_middle_of_linked_list(head):
    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# time: O(N)
# space: O(1)


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next = Node(6)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next.next = Node(7)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))


main()