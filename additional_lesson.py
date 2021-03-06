###################################################################
# - - - - - - Дополнительное занятие 04.06.2022 - - - - - - - #

# Задача 1. Необходимо создать приложение для магазина по продаже книг. Артикул книги формируется, как первые 3 буква
# названия и страна издания.


country = input('Страна издания: ')
title = input('Название книги: ')
article = title[0:3] + ' ' + country
surname = input('Фамилия автора: ')
name = input('Имя автора: ')
annotation = input('Анотация: ')


def sale_book(country, title, article, surname, name, annotation):
    return 'В продаже появилась новая книга. Название книги ' + title + ' Автор  – ' + surname + ' ' + name[
        0] + '.' + ' ' + article + '.'


print(sale_book(country, title, article, surname, name, annotation))

###################################################################
# Задача 2. В торговом центре проводится розыгрыш призов. Для получения приза необходимо загадать число.

import random


def present(user_num):
    result_number = random.randint(1, 9)  # Равно 3
    # print(result_number)  # Проверяем что выводит random
    suming = 0  # Изначальное число

    # Через цикл while
    #     while user_num != 0:  # Будет выполняться пока не будет равно нулю
    #         suming = suming + user_num % 10  # Проверяем есть ли остаток от деления на 10 введённого числа
    #         user_num = user_num // 10  # Проверяем делится ли число на 10 введённого числа
    #     if suming % result_number == 0:
    #         return 'Выигрыш'
    #     else:
    #         return 'Проигрыш'
    # print(present(22))

    # Проверяем циклом for
    for item in str(user_num):  # item временная переменная, которая живёт только в цикле.
        suming += int(item)  # Проверяем первую введённую цифру и вторую, которая вводится. Проверяем и сравниваем.
    print(suming)  # Выводим что получилось в цикле

    if suming % result_number == 0:
        return 'Выигрыш'
    else:
        return 'Проигрыш'


print(present(22))


###################################################################
# Упрощённый вариант решения Задачи

import random


def loto(user_number):  # равен 22
    result_number = random.randint(1, 9)
    print(result_number)

    if user_number % result_number == 0:
        print('Выигрыш')
    else:
        print('Проигрыш') # Проигрыш


loto(22)

# ##################################################################
# Упражнение 3. Вы создаете приложение, которое позволяет пользователям взаимодействовать и делиться своими идеями и проектами в Интернете

def test_string(string, name):
    if name in string:
        return True
    else:
        return False


print(test_string('Привет, Вика!', 'Вика'))  # True


# ##################################################################
# Упражнение 4. Перевернуть слово. Например, если ввести слово «Паровоз», то функция вернет «зовораП».

def string(name):
    return name[::-1]

print(string('Паровоз'))

###################################################################
# Упражнение 5. Написать функцию, меняющую местами первые буквы двух слов. Например, на вход подается «куриное филе», функция возвращает «фуриное киле»

def string(name1, name2):
    string1 = name2[0] + name1[1:] + ' ' + name1[0] + name2[1:]
    return string1


print(string('куриное', 'филе'))

###################################################################

