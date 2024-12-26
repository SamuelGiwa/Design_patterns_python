class Singleton:
    __instance = None
    
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
            
        return Singleton.__instance
    
    def __init__(self):
        
        print("the value is  " , Singleton.__instance)
        
        if Singleton.__instance != None:
            raise Exception("Singleton exists already!")
        else:
            Singleton.__instance = self
    

s3 = Singleton()
#s1 = Singleton.getInstance()
#s2 = Singleton.getInstance()
