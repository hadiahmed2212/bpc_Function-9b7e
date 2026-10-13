class Acc:
    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = pin 

    def show_pin_status(self):
        print("account owner:", self.owner)
        print("PIN is stored inside the class.")
    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN updated successfully.")
        else:
            print("PIN can only be 4 numbers long")
    def check_pin(self, entered_pin):
        if entered_pin == self.__pin:
            print("Access gained.")
        else:
            print("Access denied.")
 
    def __str__(self):
        return "account holder: " + self.owner
my_acc = Acc("Hadi","6741")
print(my_acc)
my_acc.show_pin_status()
my_acc.__pin = "9999"
print("tried to change PIN")
my_acc.check_pin("6741")
my_acc.check_pin("5656")
my_acc.set_pin("9999")
my_acc.check_pin("9999")