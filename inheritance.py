class Samsung:
    def __init__(self):
        print("i am Samsung")
        
    def makeScreen(self):
        print("i make screen")
    def test(self):
        print("Screen test 1: OK")
        print("Screen test 2: OK")
        print("Screen test 3: OK")
        
class Iphone(Samsung):
    def __init__(self):
        print("i am iphone")
        super().__init__()
    def a3chips(self):
        print("i make iphone 3 chips")
        
    def itest(self):
        print("A3 test: OK")
        #super().test()
        
user = Iphone()

user.a3chips()
user.makeScreen()
user.itest()