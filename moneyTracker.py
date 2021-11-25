import sqlite3
connection = sqlite3.connect('tracker.db') #creat a database

class action:
    def __init__(self, amount, description):
        self.amount = self.checkamount(amount)
        self.kind = self.checkKind()
        self.description = description

    def checkamount(self,amount):
        """
        this method check if the amount variable is actually an
        integer number or not
        :param amount: the mount of money the user typed in
        :return: amount if it's an integer, otherwise False or assert
        """
        if isinstance(amount, int) and amount != 0:
            return amount
        elif amount == 0:
            print("הכנס מספר שונה מאפס")
            return False
        elif isinstance(amount, float):
            print("הכנס מספר שלם!")
            return False
        else:
            assert False, ("הערך שהוכנס אינו מספר, אנא הכנס מספר!")

    def checkKind(self):
        """
        this method check if this is an income or outcome.
        if amount > 0 -> income
        :param amount:
        :return:
        note: maybe I should ask the user if this is an income or outcome
        """
        kind = input("income or outcome? i or o: ")
        while (kind != "o" and kind !="i"):
            kind = input("income or outcome? i or o: ")
        if kind == "i":
            kind = "input"
        else:
            kind = "output"
        return kind



# a = action(102,"income")
# print(f"amount = {a.amount} , kind = {a.kind} , description = {a.description}")
# print (f"current amount = {lastamount}")


# TO_DO:
# 1. what to do with "last amount"
#