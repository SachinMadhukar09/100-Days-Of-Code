class Myhash:
    def __init__(self,b):
        self.Bucket=b
        self.table=[[] for x in range(b)]
    def insert(self,x):
        i=x%self.Bucket
        self.table[i].append(x)
    def remove(self,x):
        if x in self.table:    
            i=x%self.Bucket
            self.table[i].remove(x)
        else:
            return (x,"is not present")
    def search(self,x):
        i=x%self.Bucket
        return x in self.table[i]
    
m=Myhash(7)
m.insert(23)
m.remove(22)



