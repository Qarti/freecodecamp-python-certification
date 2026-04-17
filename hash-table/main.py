class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key: str) -> int:
        return sum([ord(char) for char in key])

    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            self.collection[hashed_key].update({key: value})  
        else:
            self.collection[hashed_key] = {key:value}
        pass

    def remove(self, key):
        hashed_key = self.hash(key)

        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]
        

    def lookup(self, key):
        hashed_key = self.hash(key)

        try:
            return self.collection[hashed_key][key]
        except KeyError:
            return None
