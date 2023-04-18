# превращает имя в короткий ник из 3х - 4х символов
def get_nickname(user_name):
    # Перечень гласных
    vowels = 'ауоыэяюёие'

    # для коротких имен не нужен никнейм
    if len(user_name) <= 3:
        return user_name

    # возвращаем никнейм в зависимости от 3го символа
    if user_name[2].lower() in vowels:
        return user_name[0:4]
    else:
        return user_name[0:3]


if __name__ == '__main__':
    # для удобства отладки/провекри бесконеный цикл
    while True:
        # получаем от польщорвателя имя
        name = input('Ввердите имя ')

        # проверка на пустую строку с возможностью завершить программу
        if name == '':
            answer = input('вы хотите закончить? д/н ')
            if answer == 'д':
                break

        nick_name = get_nickname(name)

        # выводим в консоль готовый ник
        print(f'Ваш никнейм: {nick_name} ')

