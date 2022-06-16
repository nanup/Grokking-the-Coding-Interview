from __future__ import print_function
from cgi import FieldStorage
from xml.etree.ElementTree import TreeBuilder


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_every_k_elements(head, k):
  if k <= 1 or head is None:
    return head

  previous, current= None, head
  while True:
    first_node_of_sublist = previous
    last_node_of_sublist = current
    next = None
    i = 0
    while current and i < k:
      next = current.next
      current.next = previous
      previous = current
      current = next
      i += 1
    
    if first_node_of_sublist is not None:
      first_node_of_sublist.next = previous
    else:
      head = previous

    last_node_of_sublist.next = current

    if current is None:
      break
    previous = last_node_of_sublist

  return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_every_k_elements(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()