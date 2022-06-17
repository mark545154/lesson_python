####################################################################
#
# menu = {"тост с авокадо": 6, "морковный сок": 5, "черничный маффин": 2}
#
# sensors = {"гостиная": 21, "кухня": 23, "спальня": 20, 'party': 22}
#
# num_cameras = {"двор": 6, "гараж": 2, "проезжая часть": 1}
#
# subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}
#
# students_in_classes = {"software design": ["Aaron", "Delila", "Samson"],
#                        "cartography": ["Christopher", "Juan", "Marco"],
#                        "philosophy": ["Frederica", "Manuel"]}
#
# person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}
#
# dictionary = {'mountain': 'orod', 'bread': 'bass', 'friend': 'mellon', 'horse': 'roch'}
#
# # powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}  # TypeError: unhashable type: 'list'
# # Слово «не хэшируемый» в этом контексте означает, что этот «список» - это объект, который можно изменить.
#
# empty_dict = {}  # Мы можем создать пустой словарь следующим образом

####################################################################
# powers = {}
#
# powers ['key'] = 'value' # {'key': 'value'}
# print(powers)
####################################################################

# menu = {"овсянка": 3, "тост с авокадо": 6, "морковный сок": 5, "черничный маффин": 2}
#
# # мы хотим добавить новый товар, «чизкейк» за 8 долларов, мы можем использовать
# menu["чизкейк"] = 8  # {'овсянка': 3, 'тост с авокадо': 6, 'морковный сок': 5, 'черничный маффин': 2, 'чизкейк': 8}
# print(menu)

####################################################################
# Задание
# 1. Создайте пустой словарь с именем animals_in_zoo.
# 2. Гуляя по зоопарку, вы видите 8 зебр. Добавьте «зебры» в animals_in_zoo в качестве
# ключа со значением 8.
# 3. Добавьте «обезьяны» в animals_in_zoo в качестве ключа со значением 12.
# 4. Покидая зоопарк, вы опечалены тем, что не видели динозавров. Добавьте
# "динозавров" в animals_in_zoo в качестве ключа со значением 0.
# 5. Выведите в консоль animals_in_zoo.

# animals_in_zoo = {}
# animals_in_zoo['Зебра'] = 8
# animals_in_zoo['Обезьяны'] = 12
# animals_in_zoo['Динозавры'] = 0
#
# print(animals_in_zoo)  # {'Зебра': 8, 'Обезьяны': 12, 'Динозавры': 0}

####################################################################
# Добавить несколько ключей
# Если мы хотим добавить в словарь сразу несколько пар ключ: значение, мы можем
# использовать метод .update ()

# sensors = {"гостиная": 21, "кухня": 23, "спальня": 20}
# sensors.update({"кладовая": 22, "гостевая": 25, "патио": 34})
#
# print(sensors)  # {'гостиная': 21, 'кухня': 23, 'спальня': 20, 'кладовая': 22, 'гостевая': 25, 'патио': 34}

####################################################################
# Задание
# 1. В одной строке кода добавьте двух новых пользователей в словарь user_ids:
# theLooper, с id of 138475
# stringQueen, с id of 85739

# ser_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
# ser_ids.update({'theLooper': 138475, 'stringQueen': 85739})
#
# print(ser_ids)  # {'teraCoder': 9018293, 'proProgrammer': 119238, 'theLooper': 138475, 'stringQueen': 85739}

####################################################################
# Перезаписать значения
# Мы знаем, что можем добавить ключ, используя такой синтаксис:

# menu = {"овсянка": 3, "тост с авокадо": 6, "морковный сок": 5, "черничный маффин": 2}
#
# menu["тост с авокадо"] = 7
# menu["овсянка"] = 5
# print(menu)

####################################################################
# Задание
# 1. Добавьте ключ «"Supporting Actress"» и установите значение «Viola
# Davis».

# oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
#
# oscar_winners["Supporting Actress"] = 'Viola Davis'
# oscar_winners["Best Picture"] = 'Moonlight'
# print(oscar_winners)

####################################################################
# Понимание словаря
# Допустим, у нас есть два списка, которые мы хотим объединить в словарь, например список
# студентов и список их роста в дюймах:

# names = ['Jenny', 'Alexus', 'Sam', 'Grace']
# heights = [61, 70, 67, 64]
#
# # Python позволяет создавать словарь, используя понимание dict, с таким синтаксисом
# students = {key: value for key, value in zip(names, heights)}
# print(students)

####################################################################
# Задание
# 1. У вас есть два списка, в которых представлены некоторые напитки, продаваемые в
# кафе, и миллиграммы кофеина в каждом. Сначала создайте переменную с именем
# zipped_drinks, которая является итератором пар между списком напитков и
# списком кофеина.
# 2. Создайте словарь с именем drinks_to_caffeine, используя понимание dict, которое
# проходит через итератор zipped_drinks и превращает каждую пару кортежей в
# элемент ключ: значение.

