# Open Files
f = open('test.txt', 'r')
print(f.name)
f.close()

# Using With Statement
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')
# f_contents = f.readline()
# print(f_contents)
