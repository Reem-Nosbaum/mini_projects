import random

my_list = [['always', 'be ', 'yourself'], ['keep', 'it', 'cool'], ['do', 'it', 'now'],
           ['believe', 'in', 'yourself'], ['dreams', 'come', 'true'],
           ['go', 'for', 'it'], ['get', 'over', 'it'], ['let', 'it', 'go']]

random_num = random.randint(0, len(my_list) - 1)
print(my_list[random_num])

_one_line = ([one_list for sublist in my_list[random_num] for one_list in sublist])
print(_one_line)

_under = ['_' * len(_word) for _word in _one_line]
print(_under)


new_letter = input('enter a word: ')

if new_letter in _one_line:
    _under + new_letter
    print(_under)
