class Account:
    def __init__(self,name):
        self.name = name
    
    def info(self):
        print(f"hey {self.name} what is your occupation")

a = Account("Vivek")
a.info()