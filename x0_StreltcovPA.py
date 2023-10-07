#
## Моя игра - "Крестики/Нолики".
#
print('Вас приветсвует игра - "Крестики, Нолики!"')
print('Перед Вами ировое поле.')
print("   0   1    2","\n".join(" 012"))
print("Сделайте свой ход."
              " \nУкажите координаты куда Вы поставите Нолик - 0, "
              "\nдля этоо введите подряд две цифры от 0 до 2 включительно.")

# Подготовка начальных данных.
# Крестик или Нолик. Первым ходит Нолик.
player, next_pl= ' 0', ' x'
# Формируем двумерный список начального состояния.
spisok_strok=[["  " for j in range(3) ]for i in range(3)]# Строки.
#spisok_stolb=[["  " for j in range(3) ]for i in range(3)]# Столбцы.
diag1 =['  ','  ','  ']# Диаонали.
#diag2 =['  ','  ','  ']
flag = False#Флаг победы.
# Начало игры.

for sch in range(9) :
    while True: # Вводим координаты пока не введем правильно ).
        cifra = input()

        # Этап - 1. Вод и проверка на корректность введенных данных.
        if not cifra.isdigit():
            print('Вы ввели не цифры. Попробуйте еще раз.')
        else:
            if len(cifra) > 2:
              print('Вы ввели много цифр. Попробуйте еще раз.')
            elif len(cifra) <= 1:
             print('Вы ввели мало цифр. Попробуйте еще раз.')
            else:
                os_ox,os_oy=int(cifra)//10,int(cifra)%10# Координаты строки и столбца.
                if not(os_ox<=2 and os_oy<=2):
                    print("Координаты могут состоять только из цифр: 0 или 1 или 2.")
                else:
                    # Если координаты введены правильно, то они не должны повторяться в уже введенных.
                    if spisok_strok[os_ox] [os_oy]!= '  ':
                        print("Это место занято. Выберите другой вариант.")
                    else:
                        break

    # Этап - 2. Сохранение правильных значений.
    spisok_strok[os_ox][os_oy] = player# Заполняем стороки.
    if os_ox==os_oy:
        diag1[os_ox] = player# Заполняем первую диаональ.

    # Этап - 3. Вывод результата.
    def vivod():
        print("     0   1   2")
        print("              ")
        for i in range(3):
            print(f"{i}   {spisok_strok[i][0]}  {spisok_strok[i][1]}  {spisok_strok[i][2]}")
        return
    vivod = vivod()

    # Этап - 4. Проверка на победу.
    if sch>3:
        # Повернtv матрицу на 90 радусов.
        spisok_stolb = [[spisok_strok[j][i] for j in range(3)[::-1]] for i in range(3)]  # Заполняем столбцы.
        diag2 = [[spisok_stolb[i][j] for j in range(3)if i == j] for i in range(3) ]# Заполняем вторую диагональ.
        diag2=sum(diag2,[])
        # Проверка диаоналей.

        if diag1.count(player)==3 or diag2.count(player)==3:
            print(f'{player} победил!!')
            break

        # Проверка строк и столбцов.
        for i in range(3):
            if spisok_strok[i].count(player)==3 or spisok_stolb[i].count(player)==3:
                print(f'{player} победил!!')
                flag = True
                break

    player, next_pl= next_pl,player# Смена игрока.

    if sch==8 or flag:
        print('Победила дружба!!!')
        break