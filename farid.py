class car:
    def __init__(self,qiymet,mator):
        self.qiymet=qiymet
        self.mator=mator
    def start(self):
        print("mawin ise duwdu")



class bmw(car):
    print("bmw iwe duwdu")
b=car(20,6.3)
a=bmw(15,6.3)
a.attr=5
print(a.start())
    
    