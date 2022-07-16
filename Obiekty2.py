class Adress_book:
    def __init__(self, name, surname, company, position, mail):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.mail = mail

A = Adress_book(name = "Małgorzata", surname = "Bona", company = "LOTAMS", position = "inżynier", mail = "malgorzata@outlook.com")
B = Adress_book(name = "Jakub", surname = "Menzel", company = "PP", position = "kierownik projektu", mail = "jakub@outlook.com")
C = Adress_book(name = "Michał", surname = "Bona", company = "Solution", position = "technik", mail = "maichał@outlook.com")
D = Adress_book(name = "Leszek", surname = "Menzel", company = "wodociągi", position = "kierownik", mail = "leszek@outlook.com")

Adress = [A, B, C, D]

for i in Adress:
    print (i.name, i.surname, i.company, i.position, i.mail)

by_name = sorted (Adress, key = lambda Adress_book:Adress_book.name)
print (by_name)


class Adress_book2:
    def __init__(self, name, surname, company, position, mail):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.mail = mail
    def __str__ (self):
        return f'{self.name} {self.surname} {self.company} {self.position} {self.mail}'

A1 = Adress_book2(name = "Małgorzata", surname = "Bona", company = "LOTAMS", position = "inżynier", mail = "malgorzata@outlook.com")
B1 = Adress_book2(name = "Jakub", surname = "Menzel", company = "PP", position = "kierownik projektu", mail = "jakub@outlook.com")
C1 = Adress_book2(name = "Michał", surname = "Bona", company = "Solution", position = "technik", mail = "maichał@outlook.com")
D1 = Adress_book2(name = "Leszek", surname = "Menzel", company = "wodociągi", position = "kierownik", mail = "leszek@outlook.com")

Adress2 = [A1, B1, C1, D1]

print (Adress2)
