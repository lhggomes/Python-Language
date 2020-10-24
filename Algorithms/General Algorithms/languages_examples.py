# Creating a list
score_list = [3, 3, 6]
for i in range(1, 10):
    score_list.append(i)

# Creating a Dictionary

student = {
    'name': 'Lucas',
    'age': 21,
    'course': 'IT'
}


student_list = [
    {
        'name': 'Lucas',
        'age': 21,
        'course': 'IT'
    }, {

        'name': 'Mateus',
        'age': 19,
        'course': 'IT'

        }

]

nome_aluno = student['name']

c = [2, 3]
y = [3, 5]

d = c + y
print(d)

for key, value in student.items():
    pass

try:
    soma_errada = 15 + 15
    print('Soma feita com sucesso!')

except (Exception, FileExistsError) as error:
    print(f'Error {error.__repr__()}')
    print('Error %s at persist' % error.__repr__())
    print('Error {} at persist'.format(error.__repr__()))

finally:
    print('Final')




student_name = student['name']

print('c')
