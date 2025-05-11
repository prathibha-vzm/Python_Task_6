import pyexcel_ods3

class BankAccount:
    def __init__(self,account_number,name="",filename="bank.ods"):
        self.name = name
        self.account_number=account_number
        self.balance=0
        self.filename=filename

    def deposit(self,deposit_input):

        data = pyexcel_ods3.get_data(self.filename)
        current_data = data.get("Current Account", [])

        for dep_row in current_data[1:]:
            if dep_row[0]==self.account_number:
                self.balance=dep_row[2]
                self.balance += deposit_input
                dep_row[2]=self.balance
                pyexcel_ods3.save_data(self.filename, data)
                print(f"Successfully Deposited {deposit_input}")


    def withdraw(self,withdraw_input):

        if self.balance-withdraw_input <500:
            print("Not Enough Balance to withdraw")

        else:
            data = pyexcel_ods3.get_data(self.filename)
            current_data = data.get("Current Account", [])

            for wd_row in current_data[1:]:
                if wd_row[0] == self.account_number:
                    self.balance = wd_row[2]
                    self.balance -=withdraw_input
                    wd_row[2] = self.balance

                    pyexcel_ods3.save_data(self.filename, data)
                    print(f"Successfully Withdrawn {withdraw_input}")


class SavingsAccount(BankAccount):
    def __init__(self,name,account_number,filename="bank.ods",interest_rate=0):
        super().__init__(name,account_number,filename)
        self.interest_rate=interest_rate


    def calculate_interest(self):
        data = pyexcel_ods3.get_data(self.filename)
        current_data = data.get("Current Account", [])
        saving_data=data.get("Savings Account", [])



        for current_row in current_data[1:]:
                if current_row[0] == self.account_number:
                    self.balance = current_row[2]

                    if 500 < self.balance < 1000:
                        self.interest_rate = (3 / 100) * self.balance



                    elif self.balance > 1000:
                        self.interest_rate = (5 / 100) * self.balance


                    saving_data.append([self.account_number, self.name, self.interest_rate])
                    data["Savings Account"]=saving_data
                    pyexcel_ods3.save_data(self.filename,data)

                    print(f"{self.interest_rate} added to {self.account_number}")
                    return




class CurrentAccount(BankAccount):
    def check_balance(self,filename="bank.ods"):

        data=pyexcel_ods3.get_data(filename)
        check_data=data.get("Current Account",[])

        for check_row in check_data[1:]:

            if check_row[0]==self.account_number:
                self.account_number = check_row[0]
                self.balance = check_row[2]

                print(f"{self.account_number}-Your Balance-${self.balance}")


class Main(BankAccount):
    def account_availability(self, filename="bank.ods"):

        data = pyexcel_ods3.get_data(filename)
        account_data = data.get("Current Account", [])

        for row in account_data[1:]:
            if row[0]==self.account_number:
                self.name=row[1]
                print(f"Welcome {self.name}")
                return True


        print("Account not found")
        return False


account_number_input=int(input("Account Number :"))

main_object=Main(account_number_input)
if not main_object.account_availability():
    exit()

bank_object=BankAccount(account_number_input)

while True:
    try:
        print("Please select the Operation\n1. Deposit\n2. Withdraw\n3. Interest Amount\n4. Check Balance\n5. Exit")
        user_option = int(input())

        if user_option == 1:
            deposit_amount = int(input("Enter the amount to deposit "))
            bank_object.deposit(deposit_amount)
        elif user_option == 2:
            withdraw_amount = int(input("Enter the amount to withdraw "))
            bank_object.withdraw(withdraw_amount)
        elif user_option == 3:
            savings_object = SavingsAccount(main_object.name,account_number_input)
            savings_object.calculate_interest()
        elif user_option == 4:
            current_object = CurrentAccount(account_number_input)
            current_object.check_balance()
        elif user_option == 5:
            break


    except ValueError:
        print("Please Enter the valid option")

















