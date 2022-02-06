
from faker import Faker 
fake = Faker('pl_PL')

#print(fake.first_name())
#print(fake.last_name())
#print(fake.company())
#print(fake.job())
#print(fake.email())
#print(fake.phone_number())


class Card:
    def __init__(self, surname, name, firm, position, email):
        self.surname = surname
        self.name = name
        self.firm = firm
        self.position = position
        self.email = email

        #Variable
        #self._surname_len = 0
        #self._name_len = 0

    def __str__(self):
        return f'{self.name} {self.surname} {self.email}'
    
    def contact(self):
        return print(f"Kontaktuję się z {self.name} {self.surname}; {self.position}; {self.email}.")
    
    @property
    def sumlen(self):
        self._namelen = len(self.name)
        self._surnamelen = len(self.surname)
        self._sumlen = len(self.name) + len(self.surname) + 1
        return f'{self._namelen} {self._surnamelen} {self._sumlen}'
    

    


#card = Card(surname=fake.last_name(),name=fake.first_name(),firm=fake.company(),position=fake.job(),email=fake.email())
#print(card)

n = 2
cards = []

for _ in range(n):
    cards.append(Card(surname=fake.last_name(),name=fake.first_name(),firm=fake.company(),position=fake.job(),email=fake.email()))

by_name = sorted(cards, key=lambda card: card.name)
by_surname = sorted(cards, key=lambda card: card.surname)
by_email = sorted(cards, key=lambda card: card.email)

#print(cards[0])

print("")
""""
for i in range(len(cards)):
    print(f"{cards[i].name} , {cards[i].surname} , {cards[i].email} ")
    print("")
"""

print("\n")
print("Lista wizytówek: \n")
for i in range(len(cards)):
    print(cards[i])

print("\n")
print("Lista wizytówek posortowanych po imieniu: \n")
for i in range(len(by_name)):
    print(by_name[i])

print("\n")
print("Lista wizytówek posortowanych po nazwisku: \n")
for i in range(len(by_surname)):
    print(by_surname[i])

print("\n")
print("Lista wizytówek posortowanych po email: \n")
for i in range(len(by_email)):
    print(by_email[i])

print("\n")

for i in range(len(cards)):
    cards[i].contact()

print("\n")

for i in range(len(cards)):
    print(cards[i].sumlen)



