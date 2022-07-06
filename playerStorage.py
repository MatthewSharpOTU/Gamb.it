class HashTable:
    def __init__(self):
        self.MAX = 10
        self.tbl = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash%self.MAX
    
    def __setitem__(self, key, val):       
        h = self.get_hash(key)
        found = False
        for i, element in enumerate(self.tbl[h]):
            if len(element)==2 and element[0]==key:
                self.tbl[h][i] = (key,val)
                found = True
                break
        if not found:
            self.tbl[h].append((key,val))
        
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.tbl[h]:
            if element[0]==key:
                return element[1]
        return None
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for i, element in enumerate(self.tbl[h]):
            if element[0]==key:
                del self.tbl[h][i]

