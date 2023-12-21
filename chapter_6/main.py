my_dict = {
    'soccer': ['Manchester City', 'Bayern Munic', 'Seattle Sounders'],
    'formula one': {'driver': 'andretti'},
    'football': {'nfl': ['seahawks', 'packers', 'NOT THE PATRIOTS ANYONE BUT TOM BRADY'],
                'college': ['clemson', 'ucla', 'anyone but alabama'], 1: 3}}

print(my_dict)
print(isinstance(my_dict['football'][1], list))

# my_dict ['new key'] = 'Alphonso'
# my_dict[2] = 'cheesy bread'
# my_dict[2] = 'endless breadsticks'
# del my_dict[2]
# my_dict [2] = ''

# print(my_dict)

# x = my_dict.get(3)
# print(x)

#  for k, v in my_dict.items():
#      print(f'The key is {k}')
#      print(f'And this is the value: {v}')

# for key in my_dict.keys():
#     print(key)

#     for value in my_dict.values():
#         print(value)