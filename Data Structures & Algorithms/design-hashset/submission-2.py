class MyHashSet:

    def __init__(self):
        self.data = {}

    def add(self, key: int) -> None:
        if self.data.get(key, None) is None:
            self.data[key] = key

    def remove(self, key: int) -> None:
        if self.data.get(key, None) is not None:
            del self.data[key]
        

    def contains(self, key: int) -> bool:
        if self.data.get(key, None) is not None:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)