print('Добро пожаловать в калькулятор!')
e = input('Желаете начать? ')
while True:
    if e == 'y':
        a = int(input("Введите первое число:\n"))
        x = input('Введите операцию:\n')
        b = int(input('Введите второе число:\n'))
        if x == '+' :
           print('Итого:: ', a + b)
        elif x == '-' :
             print('Итого::', a - b)
        elif x == '*' :
             print('Итого::', a * b)
        elif x == '/' :
             print('Итого::', a / b)
             if b != 0:
                print(a / b)
             else:
                print('Деление на ноль невозможно!')
        else: print('Неверная операция!')

        d = input('Ещё раз? ')
        if d == 'y':
           continue
        elif d == 'n':
            print('Благодарим вас за использование калькулятора!')
            quit()
    elif e == 'n':
        quit()