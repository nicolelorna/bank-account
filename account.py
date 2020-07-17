class BankAccount():
  bank = "KCB"
  
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    self.bank = bank
    self.balance = balance
    self.phone_number = 0 
    self.deposit = []
    self.widrawals = []
    self.balance = 0
    self.loans = 0
    
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

  def withdrawl_statement(self): 
    self.withdraw=withdrawals.append(withdrwals) 
    return withdrawals

  def loan_given(self):
    print("recieved a loan of {}".format(amount))
    self.loans=self.loans + amount

  def pay_loan(self,amount):
    if amount >= 0 :
      self.repay =self.loan - amount
      print("you have paid {} to you loan".format(amount)) 


acc1 = BankAccount("Nicole", "Kathomi")
acc2 = BankAccount("Roy", "Murithi")


acc1.deposit(500)
acc2.deposit(4000)
acc1.deposit(350)
acc2.deposit(-179)

acc1.withdraw(200)
acc2.withdraw(300)
acc1.withdraw(100)
acc2.withdraw(-20)

acc2.get_balance()
acc1.requestLoan(300)
acc1.requestLoan(200)
acc1.payLoan(400)

print(acc1.account_name())
print(acc2.account_name())
