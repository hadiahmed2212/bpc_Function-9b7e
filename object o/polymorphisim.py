class Australia:
    def lange(self):
        print("The language used in Australia is English AU")
    def capital(self):
        print("The CAPITAL city of Australia is Canberra")
    def type(self):
        print("type of country: HIGHLY DEVELOPED")
class Pakistan:
    def lange(self):
        print("The language used in Pakistan is Urdu")
    def capital(self):
        print("The CAPITAL city of Pakistan is Islamabad")
    def type(self):
        print("type of country: developing country")
objpak=Pakistan()
objaus=Australia()

for country in (objaus,objpak):
    country.capital()
    country.lange()
    country.type()