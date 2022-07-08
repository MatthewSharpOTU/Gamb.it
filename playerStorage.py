'''
Class Function "HashTable" which is used to update and keep track of a user's 'bank account'
'''

class HashTable:
    def __init__(self):
        self.MAX = 10                               # Maximum number of instances in the hash table
        self.tbl = [[] for i in range(self.MAX)]    # Hash Table that uses linear listing

    def get_hash(self, key):                        # Gets the corresponding hash indices 
        hash = 0                
        for char in key:
            hash += ord(char)
        return hash%self.MAX                        # hash index is based off of the max instances in the hash table                        
    
    def __setitem__(self, key, val):                # Sets the current bank account of a specific user    
        h = self.get_hash(key)                      # Calls to find the hash value
        found = False
        for i, element in enumerate(self.tbl[h]):   # Goes through the linear listing of that index and find the corresponding key
            if len(element)==2 and element[0]==key:
                self.tbl[h][i] = (key,val)          # Update key's value
                found = True
                break
        if not found:
            self.tbl[h].append((key,val))           # If key does not exist yet, append it to the end of the linked list
        
    def __getitem__(self, key):                     # Finds the valye of a specific bank user
        h = self.get_hash(key)
        for element in self.tbl[h]:
            if element[0]==key:
                return element[1]
        return None
    
    def __delitem__(self,key):                      # Deletes a bank user's information from the database
        h = self.get_hash(key)
        for i, element in enumerate(self.tbl[h]):
            if element[0]==key:
                del self.tbl[h][i]

