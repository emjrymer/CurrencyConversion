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


def valid_input(value):
    if value.isalpha():
        return "Not a proper value. "

