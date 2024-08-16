import ctypes 

class MeraList:

    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array__(self.size)
        
    
    #find a len of List
    def __len__(self):
        return self.n
    
    
    #append add a value adds it at the end of list
    def append(self,item):
        
        if self.n == self.size:
            #it's return double array old_array*2 
            self.__resize(self.size*2)
            
        self.A[self.n] = item
        self.n += 1
        
    def __getitem__(self,index):
        #find a element based on index
        if 0<= index < self.n:
            return self.A[index]
        else:
            return "Indexing Error"
        
        
    def pop(self):
        #Delete an element from the last item in the list.
        if self.n == 0 :    
            return 'Empty List'
            
        else:
            self.n = self.n - 1
            return  self.n
        
    def clear(self):
        #reset Array size / number
        self.n = 0
        self.size = 1
        
        
        
    def find(self,item):
        #find a item & Return a index of specfic item where is place
        for i in range(self.n):
            #time complexity O(n) "Linear"
            if self.A[i] == item:
                return i
        return "ValueError Item not find"    
            
            
            
    def __resize(self,new_capactiy):
        #make a new array double size with old data
        B = self.__make_array__(new_capactiy)
        self.size = new_capactiy
        # copy the content into A to B:-
        
        for i in range(self.n):
            #time complexity O(n) "Linear"
            B[i] = self.A[i]
        
        self.A = B
        
        
    def insert(self,pos,item):
        if 0<= pos< self.n:
            if self.n == self.size:
                self.__resize(self.size*2)
    
            for i in range(self.n,pos,-1):
                self.A[i] = self.A[i-1]
            
            self.A[pos] = item
            self.n = self.n+1
            
        else:
            return "IndexError"
        
        
    def __delitem__(self,pos):
        
        for i in range(pos,self.n-1):
            self.A[i] = self.A[i+1]
        
        self.n = self.n-1
        
    
    def remove(self,item):
        pos = self.find(item)
        
        if type(pos) == int:
            #delete
            self.__delitem__(pos)
        else:
            return pos
        
    def sort(self):
        for i in range(self.n):
            for j in range(0,self.n-i-1):
                #using bubble sorting
                
                if self.A[j] > self.A[j+1]: #5 / 2
                    self.A[j],self.A[j+1] = self.A[j+1] ,self.A[j]
                    
        return self.A
        
            
    
    def __str__(self):
        
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) +','
                
        return '[' + result[:-1] +   ']'
    
    
    def __make_array__(self,capacity):
        return (capacity*ctypes.py_object)()
                
    
l = MeraList()

l.append(5)
l.append(4)
l.append(3)


l.insert(1,100)
l.sort()

print(l)





    
    