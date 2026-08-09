class MyHashSet:

    def __init__(self):
        self.my_list = []

    def add(self, key: int) -> None:
        self.my_list.append(key)

    def remove(self, key: int) -> None:
        self.my_list = [num for num in self.my_list if num != key]

    def contains(self, key: int) -> bool:
        for num in self.my_list:
            if num == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)