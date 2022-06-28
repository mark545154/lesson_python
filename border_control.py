###################################################################################
# 1. Что такое список

###################################################################################
# 2. Что такое список?

# Это тип данных. Предназначенный для хранения набора или последовательности разных элементов.
# Т.е. упорядоченный набор элементов.
# Список всегда начинается [ и заканчивается ] вот такими квадратными скобками.

###################################################################################
# 3. Программист, разрабатывающий приложение для
# хранения документов в строительной компании,
# должен предусмотреть в приложении возможность
# вывода информации о документе в консоль.
# Номер договора имеет формат 20А-21Б, причем должен содержать
# только заглавные буквы, Фамилия, имя составителя должны начинаться
# с Заглавной буквы, остальные строчные,
# Тип документа должен быть выведен только строчными буквами.
# На каждый параметр необходимо создать отдельную переменную.
# Вывести результат в консоль

# num_contract = input('Введите номер договора: ').upper()  # только заглавные буквы
# surname = input('Введите фамилию: ').title()  # начинаться с Заглавной буквы
# name = input('Введите имя: ').title()  # начинаться с Заглавной буквы
# type_doc = input('Введите тип документа: ').lower()  # только строчные буквы
#
# print(type_doc, num_contract, surname, name)

###################################################################################
# 4. Имеются данные о продажах некоторого магазина:
# Товары, которые продавала аптека на неделе:
# Картон (300 руб, купили 10 раз),
# Бумага (500 руб, купили 6 раз),
# Ножницы (124 руб, купили 12 раз),
# Папка (750 руб, купили 4 раза),
# Набор профессиональной акварели (567 руб, купили 5 раз),
# Подставка-котик (320 руб., купили 20 раз).
# Необходимо создать файл csv, который содержит название товара,
# стоимость и количество покупок,

# разработать приложение (использовать словари),
# чтобы на выходе можно было получить средние количество продаж,
# выручке, ценах, а также максимальное и минимальное значение,
# самый продаваемый товар, самый непопулярный товар.
# Всю статистику необходимо вывести в консоль и сохранить в отдельный файл.

import csv

product_list = [{'name': 'Картон', 'price': 300, 'purchases': 10},
                {'name': 'Бумага', 'price': 500, 'purchases': 6},
                {'name': 'Ножницы', 'price': 124, 'purchases': 12},
                {'name': 'Папка', 'price': 750, 'purchases': 4},
                {'name': 'Набор профессиональной акварели', 'price': 567, 'purchases': 5},
                {'name': 'Подставка-котик', 'price': 320, 'purchases': 20}]

with open('sales.csv', 'w') as sal_csv:
    fields = ['name', 'price', 'purchases']
    record = csv.DictWriter(sal_csv, fieldnames=fields)
    record.writeheader()

    for index in product_list:
        record.writerow(index)
sal_csv.close()


def file_loading(file_name, delim, column):
    result = []
    with open(file_name) as file_csv:
        file_reader = csv.DictReader(file_csv, delimiter=delim)
        for row in file_reader:
            result.append(float(row[column]))
    return result


def sals(price_list, sale_list):
    ave_sale = sum(sale_list) / len(sale_list)  # Находим среднее в кол-ве продаж в списке purchases
    ave_price = sum(price_list) / len(price_list)  # Находим среднюю цену в листе price

    max_sale = max(sale_list)  # Находим максимальное значение в списке purchases
    max_price = max(price_list)  # Находим максимальное значение в списке price

    min_sale = min(sale_list)  # Находим минимальное значение в списке purchases
    min_price = min(price_list)  # Находим минимальное значение в списке price

    revenue = [(price_list[i]) * sale_list[i] / 10 for i in range(len(sale_list))]  # Среднее кол-во продаж за 10 дней
    sor_rev = sorted(revenue)
    return ave_sale, (round(ave_price), 1), max_sale, max_price, min_sale, min_price, sor_rev


quantity = file_loading('sales.csv', ',', 'purchases')
price_sale = file_loading('sales.csv', ',', 'price')


ave_sale, ave_price, max_sale, max_price, min_sale, min_price, sor_rev = sals(price_sale, quantity)

popular_product = {'name': 0, 'price': 0, 'purchases': 0}

for index in range(len(product_list)):
    if product_list[index]['purchases'] > popular_product['purchases']:
        popular_product['price'] = product_list[index]['price']
        popular_product['purchases'] = product_list[index]['purchases']
        popular_product['name'] = product_list[index]['name']

print(popular_product)





# no_popular_product = {'name': 0, 'price': 0, 'purchases': 0}
#
# for index in range(len(product_list)):
#     if product_list[index]['purchases'] < no_popular_product['purchases']:
#         no_popular_product['price'] = product_list[index]['price']
#         no_popular_product['purchases'] = product_list[index]['purchases']
#         no_popular_product['name'] = product_list[index]['name']
# print(no_popular_product)


# print(f'''За неделю:
# Среднее значение по продажам {ave_sale}
# Среднее значение по цене {ave_price}
# Максимальное кол-во товаров продано {max_sale}
# Максимальная продажа по цене {max_price}
# Минимальное кол-во которое было продано {min_sale}
# Минимальная цена по продажам {min_price}
# Средняя выручка за 7 дней {sor_rev}
# Самый продаваемый товар {popular_product}
# Самый непопулярный товар {no_popular_product}''')
