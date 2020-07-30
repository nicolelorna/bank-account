from datetime import datetime
class BankAccount():
  bank = "KCB"
  
  def __init__(self, first_name, last_name,phone_number,bank):
    self.first_name = first_name
    self.last_name = last_name
    self.bank = bank
    self.phone_number = phone_number
    self.balance = 0
    self.deposits = []
    self.widrawals = []
    self.balance = 0
    self.loans = 0
    
  def account_name(self):
    name = "{} account for {} {}". format(self.bank, self.first_name, self.last_name)
    return name

  def withdraw(self,amount):
    try:
      amount + 1
    except TypeError:
      print("You must enter the amount in digits")
      return
     if amount >0: 
        self.balance += amount
        timeDate = self.get_current_time()
        transaction_details = {"amount":"amount","date":"date"}
        self.withdrawals.append(transaction_details)
        print("Hello {},you have withdrawed {} from your account at {} and new balanceis {}".format(self.first_name,amount.time,self.balance))

    else:
         print("withdrawal rejected")
        
  def get_balance(self): 
    return "This balance for {} is {}". format(self.account_name(), self.balance) 

  def show_deposit_statements(self):
    try:
        amount + 1
    except TypeError:
      print("amount in digits")
      return
    deposit=self.deposits.append(amount)

    print("deposit higher amount") 

  
  else:
      self.balance += amount
      time = datetime.now()
      get_time = time.strftime("%H:%M%P , %d%m%Y")
      deposit = {
        "time": "time"
        "amount": "amount"
      }
      print("Hello {} , you have deposited {} at {}. Your balance is {}".format(self.account_name(),amount ,get_time,self.balance))

    

  def show_withdrawal_statement(self): 
    for withdrawals in self.withdrawals 
     print (withdrawals)
     
  def request_loan(self):
    try:
      amount + 1
    except TypeError:
      print("You must enter account in digits")

    if amount <= 0:   
      print("you cannot request a loan for that amount")
    else:
      self.loan = amount
      print("you have been given a loan of {}".format(amount))  
    
  def repay_loan(self,amount):
    try:
       amount + 1
    except TypeError:
      print("you must enter the amount in digits")
    if amount <= 0 :
      print("you cannot repay with that amount")
    elif self.loan == 0:
      print("you do not have a loan at the moment") 
    elif amount > self.loan:
      print("your loan is {} ,please enter an amount that is less or equal.format(self.loan)")  
    else:
      self.loan -= amount
      self.repay = self.loan - amount
      time = datetime.now()
      get_time = time,strftime("%H:%M%p %d%m%Y")
      print("you have repaid your loan with {}. your loan balance is {}.format(amount,self.loan")  
      


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
acc2.show_withdrawal statement()
acc2.show_withdrawal_statement()
print(acc1.get_balance())
print(acc2.get_balance())

print(acc1.account_name())
print(acc2.account_name())


class BankAccount(Account):
  def __init__(self,first_name,last_name,phone_number,bank):
    self.bank = bank
    super ().__init__(first_name,last_name,phone_number)


class MobileMoneyAccount (account):
  def __init__(self,first_name,last_name,phone_number,service_provider):
    self.service_provider = service_provider
    self.airtime =[]
    super ().__init___(first_name,last_name,phone_number)


   def buy_airtime(self,amount):
     try:
       amount + 1
     except TypeError:
       print("Plese enter amount in figures")\
       return
     if amount > self.balance:
       print("You do not have enough balance.Your balance is {}".format(self.balance))
       else:
         self.balance -= amount
         time = datetime.now()
         airtime = {
           "time"=time,
           "airtime":amount
         }   
         self.airtime.append(airtime)
         print("you have bought airtimeworth {} on {}".format(amount,self.get_formatted_time(time))

    def pay_bill(self,amount):
      try:
        amount + 1
      except TypeError:
          print("Please enter digits in figures")  
          return
      if amount > self.balance
           print("You do not have enough balance.Your balance is {}".format(self.balance))
         else:
             self.balance -= amount
             time = datetime.now()
             paybill = {
               "time"=time
               "paybill":amount
             }
             self.paybill.append(paybill)
             print("you have paid your bill of {} on {}".format(amount,self.get_formated_time(time))

      def send_money(self,amout):
        try:
          amount + 1
        except TypeError:
          print("Money you want to send in digits")  
          return
        if amount > self.balance
           print("You do not have enough balance.Your balance is {}".format(self.balance))  
         else:
           self.balance -= amount
           time = datetime.now()
           sendmoney ={
             "time"=time
             "money":amount
           } 
           self.send_money.append(send_money) 
           print("You have sent {} amount of money on {}".format(amount,self.get_formatted_time(time))

     def recieve_money(self,amount):
        try:
          amount + 1
         except TypeError:
           print("Type amount of money recieved in digits")   
           return
         if amount > self.balance
           print("Money recieved in digits") 
         else:
           self.balance -= amount
           time = datetime.now()
           recievemoney ={
             "time"=time
             "money":amount
           }    
           self.recieve_money.append(recieve_money)  
           print("You have recieved {} money on {}".format(amount,self.get_formatted_time(time))
