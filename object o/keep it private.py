class Something:
    __nothing= 0
    def __privmeth(self):
        print("im inside a class!")
    def pubmeth(self):
        print("value:",Something.__nothing)
obj=Something()
obj.pubmeth()
obj.__privmeth()
