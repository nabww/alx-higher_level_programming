#!/usr/bin/python3

import sys
import json

def load_from_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

filename = 'add_item.json'
try:
    items = load_from_json_file(filename)
except:
    items = []

for arg in sys.argv[1:]:
    items.append(arg)

save_to_json_file(items, filename)

