#!/usr/bin/env python3

# Dictionaries

dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}

dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}

# Lists

list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']

list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):

    """Creating the dictionary using two lists of keys and values."""

    dictionary = {}

    index = 0

    while index < len(keys):

        dictionary[keys[index]] = values[index]

        index += 1

    return dictionary



def shared_values(dict1, dict2):

    """Finds common values between two dictionaries."""

    return set(dict1.values()) & set(dict2.values())



if __name__ == '__main__':

    york = create_dictionary(list_keys, list_values)

    print('York: ', york)

    common = shared_values(dict_york, dict_newnham)
