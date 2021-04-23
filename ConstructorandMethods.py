class Mobile:
    def __init__(self,**kwargs):
        print(kwargs)
        self.diallist=kwargs
    def __str__(self):
        return "Hi buddy"
    def Dial(self):
        for name,num in self.diallist.items():
            if(str(num)=="54321"):
                print(name)
mano=Mobile(Mano=12345,mani=54321)
mano.Dial()
print(mano)
