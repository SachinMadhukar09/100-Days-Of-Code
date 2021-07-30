class Myhash:
    def __init__(self,c):
        self.cap=c
        self.table=[-1]*c
        self.size=0
    def hash(self,x):
        return x%self.cap
    def search(self,x):
        h=self.hash(x)
        t=self.table
        i=h
        while t[i]!=-1:
            if t[i]==x:
                return True
            i=(i+1)% self.cap
            if i==h:
                return False
            return False
    def insert(self,x):
        i=self.hash(x)
        t=self.table
        if self.cap==self.size:
            return False
        if self.search(x)==True:
            return False
        while t[i] not in (-1,-2):
            i=(i+1)%self.cap
        t[i]=x
        self.size+=1
        return True
    def delete(self, x):
        t=self.table
        h=self.hash(x)
        i=h
        while t[i]!=1:
            if t[i]==x:
                t[i]=-2
                return True
            i=(i+1)%self.cap
            if i==h:
                return False
        return False    
        
            
m=Myhash(7)
m.insert(43)
m.insert(49)
m.insert(53)
m.insert(56)
m.insert(64)
m.insert(23)
m.delete(43)

