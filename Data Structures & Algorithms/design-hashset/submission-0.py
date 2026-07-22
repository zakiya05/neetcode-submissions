class MyHashSet:

    def __init__(self):
        self.d={}
    def add(self, key: int) -> None:
        self.d[key]=self.d.get(key,0)+1

    def remove(self, key: int) -> None:
        if self.d.get(key,-1)!=-1:
            del self.d[key]

    def contains(self, key: int) -> bool:
        if self.d.get(key,-1)!=-1:
            return True 
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)