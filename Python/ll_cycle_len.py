#!/usr/bin/python3

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def cycle(head):
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return cycle_len(slow)
    return 0

def cycle_len(slow):
    current = slow
    cycle_len = 0
    while True:
        current = current.next
        cycle_len += 1
        if current == slow:
            break
    return cycle_len

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle length: " + str(cycle(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle length: " + str(cycle(head)))


main()