# drinks = ["espresso", "chai", "decaf", "drip"]
# caffeine = [64, 40, 0, 120]
#
# zipped_drinks = zip(drinks, caffeine)
# drinks_to_caffeine = {key: value for key, value in zipped_drinks}
# print(drinks_to_caffeine)  # {'espresso': 64, 'chai': 40, 'decaf': 0, 'drip': 120}

####################################################################
# Задание
# 1. Мы создаем музыкальный стриминговый сервис. Мы предоставили два списка, в
# которых представлены песни в библиотеке пользователя и количество
# воспроизведений каждой песни.
# Используя понимание списка, создайте словарь под названием plays, который проходит
# через zip (песни, playcounts) и создает пару song: playcount для каждой песни в песнях и
# каждого playcount в playcounts.
# 2. Выведите plays.
# 3. После этого добавьте к plays новую запись. Запись должна быть для песни "Purple
# Haze", а количество воспроизведений - 1.
# 4. Этот пользователь заразился лихорадкой Ареты Франклин и прослушал «Respect» 5.
# 5. Создайте словарь, называемый library, который имеет две пары ключ: значение:
# ключ «The Best Songs» со значением plays, словарь, который вы создали
# ключ "Sunday Feelings" со значением пустого словаря
# 6. Выведите library

# songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
# playcounts = [78, 29, 44, 21, 89, 5]
#
# plays = {key: value for key, value in zip(songs, playcounts)}
# # print(plays)
# plays['Purple Haze'] = 1
# # plays["Respect"] += 5  # Берёт значение по ключу и добавляем + к сумме указанной в словаре!!!
# plays.update({'Purple Haze': 1, 'Respect': plays['Respect'] + 5})  # Или поменять значение по ключу 'Respect' в таком варианте!
#
# plays.update({'Purple Haze': 1, 'Respect': 94})  # Или поменять значение напрямую по ключу 'Respect'
# # print(plays)
# library = {'The Best Songs': plays, 'Sunday Feelings': {}}
# print(library)
# print(plays['Purple Haze'])  # Обращаемся напрямую по ключу, чтобы посмотреть значение!

####################################################################
# Получить ключ
# Если у нас есть словарь, можно получить доступ к его значениям, указав ключ. Например,
# представим, что у нас есть словарь, в котором отображается высота зданий в метрах:

# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601,
#                     "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
#
# # Мы можем получить доступ к данным в нем следующим образом
# print(building_heights["Burj Khalifa"])  # 828
# print(building_heights["Ping An"])  # 599

####################################################################
# Задание
# 1. Ниже дан словарь, в котором элементы астрологии соотносятся со знаками зодиака.
# Выведите на консоль список знаков зодиака, связанных со стихией «земля».

# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"],
#                    "fire": ["Aries", "Leo", "Sagittarius"],
#                    "earth": ["Taurus", "Virgo", "Capricorn"],
#                    "air":["Gemini", "Libra", "Aquarius"]}
#
# print(zodiac_elements["fire"])  # ['Aries', 'Leo', 'Sagittarius']
# print(zodiac_elements["earth"])  # ['Taurus', 'Virgo', 'Capricorn']

####################################################################
# Получить недействительный ключ
# Допустим, у нас есть словарь высот зданий из последнего упражнения

# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632,
#                     "Abraj Al Bait": 601, "Ping An": 599,
#                     "Lotte World Tower": 554.5, "One World Trade": 541.3}
#
# # Как быть, если нам нужно узнать высоту Landmark 81 в Хошимине? Можно попробовать
# # Но «Landmark 81» не существует в качестве ключа в словаре building_heights! Таким
# # образом, данный код вызовет KeyError:
# # print(building_heights["Landmark 81"])
#
#
# # Один из способов избежать этой ошибки - сначала проверить, существует ли ключ в словаре
# # В таком виде, код не приведет к ошибке, потому что key_to_check в building_heights
# # вернет False, и поэтому мы никогда не попытаемся получить доступ к ключу.
# key_to_check = "Landmark 81"
# if key_to_check in building_heights:
#     print(building_heights["Landmark 81"])


####################################################################
# Задание
# 1. Запустите код. Он должен выдать KeyError! «energy» не существует как один из
# элементов.
# 2. Добавьте ключевую «energy» к zodiac_elements. Он должен соответствовать
# значению «Not a Zodiac element». Запустите код. Устранен ли KeyError?

# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"],
#                    "fire": ["Aries", "Leo", "Sagittarius"],
#                    "earth": ["Taurus", "Virgo", "Capricorn"],
#                    "air": ["Gemini", "Libra", "Aquarius"],
#                    'energy': ['Not a Zodiac element']}
#
# print(zodiac_elements['energy'])
#
# # Try/Except для получения ключа
# # Мы увидели, что можно избежать KeyErrors, сначала проверив, есть ли ключ в словаре.
# # Другой метод, который возможно использовать, - это try / except:
#
# key_to_check = "Landmark 81"
# try:
#     print(zodiac_elements[key_to_check])
# except KeyError:
#     print("That key doesn't exist!")

####################################################################
# Задание
# 1. Используйте блок try/except чтобы попытаться вывести уровень кофеина в матче.
# Если возникла ошибка KeyError, выведите «Неизвестный уровень кофеина».
# 2. Над блоком try добавьте в словарь «матча» со значением

# caffeine_level = {"эспрессо": 64, "чай": 40, "декаф": 0, "дрип": 120}
# caffeine_level['матча'] = 30
#
# try:
#     print(caffeine_level['матча'])
# except KeyError:
#     print('Неизвестный уровень кофеина')

####################################################################
# Безопасно получить ключ
# В последнем упражнении мы увидели, что для того, чтобы избежать KeyError нам нужно
# добавить в словарь пару ключ: значение. Такое решение не является универсальным и
# устойчивым. Мы не можем предсказать каждый ключ, который понадобится вызвать
# пользователю, и добавить все эти значения-заполнители в наш словарь.
# В словарях есть метод .get () для поиска значения вместо my_dict [key], которую мы
# использовали ранее. Если ключа, который вы пытаетесь использовать .get (), не существует,
# по умолчанию он вернет None:

# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632,
#                     "Abraj Al Bait": 601, "Ping An": 599,
#                     "Lotte World Tower": 554.5, "One World Trade": 541.3, 'Kilimanjaro': 'No Value'}
#
# print(building_heights.get("Shanghai Tower"))  # 632
#
#
# # Также есть возможность указать значение, которое будет возвращено, если ключа не
# # существует. Например, вернуть высоту здания, равную 0, если желаемое здание
# # отсутствует в словаре, можно следующим образом:
#
# print(building_heights.get("My House"))  # None
# print(building_heights.get("My House", 0))  # 0
#
# print(building_heights.get('Kilimanjaro', 'No Value'))  # No Value

####################################################################
# Задание
# 1. Используйте .get (), чтобы получить значение идентификатора пользователя
# teraCoder, со значением по умолчанию 100000, если пользователя не существует.
# Сохраните его в переменной tc_id. Выведите tc_id в консоль.
# 2. Используйте .get (), чтобы получить значение идентификатора пользователя
# superStackSmash, со значением по умолчанию 100000, если пользователь не
# существует. Сохраните его в переменной stack_id. Вывести stack_id в консоль.

# user_ids = {"teraCoder": 100019, "pythonGuy": 182921,
#             "samTheJavaMaam": 123112, "lyleLoop": 102931,
#             "keysmithKeith": 129384}
#
# tc_id = user_ids.get('teraCoder', 100000)
#
# stack_id = user_ids.get('superStackSmash', 100000)


####################################################################
# Удалить ключ
# Иногда возникает необходимость получить ключ и удалить его из словаря. Представьте,
# что проводится розыгрыш, и у нас есть словарь, сопоставляющий номера билетов с
# призами:

# raffle = {223842: "Teddy Bear", 872921: "Concert Tickets",
#           320291: "Gift Basket", 412123: "Necklace",
#           298787: "Pasta Maker"}
#
# # Когда мы получаем номер билета, мы хотим выдать приз, а также удалить эту пару из
# # словаря, поскольку приз уже был выдан. Для этого мы можем использовать .pop (). Как и в
# # случае с .get (), можно предоставить значение по умолчанию, если ключа не существует в
# # словаре:
#
# raffle.pop(320291, "No Prize")
# print(raffle)
#
# raffle.pop(100000, "No Prize")
# print(raffle)
#
# raffle.pop(872921, "No Prize")
# print(raffle)

####################################################################
# Получить все ключи
# Рассмотрим пример, когда нам нужно оперировать всеми ключами в словаре. Например, у
# нас есть словарь учащихся математического класса и их оценок:

