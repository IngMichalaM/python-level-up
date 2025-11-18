# Save dictionary to a file, read dictionary from a file
# Might be done with python 'pickle' module as well

import json


def save_dict_to_file(dict_data, file_to_save):
    with open(file_to_save + '.json', 'w') as file:
        json.dump(dict_data, file, indent=4)
    print(f'Dictionary saved to {file_to_save}.')


def read_dict_from_file(dict_path):
    try:
        with open(dict_path, 'r') as file:
            dict_data = json.load(file)
            print(f'Dictionary loaded from {dict_path}:')
            print(dict_data)
    except FileNotFoundError:
        print(f'Error: File {dict_path} not found.')


my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
save_dict_to_file(my_dict, 'my_dict')
read_dict_from_file('my_dict.json')