from json import dumps, loads
from pprint import pp


json_string_in = '''
{
    "_id": "_b_mountains",
    "name": "Горы",
    "changed": false,
    "enter condition": {
        "pass": 10,
        "run": 15
    },
    "zones": [
        "_z_plateau", 
        "_z_scarp", 
        "_z_rocks", 
        "_z_nek"
    ]
}
'''

data = loads(json_string_in)

# >>> pp(data, width=30)
# {'_id': '_b_mountains',
#  'name': 'Горы',
#  'changed': False,
#  'enter condition': {'pass': 10,
#                      'run': 15},
#  'zones': ['_z_plateau',
#            '_z_scarp',
#            '_z_rocks',
#            '_z_nek']}


data['enter condition']['run'] = 15.5

# компактное представление (для сетевой передачи)
json_string_out_1 = dumps(data)

# >>> print(json_string_out_1)
# {"_id": "_b_mountains", "name": "\u0413\u043e\u0440\u044b", "changed": false, "enter condition": {"pass": 10, "run": 15.5}, "zones": ["_z_plateau", "_z_scarp", "_z_rocks", "_z_nek"]}

# представление с отступами (для записи в файл)
json_string_out_2 = dumps(data, ensure_ascii=False, indent=2)

# >>> print(json_string_out_2)
# {
#   "_id": "_b_mountains",
#   "name": "Горы",
#   "changed": false,
#   "enter condition": {
#     "pass": 10,
#     "run": 15.5
#   },
#   "zones": [
#     "_z_plateau",
#     "_z_scarp",
#     "_z_rocks",
#     "_z_nek"
#   ]
# }

