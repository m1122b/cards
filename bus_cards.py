

from faker import Faker 
fake = Faker('pl_PL')

#print(fake.first_name())
#print(fake.last_name())
#print(fake.company())
#print(fake.job())
#print(fake.email())
#print(fake.phone_number())


class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.name} {self.surname} {self.phone} {self.email}'
    
    def contact(self):
        return print(f"Wybieram numer prywatny {self.phone} i dzwonię do {self.name} {self.surname}.")
    
    @property
    def label_length(self):
        self.sumlen = len(self.name) + len(self.surname)
        return self.sumlen
    



class BusinessContact(BaseContact):
    def __init__(self, position, firm, busphone, *args, **kwargs):
        self.position = position
        self.firm = firm
        self.busphone = busphone
        super().__init__(*args, **kwargs)
        
    def contact(self):
        return print(f"Wybieram numer służbowy {self.busphone} i dzwonię do {self.name} {self.surname}.")
    



def create_contacts( type_of_card: str = 'business'  , number_of_cards: int = 2) -> list:
    """
    type_of_cards (string) - 'business' or 'base' \n
    number_of_cards (integer) - from 1 to .......

    """
    cards = []

    if type_of_card == 'base':
        for _ in range(number_of_cards):
            cards.append(BaseContact(name=fake.first_name(),
                                     surname=fake.last_name(),
                                     phone=fake.phone_number(),
                                     email=fake.email()
                                     ))
    
    elif type_of_card == 'business':
              for _ in range(number_of_cards):
                  cards.append(BusinessContact(name=fake.first_name(),
                                               surname=fake.last_name(),
                                               phone=fake.phone_number(),
                                               email=fake.email(),
                                               position=fake.job(),
                                               firm=fake.company(),
                                               busphone=fake.phone_number()
                                               ))

    else:
        exit(1)
    
    return cards



base_cards = create_contacts('base' , 20)

business_cards = create_contacts(number_of_cards = 12)

print("\n")

for i in range(len(base_cards)):
    print(base_cards[i])
    print(f"Suma znaków imienia i nazwiska: {base_cards[i].label_length}.")

print("\n")

for i in range(len(base_cards)):
    base_cards[i].contact()

print("\n")

for i in range(len(business_cards)):
    print(business_cards[i])

print("\n")

for i in range(len(business_cards)):
    business_cards[i].contact()

print("\n")




