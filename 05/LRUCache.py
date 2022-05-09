
class LRUCache:

    def __init__(self, limit=42):
        # Храним ключ-значение
        self.cache = {}
        # Храним порядок
        self.priority = []
        # Храним максимальное количество значений
        self.limit = limit

    def get(self, key):
        if key not in self.cache:
            return None
        self.priority.remove(key)
        self.priority.append(key)
        return self.cache[key]

    def set(self, key, value):
        self.cache[key] = value
        self.priority.append(key)
        if len(self.cache) > self.limit:
            self.cache.pop(self.priority[0])
            self.priority.pop(0)
