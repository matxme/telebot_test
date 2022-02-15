# первая задача
name = 'roma'
print(name)
# вторая пошла...
age = 17
print('my name is', name, 'and im', age)
# третья
more_name = (name + ' ') * 5
print(more_name)
print((name + ' ')*5)   # два разных способа, why not ?
# четвёртая
print('what is ur name?')
user_name = input()
while user_name.isspace() or ' ' in user_name:
    print('pls enter correct name')    # проверка на наличие пробелов в нике
    user_name = input()
print('good', user_name, 'how old r u?')
user_age = input()
while int(user_age) <= 0 or int(user_age) >= 150:
    print('pls enter correct age')      # проверка на корректность возраста
    user_age = input()
print('ur name is', user_name, 'and u r', user_age)
# пятый пошёл
if int(user_age) < 20:
    print('lol, ok zoomer')   # шутки про возраст
else:
    print('lol, ok boomer')
# шестая (пошла, но на костылях)
print(user_name[1:-1])
print(user_name[0:2])       # вывод имени по частям
print(user_name[::-1])
# седьмая
length = len(user_name)
print('name length is', length)        # длина имени и операции с возрастом
age_length = len(user_age)
if int(age_length) == 2:
    print(int(user_age[0])+int(user_age[1]))
    print(int(user_age[0])*int(user_age[1]))
elif int(age_length) == 3:
    print(int(user_age[0]) + int(user_age[1]) + int(user_age[2]))
    print(int(user_age[0]) * int(user_age[1]) * int(user_age[1]))
else:
    print('ur age is bruh')
# восьмая
print(user_name.title())
print(user_name.lower())     # изменение регистра символов и тд
print(user_name.upper())
# тесты от девятой вшил
# десятая
print('tell me pls 2+2*2 = ?')
zadacha = 2+2*2
sol = input()
while int(sol) != zadacha:
    print('nope')
    sol = input()
else:
    print('yep')
