# a=5
# print(id(a))
# x=100
# y=100
# isT =x is y
# print("地址相同"+str(isT))
# a =[1,2,3]
# b=a[:]#a的切片
# print(a is b)
# b.append(4)
# print(b)
class Linux_version:

    def __init__(self,name,company):
        self.name =name
        self.company =company
    def info(self):
        print(f"name:{self.name},company:{self.company}")
            
linux1=Linux_version("Ubuntu","Canonical")
linux2=Linux_version("Fedora","RedHat")
linux1.info()
linux2.info()
        
    
class BankAccount:
    def __init__(self,owner,balance =0):
        self.owner =owner
        self._balance = balance
    def deposit(self,amount):
        if(amount>0):
            self._balance+=amount
            print(f"{self.owner} 存入 {amount} 元，当前余额是 {self._balance}元.")
        else:
            print("存款金额必修大于0")
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{self.owner} 取出 {amount} 元，当前余额是 {self._balance}元.")
        else:
            print("金额不可用或必须大于 0.")
usa_bank =BankAccount("Lee",1000)
usa_bank.deposit(500)
usa_bank.withdraw(200)

class animals:
    def __init__(self,type,age):
        self.type =type
        self.age =age
    def info(self):
        print(f"种类:{self.type},{self.age}")    
cat =animals("cat",9)
cat.info()            
                       
        
