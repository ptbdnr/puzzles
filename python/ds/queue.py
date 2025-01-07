####################
# queue with list

q = []

# enqueue(data: any)
q.append("a")
q.append("b")
# dequeue()
assert "a" == q.pop(0)
assert "b" == q.pop(0)
assert len(q) == 0

print("Done")


####################
# queue with singly linked list


class Node:
    value: any
    next  #: Node

    def __init__(self, value: any):
        self.value = value
        self.next = None


class Queue:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value: any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def dequeue(self) -> any:
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value


q = Queue()
# enqueue(data: any)
q.enqueue("a")
q.enqueue("b")
# dequeue()
assert "a" == q.dequeue()
assert "b" == q.dequeue()
assert q.head is None

print("Done")
