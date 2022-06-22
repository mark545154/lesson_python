####################################################################
# Скраббл
# В этом проекте вы будете обрабатывать некоторые данные группы друзей, играющих в
# скраббл. Вы будете использовать словари для систематизации игроков, слов и очков.
# Есть много способов расширить этот проект самостоятельно, если вы закончите и
# захотите больше попрактиковаться!
# 1. Мы предоставили вам два списка, буквы и точки. Мы хотели бы объединить эти
# два в словарь, который бы сопоставил букву с ее значением точки.
# Используя понимание списка и zip, создайте словарь с именем letter_to_points, который
# содержит элементы букв в качестве ключей и элементы точек в качестве значений.
# letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
# "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8
# , 4, 10]
# 2. В нашем списке писем не учитывались пустые плитки. Добавьте в словарь
# letter_to_points элемент с ключом " " и значением точки 0.
# 3. Мы хотим создать функцию, которая будет принимать слово и возвращать, сколько
# очков стоит это слово.
# 4. Определите функцию с именем score_word, которая принимает слово в качестве
# параметра.
# 5. Реализуйте в рамках функции алгоритм подсчета очков введенного слова.
# 6. Протестируйте полученную функцию с использованием print

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
           "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key: value for key, value in zip(letters, points)}
letter_to_points[" "] = 0


def score_word(word):
    score = 0
    for letter in word.upper():
        score += letter_to_points[letter]
    return score


print(score_word('hello'))

####################################################################
# Помощник пассивного (индексного) инвестора
# Пассивным инвестированием называют формирование портфеля из различных ценных
# бумаг на длительный срок. В основном – это инвестирование в индексные фонды и ETF.
# Начинающий инвестор, после консультации со специалистом, сформировал проект
# идеального портфеля
# Необходимо разработать приложение, позволяющее сформировать файл с рекомендациями
# по текущему портфелю следующим образом:
# При наличии ценной бумаги из идеального портфеля в текущем портфеле,
# необходимо рассчитать ее долю в общей стоимости портфеля и сравнить с эталонной
# долей. Вариация не должна превышать 5%. Дать рекомендации по покупке или
# продаже ее части с указанием суммы и количества бумаг.
# При отсутствии бумаги – дать рекомендации о покупке с указанием суммы покупки
# и количества, исходя из текущих котировок.
# При наличии в портфеле лишних бумаг, дать рекомендацию об их продаже.
# Рекомендация должна выводиться в файл. Основной функционал оформляется в виде
# функций

ideal = {'FXGD': 0.15, 'FXRB': 0.07, 'FXRU': 0.08, 'FXRL': 0.1, 'FXCN': 0.16, 'FXUS': 0.24, 'FXIT': 0.16}

actual = {'FXRE': 75, 'FXRD': 103, 'FXES': 79, 'FXFA': 78, 'FXTP': 78, 'FXIP': 108, 'FXDM': 78, 'FXGD': 903,
          'FXWO': 1.89, 'FXRW': 1.34, 'FXTB': 762, 'FXMM': 1715, 'FXUS': 64, 'FXRB': 19, 'FXRU': 956, 'FXDE': 29,
          'FXCN': 3117, 'FXKZ': 331, 'FXIM': 102, 'FXIT': 12337, 'FXRL': 43}
current = {'FXCN': 49900, 'FXIT': 37000, 'FXDM': 31484, 'FXGD': 23493, 'FXWO': 21800, 'FXUS': 19000, 'FXDE': 14745,
           'FXES': 11776, 'FXRL': 12000}

summ_cur = sum(current.values())

def differs(cur_list, ideal_list):
    extra = []

    for pond in cur_list:
        if pond not in ideal_list:
            extra.append(pond)
    miss = [pond for pond in ideal_list if pond not in cur_list]
    return extra, miss

print(differs(current.keys(), ideal.keys()))


####################################################################
#
cards = [
    {'surname': 'Астахов', 'name': 'Игорь', 'patronymic': 'Александрович', 'age': 35, 'gender': 'Муж', 'married': True,
     'sity': 'Москва', 'job': 'маркетолог'},
    {'surname': 'Вавилова', 'name': 'Елена', 'patronymic': 'Сергеевна', 'age': 40, 'gender': 'Жен', 'married': True,
     'sity': 'Таганрог', 'job': 'бухгалтер'},
    {'surname': 'Карелин', 'name': 'Андрей', 'patronymic': 'Васильевич', 'age': 25, 'gender': 'Муж', 'married': False,
     'sity': 'Подольск', 'job': 'специалист'},
    {'surname': 'Воронова', 'name': 'Мария', 'patronymic': 'Игоревна', 'age': 30, 'gender': 'Жен', 'married': False,
     'sity': 'Москва', 'job': 'менеджер'},
    {'surname': 'Остроумовна', 'name': 'Карина', 'patronymic': 'Владимировна', 'age': 44, 'gender': 'Жен',
     'married': True, 'sity': 'Подольск', 'job': 'маркетолог'},
    {'surname': 'Борзов', 'name': 'Владимир', 'patronymic': 'Андреевич', 'age': 40, 'gender': 'Муж', 'married': False,
     'sity': 'Москва', 'job': 'начальник отдела'}]

spec = ['маркетолог', 'бухгалтер', 'менеджер', 'специалист']
mid_manag = ['начальник отдела', 'главный бухгалтер']
top_manag = ['директор']
salary = [40000, 60000, 80000]

ndfl = 0.13
social = 0.3


def salaries(cards):
    for card in cards:
        if card['job'] in spec:
            card['salary'] = salary[0]
        elif card['job'] in mid_manag:
            card['salary'] = salary[1]
        elif card['job'] in top_manag:
            card['salary'] = salary[2]


salaries(cards)

# print(cards)


def bonus(card, bonus_value):
    card['salary'] += bonus_value


def nalog(cards, percent):
    return cards['salary'] * percent

taxes = 0
socstrah = 0

for card in cards:
    if card['married'] == True:
        bonus(card, 5000)

    print(f'''{card['name']}, {card['patronymic']}, {card['surname']}
    {card['job']}, {card['salary'] - nalog(card, ndfl)} ''')

    taxes += nalog(card, ndfl)
    socstrah += nalog(card, social)

print(f'''Общие налоговые отчисления составили: {taxes}
Сумма страховых взносов составила: {socstrah}''')
# print(cards)

####################################################################

import random

print(random.__dict__.keys())

####################################################################
#
# from random import randint
# randint(1.10)

import random
random.randint(1, 10)

