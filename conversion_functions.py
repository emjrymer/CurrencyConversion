# USD -------> EUR
def convert_usd_to_eur(value):
    converted_amount = value * 0.9
    return round(converted_amount, 2)


def convert_multi_entries_usd_to_eur(values):
    converted_amount = 0
    for value in values:
        converted_amount += value
    return round((converted_amount * 0.9), 2)


def register_usd_to_eur(values):
    register = []
    for value in values:
        register.append(convert_usd_to_eur(value))
    return register


# EUR -------> USD
def convert_eur_to_usd(value):
    converted_amount = value * 1.11
    return round(converted_amount, 2)


def convert_multi_entries_eur_to_usd(values):
    converted_amount = 0
    for value in values:
        converted_amount += value
    return round((converted_amount * 1.11), 2)


def register_eur_to_usd(values):
    register = []
    for value in values:
        register.append(convert_eur_to_usd(value))
    return register


# attempting to validate the user's input :(

'''def valid_input(values):
    for value in values:
        if value.isnumeric():
            if value > 0:
                return value
        else:
            return "Not a proper value. "


def proper_input(values):
        for value in values:
        try:
            return value
        except ValueError:
            if str(value).isalpha():
                return "not a proper input"
            elif len(str(value)) == 0:
                return "not a proper input"'''


def proper_input(values):
    while True:
        for value in values:
            if not int(value):
                print("not a proper input")
                continue
            elif int(value) <= 0:
                print("not a proper input")
                continue
            else:
                return value
