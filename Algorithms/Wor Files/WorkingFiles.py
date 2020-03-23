# Open Files
f = open('test.txt', 'r')
print(f.name)
f.close()

# Using With Statement
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')

# Determing a size
with open('test.txt', 'r') as f:
    szread = 10
    f_contents = f.read(szread)
    while len(f_contents) > 0:
        print(f_contents, end='')
