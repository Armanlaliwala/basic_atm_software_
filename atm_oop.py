class Atm:
    
  def __init__(self):
    pin = ''
    balance = 0
    self.menu()

  def menu(self):
    user_input = input("""
    Hi how can I help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit
    """)

    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    elif user_input == '3':
       self.check_balance()
    elif user_input == '4':
      self.withdraw()
    else:
      exit()


  def create_pin(self):
    user_pin = input('Enter your pin')
    self.pin = user_pin

    user_balance = int(input('Enter balance'))
    self.balance = user_balance
    print('Pin created successfully')
    self.menu()


  def change_pin(self):
    old_pin = input("Enter Old Pin ")
    if old_pin == self.pin:
      new_pin = input("Enter New Pin ")
      self.pin = new_pin
      print("Pin changed successfully")
    else:
      print("Incorrect Pin")
    self.menu()

  def check_balance(self):
    user_pin = input('Enter your pin')
    if  user_pin == self.pin :
      print('Your balance is ', self.balance)
    else:
      print('Incorrect Pin')
    self.menu()

  def withdraw(self):
    user_pin = input('Enter the pin')
    if  user_pin == self.pin :
      amount = int(input('Enter the amount'))
      if amount <= self.balance:
        self.balance = self.balance - amount
        print('Withdraw Successful')
      else:
        print('Insufficient Balance')
    else:
      print('Incorrect Pin')
    self.menu()

obj = Atm()