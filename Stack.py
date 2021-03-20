# Something about stack
class Node:
    def __init__(self, value):
        self.value = value
        self.head = None

    def __str__(self):
        return self.value


class Stack:
    def __init__(self):
        self.node = None
        self.size = 0

    def add(self, node):
        if not self.node:
            self.node = node
        else:
            node.head = self.node
            self.node = node
        self.size += 1

    def pop(self):
        if not self.node:
            return None
        else:
            if self.size > 0:
                node = self.node
                self.node = node.head
                self.size -= 1
                return node
            else:
                self.node = None
                return None


def test_stack():
    print('Testing Stack Function ...')
    a, b, c, d = Node('a'), Node('b'), Node('c'), Node('d')
    stack = Stack()
    stack.add(a)
    stack.add(b)
    stack.add(c)
    stack.add(d)
    try:
        assert stack.node.value == 'd'
        assert stack.pop().value == 'd'
        assert stack.pop().value == 'c'
        print('Test pass!')
    except Exception as e:
        print('Test failed')
        print(e)


test_stack()
