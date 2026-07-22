class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt =None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache={}
        self.old =Node(0,0)
        self.new =Node(0,0)
        self.old.nxt = self.new
        self.new.prev = self.old

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1
    def remove(self, node):
        prev, next = node.prev , node.next
        prev.next = next
        next.prev = prev

    def add(self, node):
        prev, next = self.new.prev, self.new
        prev.next = next.prev = node
        node.prev = prev
        node.next = next

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.add(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.old.next
            self.remove(lru)
            del self.cache[lru.key]

        
