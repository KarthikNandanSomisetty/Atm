class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("your balance is 10000")

    def withdrawl(self,amount):
        new_amount = 10000 - amount
        print("you have withdrawn amount "+str(amount) +". your remaining balance is "+ str(new_amount))



Card_number = input("insert your Card Number: ")
pin_number  = input("enter your Pin Number: ")

new_user =  Atm(Card_number ,pin_number)
print("choose your activity ")
print("1)Balance Enquriy   2)withdrawl")
activity = int(input("enter Activity Number : "))

if (activity == 1):
    new_user.check_balance()
elif (activity == 2):
    amount = int(input("enter the amount: "))
    new_user.withdrawl(amount)
else:
    print("enter a Valid Number")