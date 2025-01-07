####################
# stack with list

s = []
# push(data: any)
s.append("a")
s.append("b")
# peek()
assert "b" == s[-1]
# pop()
assert "b" == s.pop()
assert "a" == s.pop()
assert len(s) == 0

print("Done")


####################
# stack with Collections.deque
from collections import deque

s = deque()
# push(data: any)
s.append("a")
s.append("b")
# peek()
assert "b" == s[-1]
# pop()
assert "b" == s.pop()
assert "a" == s.pop()
assert len(s) == 0

print("Done")


####################
# stack with singly linked list

class Node:
    value: any
    next  #: Node

    def __init__(self, value: any):
        self.value = value
        self.next = None


class Stack:
    head: Node

    def __init__(self):
        self.head = None

    def push(self, value: any) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def peek(self) -> any:
        if self.head is None:
            return None
        return self.head.value

    def pop(self) -> any:
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value


s = Stack()
# push(data: any)
s.push("a")
s.push("b")
# peek()
assert "b" == s.peek()
# pop()
assert "b" == s.pop()
assert "a" == s.pop()
assert s.head is None

print("Done")
