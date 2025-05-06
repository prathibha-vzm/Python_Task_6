#Question 1

#Base Class
class BankAccount:
    def __init__(self): #constuctor
        print("Enter your Account Number:")

        #getting input as integer
        self.account_number=int(input())

        #declaring private variable balance with minimum balance
        self._balance=500#private attribute

    #getter method to retrieve the value of private attribute
    def get_balance(self):
        return self._balance

    #Setter method to set or modify the value of private attribute
    def set_balance(self,amount):
        if self._balance >= 500:
            self._balance=amount
        else:
            print("Maintain Sufficient balance")

    #Method Deposit
    def deposit(self):
        print("Enter the Amount to deposit")
        deposit=int(input())

        #getting the value and adding.
        #setting the modified values.
        self.set_balance(self.get_balance()+deposit)

    #Method Withdraw
    def withdraw(self):
        print("Enter the Amount to withdraw")
        withdraw= int(input())

        #subtracting the withdrawal amount from balance
        self._balance -= withdraw

        #Checking for minimum balance
        if withdraw>self.get_balance():
              print("Insufficient Balance")
              #restricting to withdraw the amount
              self._balance+=withdraw

        elif self.get_balance()-withdraw<500:
              print("Maintain Sufficient balance")

        else:
              # getting the value and subtracting.
              # setting the modified values.
              self.set_balance(self.get_balance()-withdraw)


class SavingsAccount(BankAccount):
    #constructor
    def __init__(self):
        super().__init__()

        #Getting loan amount
        print("Enter the Loan Amount")
        self.loan=int(input())

        #getting time period for loan
        print("Choose the number of years to pay the loan\n1\t5\t10")
        self.interest_time=int(input())

        #calaculating the interest rate according the time
        if self.interest_time==1:
            self.interest_rate=(2/100)*self.loan
        elif self.interest_time==5:
            self.interest_rate=(3/100)*self.loan
        elif self.interest_time==10:
            self.interest_rate=(5/100)*self.loan

    #Method to calculate interest
    def calculate_interest(self):
        # calculating the interest rate
        self.interest_rate=(self.loan*self.interest_rate*self.interest_time)/100

        #printing
        print(f"Interest Rate for {self.interest_time} years : {int(self.interest_rate)}")

#subcalss with parent BankAccount class
class CurrentAccount(BankAccount):
    def __init__(self):
        super().__init__()

    #Private method to check balance(encapsulation)
    def check_balance(self):
        #Printing the balance
        print("Account Balance :",self.get_balance())

    #method to do actions according to the input
    def action(self):
        print("Choose the operation")

        while True:
            print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Interest Rate\n5. Exit")
            option=int(input())

            #Execute the methods according to the input
            if option==1:
                # calling the method from parent class
                self.deposit()
            elif option==2:
                # calling the method from parent class
                self.withdraw()
            elif option==3:
                #since it is private class(encapsulation) calling it using the object name
                self.check_balance()
            elif option==4:
                #this calculates interest is a method from another subclass
                #creating the object for the class and calling here
                savings_account_object = SavingsAccount()
                savings_account_object.calculate_interest()
            elif option==5:
                #to exit
                break
            else:
                print("Please Enter Valid option")


#creating object for the subclass and calling action method
CurrentAccount_object=CurrentAccount()
CurrentAccount_object.action()

