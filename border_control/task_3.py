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

num_contract = input('Введите номер договора: ').upper()  # только заглавные буквы
surname = input('Введите фамилию: ').title()  # начинаться с Заглавной буквы
name = input('Введите имя: ').title()  # начинаться с Заглавной буквы
type_doc = input('Введите тип документа: ').lower()  # только строчные буквы

print(type_doc, num_contract, surname, name)
