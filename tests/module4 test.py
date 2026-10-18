class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=False
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed=True
            print("you have borrowed a book sucsessfully")
        else:
            print("we couldn't get that please try again or ask the staff")
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed=False
            print("you have returned your library books")
        else:
            print("your books are due plz return them")
book1=book("hadi","hadi")
book2=book("snowy","bluey")
book3=book("bluey","snowy")
book1.borrow()
book2.borrow()
book3.return_book()