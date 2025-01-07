class Node:
    value: any
    next  #: Node

    def __init__(self, value: any):
        self.value = value
        self.next = None


n = Node("a")
assert n.value == "a"
n.next = Node("b")

while n is not None:
    n = n.next
print("Done")
