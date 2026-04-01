class MyHashMap:

    def __init__(self):
        self.check = set()
        self.counter = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.check.add(key)
        self.counter[key] = value

    def get(self, key: int) -> int:
        return self.counter[key]

    def remove(self, key: int) -> None:
        if key in self.check:
            self.check.remove(key)
        self.counter[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)