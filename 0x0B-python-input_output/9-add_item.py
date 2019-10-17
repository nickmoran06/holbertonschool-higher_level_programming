#!/usr/bin/python3
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file
from sys import argv


filename = "add_item.json"

try:
    json_list = load_from_json_file(filename)
except:
    json_list = []

for arguments in argv[1:]:
    json_list.append(arguments)

save_to_json_file(json_list, filename)
