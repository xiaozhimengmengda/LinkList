# 单链表
class SingleNode:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __repr__(self):
        return repr(self.item)


class LinkList:
    def __init__(self):
        self.head = None
        self.tailf = None
        self.size = 0

    def add(self, item):
        node = SingleNode(item)
        if self.head is None:
            self.head = node
        else:
            self.tailf.next = node
        self.tailf = node

    def iternodes(self):
        current = self.head
        while current:
            yield current
            current = current.next


class LinkList2:
    def __init__(self):
        self.head = None
        self.tailf = None
        self.items = []

    def addend(self, item):
        node = SingleNode(item)
        if self.head is None:
            self.head = node
        else:
            self.tailf.next = node
        self.tailf = node
        self.items.append(node)

    def iternodes(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def getitem(self, index):
        return self.items[index]

ll = LinkList()
ll.add('abc')
ll.add(1)
ll.add(2)

print(ll.head, ll.tailf)
for x in ll.iternodes():
    print(x)

# 双链表

class SingleNode:
    def __init__(self, item, prev=None, next=None):
        self.item = item
        self.next = next
        self.prev = prev

    def __repr__(self):
        return repr(self.item)


class LinkList3:
    def __init__(self):
        self.head = None
        self.tailf = None
        self.size = 0

    def addend(self, item):
        node = SingleNode(item)
        if self.head is None:
            self.head = node
        else:
            self.tailf.next = node
            node.prev = self.tail
        self.tailf = node

    def insert(self, index, item):
        if index < 0:
            raise ValueError('Error Index{}'.format(index))
        current = None
        for i, node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        if current is None:
            self.append(item)
            return

        node = SingleNode(item)
        prev = current.prev
        if prev is None:
            self.head = node
        else:
            prev.next = node
        node.next = current
        current.prev = node

    def pop(self):
        if self.tail is None:
            raise Exception('Empty')
        node = self.tailf
        item = node.item
        prev = node.prev

        if prev is None:
            self.head = None
            self.tailf = None
        else:
            prev.next = None
            self.tailf = prev
        return item

    def remove(self, index):
        if self.tail is None:
            raise Exception('Empty')
        if index < 0:
            raise  ValueError('error index {]'.format(index))
        current = None
        for i, node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        if current is None:
            raise ValueError('error index {}.Out of boundary'.format(index))
        prev = current.prev
        next = current.nect

        if prev is None and next is None:
            self.head = None
            self.tailf = None
        elif prev is None:
            self.head = next
            next.prev = None
        elif next is None:
            self.tailf = prev
            prev.next = None
        else:
            prev.next = next
            next.prev = prev
        del current

    def iternodes(self, reverse=False):
        current = self.tailf if reverse else self.head
        while current:
            yield current
            current = current.prev if reverse else current.next

    def getitem(self, index):
        return self.items[index]
