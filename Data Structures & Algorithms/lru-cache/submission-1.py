class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int: 
        if self.hashMap.get(key, None) is None:
            return -1
        else:
            curr = self.hashMap.get(key)
            prev = curr.prev
            nxt = curr.next
            prev.next = nxt
            nxt.prev = prev

            headNxt = self.head.next
            curr.prev = self.head
            curr.next = headNxt
            self.head.next = curr
            headNxt.prev = curr
            self.hashMap[key] = curr
            return curr.data

    def put(self, key: int, value: int) -> None:
        if self.hashMap.get(key, None) is not None:
            curr = self.hashMap.get(key)
            curr.data = value

            self.get(key)
        else:
            newNode = Node(data=value, key=key)
            headNxt = self.head.next
            newNode.prev = self.head
            newNode.next = headNxt
            headNxt.prev = newNode
            self.head.next = newNode
            self.hashMap[key] = newNode

        if len(self.hashMap) > self.capacity:
            nodeForDelete = self.tail.prev
            key = nodeForDelete.key
            prevNode = nodeForDelete.prev
            self.tail.prev = prevNode
            prevNode.next = self.tail
            del self.hashMap[key]
        

class Node:
    def __init__(self, next=None, prev=None, key=None, data=None):
        self.key = key
        self.next = next
        self.prev = prev
        self.data = data