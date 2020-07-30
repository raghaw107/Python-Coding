class Phone:
    phone_version = "s10"
    brand_name = "Samsung"
    user_name = ""
    
    model = "s10+"
	
    def get_model(self):
        return self.model
    
    def set_model(self, val):
        self.model = "s10+, " + val
        
    #constructor    
    def __init__(self,user):
        self.user_name = user
        
    def Bootlogo(self):
        print("Samsung",self.phone_version)
        
hitesh = Phone("hitest_phone")
#hitesh.phone_version = "iphone x8 Series"
#hitesh.model = "iphone"
#hitesh.Bootlogo()
print(hitesh.get_model())
hitesh.set_model("iphone")