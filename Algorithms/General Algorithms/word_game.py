import random as rd
words = []

with open('Words.txt', 'r') as f:
    words = f.readlines()

inWord = rd.randint(0, (len(words) - 1))
drawnWord = words[inWord]
print(drawnWord)

word = ['_'] * len(drawnWord)
while True:
    letter = input("Digite uma letra Maiscula: ")
    for i in range(len(drawnWord)):
        if letter == drawnWord[i]:
            word[i] = letter

    if ''.join(word) == drawnWord:
        print('You Won! Ended Game!')
        print('A palavra é {0}'.format(drawnWord))
        break
    else:
        print(''.join(word))







