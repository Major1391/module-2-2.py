first = int(input('Введите любое число '))
second = int(input('Введите любое число '))
third = int(input('Введите любое число '))

if first == second and second == third:
    print(3)

elif first == second or second == third or first == third:
    print(2)

else:
    print(0)