class PC:
    def __init__(self):
        self.__mxpr=300
    def sell(self):
        print("selling price:",self.__mxpr)
    def stmxpr(self,price):
        self.__mxpr=price
obj=PC()
obj.sell()
obj.__mxpr=375
obj.sell()
obj.stmxpr(375)
obj.sell()