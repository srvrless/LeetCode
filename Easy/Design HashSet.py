class MyHashSet:

    def __init__(self):
        self.dick = []

    def add(self, key: int) -> None:
        if key not in self.dick:
            self.dick.append(key)

    def remove(self, key: int) -> None:
        if key in self.dick:
            self.dick.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.dick:
            return True
        return False