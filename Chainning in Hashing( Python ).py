#chainning in hashing-
#chaining- 1st method of collision handeling.
#IDEA- WE MAINTAIN A ARRAY OF LINKED LIST.
#hash(key)=key%7
#program for myhash..
class MyHash:
    def__init__(self,b):
    self.bucket=b
    self.table=[[] for x in range(b)]

    def insert(self,x):
        i=x%self.bucket
        self.table[i].append(x)

def remove(self,x):
        i=x%self.bucket
        self.table[i].remove(x)
        




    def search(self,x):
        i=x%self.bucket
        return x in self.table[i]
