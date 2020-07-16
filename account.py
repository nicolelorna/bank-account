class BankAccount:
  bank = "KCB"
  
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    self.balance = 0
    
  def account_name(self):
    name = "{} account for {} {}". format(self.bank, self.first_name, self.last_name)
    return name

  def withdraw(self,amount):
        self.balance += amount
        if amount >0:
          print("you have withdrawn {} from your account".format(amount))
        else:
         print("withdrawal rejected")
        
    
  def deposit(self, amount):
    self.balance +=amount
    if amount > 0:
      print("You have deposited {} to your account".format(amount))
    else: 
      print("Insufficient deposited amount")  
  def get_balance(self): 
    return "This balance for {} is {}". format(self.account_name(), self.balance) 

acc1 = BankAccount("Nicole", "Kathomi")
acc2 = BankAccount("Roy", "Murithi")

print(acc1.account_name())
print(acc2.account_name())

acc1.deposit(500)
acc2.deposit(4000)
acc1.deposit(350)
acc2.deposit(-179)

print(acc1.get_balance())
print(acc2.get_balance())

acc1.withdraw(200)
acc2.withdraw(300)
acc1.withdraw(100)
acc2.withdraw(-20)

print(acc2.get_balance())
print(acc1.get_balance())
