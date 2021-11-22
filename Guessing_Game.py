import random

my_list = [['always', 'be', 'yourself'], ['keep', 'it', 'cool'],
           ['do', 'it', 'now'], ['believe', 'in', 'yourself'],
           ['dreams', 'come', 'true'], ['go', 'for', 'it'],
           ['get', 'over', 'it'], ['let', 'it', 'go'],
           ['be', 'here', 'now'], ['do', 'your', 'best']]

num = random.randint(0, len(my_list) - 1)
display_none = []
for i in range(len(my_list[num])):
    display_none.append('_' * len(my_list[num][i]))
print(display_none)
print(my_list[num])
score = 0

while display_none != my_list[num]:
    letter = input('enter a guess letter: ').lower()
    if letter == int or float:
        print("INVALID CHARACTER, TRY AGAIN.")

    count_guess = 0
    for word_index in range(len(my_list[num])):
        for letter_index in range(len(my_list[num][word_index])):
            if my_list[num][word_index][letter_index] == letter:
                display_none[word_index] = display_none[word_index][:letter_index] + letter + display_none[word_index][
                                                                                              letter_index + 1:]
                count_guess += 1
    if count_guess != 0:
        score += 5
    else:
        score -= 1
    print(display_none)

print(f'GOOD JOB, YOU DID IT! YOUR SCORE IS * {score} *')
