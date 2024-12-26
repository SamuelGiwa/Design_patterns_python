class Singleton:
    __instance = None
    
    def __new__(cls, name=None):
        if (cls.__instance is None):
            
            cls.__instance = \
                super(Singleton, cls).__new__(cls)
            cls.__instance.name_ =  name 
                
        return cls.__instance      

#s1 = Singleton("bolu")
# print(s1)

s2 = Singleton()
print(s2.name_)