# test_scores = {"Grace": [80, 72, 90], "Jeffrey": [88, 68, 81],
#                "Sylvia": [80, 82, 84], "Pedro": [98, 96, 95],
#                "Martin": [78, 80, 78], "Dina": [64, 60, 75]}
#
# # Чтобы получить список учащихся в классе без учета их оценок, можно воспользоваться
# # встроенной функции list ():
#
# print(list(test_scores))  # ['Grace', 'Jeffrey', 'Sylvia', 'Pedro', 'Martin', 'Dina']
#
# # В словарях также есть метод .keys(), который возвращает объект dict_keys. Объект dict_keys
# # - это объект представления, который обеспечивает просмотр текущего состояния словаря
# # без возможности изменения пользователем чего-либо. Объект dict_keys, возвращаемый
# # функцией .keys (), представляет собой набор ключей в словаре. Вы не можете добавлять
# # или удалять элементы из объекта dict_keys, но его можно использовать вместо списка для
# # итерации:
#
# for key in test_scores.keys():
#     print(key)  # Grace
#                     # Jeffrey
#                     # Sylvia
#                     # Pedro
#                     # Martin
#                     # Dina

####################################################################
# Задание
# 1. Создайте переменную с именем users и назначьте ей объект dict_keys для всех
# ключей словаря user_ids
# 2. Создайте переменную с именем classes и назначьте ее объектом dict_keys для всех
# ключей словаря num_exercises.
# 3. Вывести users в консоль.
# 4. Вывести lessons на консоли

# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops":22, "lists": 19, "classes": 18, "dictionaries": 18}
#
# users = list(user_ids.keys())
# print(users)
#
# classes = num_exercises.keys()
# print(classes)

####################################################################
# Получить все значения
# В словарях есть метод .values (), который возвращает объект dict_values (точно так же, как
# объект dict_keys, но для значений!) Со всеми значениями в словаре. Его также можно
# использовать вместо списка для итерации:

# test_scores = {"Катерина": [80, 72, 90], "Даниил": [88, 68, 81],
#                "София": [80, 82, 84], "Павел": [98, 96, 95],
#                "Марк": [78, 80, 78], "Диана": [64, 60, 75]}
#
# # Получаем все ключи в словаре!
# for key in test_scores.keys():
#     print(key)  # Катерина
#     # Даниил
#     # София
#     # Павел
#     # Марк
#     # Диана
#
# # Получаем все значения в словаре!
# for value in test_scores.values():
#     print(value)  # [80, 72, 90]
#     # [88, 68, 81]
#     # [80, 82, 84]
#     # [98, 96, 95]
#     # [78, 80, 78]
#     # [64, 60, 75]
#
# # Встроенной функции для получения всех значений в виде списка не существует, но если
# # действительно необходимо, можно использовать:
#
# list(test_scores.values())

####################################################################
# Задание
# 1. Создайте переменную с именем total_exercises и установите ее равной 0.
# 2. Просмотрите значения в списке num_exercises и добавьте каждое значение в
# переменную total_exercises.
# 3. Выведите в консоль переменную total_exercises

# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15,
#                  "loops":22, "lists": 19, "classes": 18, "dictionaries": 18}
#
# total_num = 0
#
# for num in num_exercises.values():
#     total_num += num


####################################################################
# Получить все пары в словаре
# Вы можете получить как ключи, так и значения с помощью метода .items (). Подобно .keys
# () и .values (), он возвращает объект dict_list. Каждый элемент dict_list, возвращаемый
# функцией .items (), представляет собой кортеж, состоящий из:
# поэтому для итерации вы можете использовать этот синтаксис:

# biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
#
# summ = 0
# for company,value in biggest_brands.items():
#     print(company + ' has a value of ' + str(value) + ' billion dollars. ')
#     summ += value

####################################################################
# Задание
# 1. Ниже представлена колода карт Таро, Таро. Вы собираетесь раскладывать три карты
# своего прошлого, настоящего и будущего.
# Создайте пустой словарь под названием spread.
# 2. Первая карта, которую вы хотите получить, — это карта 13. Извлеките значение,
# присвоенное ключу 13, из словаря Таро и назначьте его как значение «прошедшего»
# ключа распространения.
# 3. Вторая карта, выпадающая вам — это карта 22. Извлеките значение, присвоенное
# ключу 22, из словаря Таро и назначьте его как значение «настоящего» ключа
# распространения.
# 4. Третья карта, которую вы берете, — это карта 10. Извлеките значение, присвоенное
# ключу 10, из словаря Таро и назначьте его как значение «будущего» ключа
# распространения

tarot = { 1: "The Magician", 2: "The High Priestess", 3: "The Empress",
          4: "The Emperor", 5: "The Hierophant", 6: "The Lovers",
          7: "The Chariot", 8: "Strength", 9: "The Hermit",
          10: "Wheel of Fortune", 11: "Justice",12: "The Hanged Man",
          13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower",
          17: "The Star", 18: "The Moon", 19: "The Sun", 20: "Judgement",
          21: "The World", 22: "The Fool"}



####################################################################
#

####################################################################
#

####################################################################
#
