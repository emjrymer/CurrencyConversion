from conversion_functions import convert_usd_to_eur


class Money:

    def __init__(self):
        self.amount = 0
        self.currency = ""

    # USD -------> EUR
    def convert_usd_to_eur(self, value):
        converted_amount = value * 0.9
        return round(converted_amount, 2)

    def convert_multi_entries_usd_to_eur(self, values):
        converted_amount = 0
        for value in values:
            converted_amount += value
        return round((converted_amount * 0.9), 2)

    def register_usd_to_eur(self, values):
        register = []
        for value in values:
            register.append(self.convert_usd_to_eur(value))
        return register

    # EUR -------> USD
    def convert_eur_to_usd(self, value):
        converted_amount = value * 1.11
        return round(converted_amount, 2)

    def convert_multi_entries_eur_to_usd(self, values):
        converted_amount = 0
        for value in values:
            converted_amount += value
        return round((converted_amount * 1.11), 2)

    def register_eur_to_usd(self, values):
        register = []
        for value in values:
            register.append(self.convert_eur_to_usd(value))
        return register

money = Money()
money.currency = input("Do you have EUR or USD? ")
while True:
    if money.currency.lower() == 'eur':
        type_of_conversion = input("Would you like: \nA) a register? \nB) a single sum conversion?\nC) multiple entry conversion? ")
        if type_of_conversion.lower() == 'a':
            money.amount = input("Enter a list of numbers you want converted. ")
            print(money.register_eur_to_usd(int(money.amount)))
        elif type_of_conversion.lower() == 'b':
            money.amount = input("How much in EUROS do you have? ")
            print(money.convert_eur_to_usd(int(money.amount)))
        elif type_of_conversion.lower() == 'c':
            money.amount = input("How much in EUROS do you have? ")
            print(money.convert_multi_entries_eur_to_usd(int(money.amount)))

    elif money.currency.lower() == 'usd':
        print("You have chosen USD")
    else:
        "Enter USD or EUR"

# http://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response