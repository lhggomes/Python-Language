import random as rd
words = []

with open('Words.txt', 'r') as f:
    words = f.readlines()


inWord = rd.randint(0, (len(words) - 1))
drawnWord = words[inWord].replace('\n', '')
print(drawnWord)





