class a:
    def a(self):
        print("Inside A")
class b(a):
    def b(self):
        print("Inside B")
class c(b):
    def c(self):
        print("Inside C")

cc=c()
cc.a()
cc.b()
cc.c()
