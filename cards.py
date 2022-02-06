
from faker import Faker 
fake = Faker()

#print(fake.first_name())
#print(fake.last_name())
#print(fake.company())
#print(fake.job())
#print(fake.email())


class Card:
    def __init__(self, surname, name, firm, position, email):
        self.surname = surname
        self.name = name
        self.firm = firm
        self.position = position
        self.email = email
    def __str__(self):
        return f'{self.name} {self.surname} {self.email}'
    


#card = Card(surname=fake.last_name(),name=fake.first_name(),firm=fake.company(),position=fake.job(),email=fake.email())
#print(card)

n = 10
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


