###################################################################################
# - - - - - - - Работа с данными с использованием библиотеки NumPy - - - - - - - #
# NumPy и Mean
# Первое статистическое понятие, которое мы рассмотрим, — это среднее значение, также
# обычно называемое средним. Среднее значение - полезное измерение для определения
# центра набора данных. NumPy имеет встроенную функцию для вычисления среднего или
# среднего значений массивов: np.mean
# Предположим, мы хотим найти среднее количество фунтов продукции, которое человек
# покупает в неделю. Мы провели опрос и получили 1000 ответов:


import numpy as np

survey_responses = [5, 10.2, 4, .3, 6.6]
survey_responses = np.array(survey_responses)
print(np.mean(survey_responses))  # 5.220000000000001

###################################################################################
# Задание
# 1. Дистрибьютор напитков Wine Not? Хочет подсчитать, сколько бутылок Bourdeaux он
# продает в среднем у трех местных продавцов вина, чтобы определить, следует ли
# увеличивать свои запасы. Продажи за последнюю неделю для каждого магазина
# перечислены ниже.
# Найдите средние продажи для каждого магазина и сохраните их в переменных
# store_one_avg, store_two_avg и store_three_avg.
# 2. Выведите в консоль все полученные средние
# 3. Обратите внимание на средние продажи в неделю для каждого магазина. Начальник
# говорит, что мы должны увеличивать запасы, но только в том случае, если средние
# продажи в магазине превышают 7 бутылок в неделю.
# Сохраните имя переменной набора данных магазина, которое соответствует этому
# описанию, в переменной best_seller.


import numpy as np

store_one = np.array([2, 5, 8, 3, 4, 10, 15, 5])
store_two = np.array([3, 17, 18, 9, 2, 14, 10])
store_three = np.array([7, 5, 4, 3, 2, 7, 7])

store_one_avg = np.mean(store_one)
print('Средние продажи первого магазина: ', store_one_avg)
store_two_avg = np.mean(store_two)
print('Средние продажи второго магазина: ', store_two_avg)
store_three_avg = np.mean(store_three)
print('Средние продажи третьего магазина: ', store_three_avg)
# best_seller = max(store_one_avg, store_two_avg, store_three_avg)  # можно определить так максимальное значение
# print(best_seller)

if store_one_avg >= 7:
    best_seller = store_one_avg
    print('Продажи первого магазина за 7 дней составляет: ', best_seller)
elif store_two_avg >= 7:
    best_seller = store_two_avg
    print('Продажи второго магазина за 7 дней составляет: ', best_seller)
elif store_three_avg >= 7:
    best_seller = store_three_avg
    print('Продажи третьего магазина за 7 дней составляет: ', best_seller)
else:
    'Продажи не превышают заданного запроса'

###################################################################################
# Средние и логические операции
# Мы также можем использовать np.mean для вычисления процента элементов массива, у
# которых есть определенное свойство.
# Как мы знаем, логический оператор будет оценивать каждый элемент в массиве, чтобы
# убедиться, что он соответствует указанному условию. Если элемент соответствует
# заданному условию, он будет оцениваться как True и равен 1. Если он не соответствует, он
# будет False и равен 0.
# Когда np.mean вычисляет логический оператор, результирующее среднее значение будет
# эквивалентно общему количеству элементов True, разделенному на общую длину массива.
# В нашем примере опроса продукции мы можем использовать этот расчет, чтобы узнать
# процент людей, которые покупали более 8 фунтов продукции каждую неделю:
# Логический оператор survey_array> 8 оценивает, какие ответы на опрос были больше 8, и
# присваивает им значение 1. np.mean складывает все единицы и делит их на длину массива
# survey_array. Полученные результаты говорят нам, что 20% респондентов купили более 8
# фунтов продукции.


import numpy as np

survey_array = [5, 10.2, 4, .3, 6.6]  # .3 это значение 0.3
survey_array = np.array(survey_array)

print('Процент людей, которые покупали более 8 фунтов продукции каждую неделю: ', (np.mean(survey_array > 8) * 100), '%')  # 0.2


###################################################################################
# Задание
# 1. Вы проводите встречу выпускников местного колледжа. У вас есть список с
# именами всех присутствующих и годом, когда они закончили обучение.
# Мы сохранили этот список как массив NumPy в переменной class_year. Подсчитайте
# процент выпускников, получивших высшее образование в 2005 году и позже, и сохраните
# свой результат в переменной миллениалы.


import numpy as np

class_year = np.array([1967, 1949, 2004, 1997, 1953, 1950, 1958, 1974, 1987, 2006,
                       2013, 1978, 1951, 1998, 1996, 1952, 2005, 2007, 2003, 1955,
                       1963, 1978, 2001, 2012, 2014, 1948, 1970, 2011, 1962, 1966,
                       1978, 1988, 2006, 1971, 1994, 1978, 1977, 1960, 2008, 1965,
                       1990, 2011, 1962, 1995, 2004, 1991, 1952, 2013, 1983, 1955,
                       1957, 1947, 1994, 1978, 1957, 2016, 1969, 1996, 1958, 1994,
                       1958, 2008, 1988, 1977, 1991, 1997, 2009, 1976, 1999, 1975,
                       1949, 1985, 2001, 1952, 1953, 1949, 2015, 2006, 1996, 2015,
                       2009, 1949, 2004, 2010, 2011, 2001, 1998, 1967, 1994, 1966,
                       1994, 1986, 1963, 1954, 1963, 1987, 1992, 2008, 1979, 1987])

millenials = np.mean(class_year >= 2005)
print('Процент выпускников получивших высшее образование в 2005 года ', (millenials * 100), '%')

###################################################################################
# Вычисление среднего двумерных массивов
# Если у нас есть двумерный массив, np.mean может вычислить средние значения
# большего массива, а также внутренних значения (под массивов).
# Представим себе игру в бросок кольца на карнавале. В этой игре у вас есть три разных
# шанса собрать все три кольца на палку. В нашем массиве ring_toss каждый внутренний
# массив (массивы в более крупном массиве) — это одна попытка, а каждое число - это один
# бросок кольца. 1 представляет успешный бросок, 0 представляет неудачу.
# Во-первых, мы можем использовать np.mean, чтобы найти среднее значение по всем
# массивам:


import numpy as np

ring_toss = np.array([[1, 0, 0],
                      [0, 0, 1],
                      [1, 0, 1]])

print('Среднее значение по всем массивам: ', np.mean(ring_toss))  # 0.4444444444444444

# Чтобы найти среднее каждого внутреннего массива, мы указываем ось 1 («строки»):
print('Среднее каждого внутреннего массива: ', np.mean(ring_toss, axis=1))  # [0.33333333 0.33333333 0.66666667]

# Чтобы найти среднее значение каждой позиции индекса (т.е. среднее значение всех
# первых бросков, среднее значение всех вторых бросков и т.д.), мы указываем ось 0 («столбцы»):
print('Среднее значение каждой позиции индекса: ', np.mean(ring_toss, axis=0))  # [0.66666667 0.         0.66666667]

###################################################################################
# Задание
# 1. Мы предоставили данные об испытании нового лекарства от аллергии
# AllerGeeThatSucks! Пятерых участников попросили оценить, насколько сонливыми
# они были в результате приема лекарства, раз в день в течение трех дней по шкале от
# одного (наименьшая сонливость) до десяти (наибольшая сонливость).
# Используйте np.mean, чтобы найти средний уровень сонливости по всем испытаниям и
# сохранить результат в переменной total_mean
# 2. Используйте np.mean, чтобы найти средний уровень сонливости за каждый день
# эксперимента, и сохраните его в переменной trial_mean.
# 3. Используйте np.mean, чтобы найти средний уровень сонливости для каждого
# отдельного пациента, чтобы увидеть, были ли некоторые из них более
# чувствительны к препарату, чем другие, и сохраните его в переменной Patient_mean.
# 4. Выведите в консоль все значения средних


import numpy as np

allergy_trials = np.array([[6, 1, 3, 8, 2],
                           [2, 6, 3, 9, 8],
                           [5, 2, 6, 9, 9]])

total_mean = np.mean(allergy_trials)
print('Средний уровень сонливости по всем испытаниям: ', round(total_mean, 2))

trial_mean = np.mean(allergy_trials, axis=1)
print('Средний уровень сонливости за каждый день эксперимента: ', list(trial_mean))

patient_mean = np.mean(allergy_trials, axis=0)
print('Средний уровень сонливости для каждого отдельного пациента: ', list(patient_mean))

# print(total_mean, trial_mean, patient_mean)

###################################################################################
# Сортировка и выбросы
# Один из способов быстро выявить выбросы — это отсортировать наши данные. После
# сортировки данных мы можем быстро взглянуть на начало или конец массива, чтобы
# увидеть, не лежат ли некоторые значения далеко за пределами ожидаемого диапазона. Мы
# можем использовать функцию NumPy np.sort для сортировки наших данных.
# Вернемся к нашему примеру с ростом в третьем классе и представим, что восьмиклассник
# вошел в наш эксперимент:
# Если мы воспользуемся np.sort, мы сразу сможем идентифицировать более высокого
# ученика, поскольку его рост (62 дюйма) заметно выходит за пределы диапазона набора
# данных:


import numpy as np

heights = np.array([49.7, 46.9, 62, 47.2, 47, 48.3, 48.7])

heights = np.sort(heights)
print('Наш отсортированный массив со значениями: ', list(heights))


###################################################################################
# Задание
# 1. Вы отслеживали данные о температуре летом на своем заднем крыльце, но поняли,
# что разместили датчик прямо над решеткой! Прежде чем вы сможете использовать
# свои данные, вам нужно проверить, не вызвало ли тепло от гриля каких-либо
# странных показаний, которые могли бы исказить ваши данные.
# Сначала отсортируйте массив данных temps и сохраните отсортированные данные в
# переменной sorted_temps.


import numpy as np

temps = np.array([86, 88, 94, 85, 97, 90, 87, 85, 94, 93, 92, 95, 98, 85, 94, 91,
                  97, 88, 87, 86, 99, 89, 89, 99, 88, 96, 93, 96, 85, 88, 191, 95,
                  96, 87, 99, 93, 90, 86, 87, 100, 187, 98, 101, 101, 96, 94, 96,
                  87, 86, 92, 98, 94, 98, 90, 99, 96, 99, 86, 97, 98, 86, 90, 86,
                  94, 91, 88, 196, 195, 93, 97, 199, 87, 87, 90, 90, 98, 88, 92,
                  97, 88, 85, 94, 88, 93, 198, 90, 91, 90, 92, 92])

sorted_temps = np.sort(temps)
print('Наш отсортированный массив с данными: ', sorted_temps)

###################################################################################
# NumPy и медиана
# Еще один ключевой показатель, который мы можем использовать при анализе данных, —
# это медиана. Медиана — это среднее значение набора данных, упорядоченного по величине
# (от наименьшего к наибольшему).


import numpy as np

temps = np.array([1, 1, 2, 3, 4, 5, 5])

print('Медиана нашего массива [1, 1, 2, 3, 4, 5, 5] будет равна: ', np.median(temps))  # 3.0

my_array = np.array([1, 1, 2, 3, 4, 5, 5, 6])  # 3.5
print('Медиана в массиве [1, 1, 2, 3, 4, 5, 5, 6] будет равна: ', np.median(my_array))

my_array2 = np.array([50, 38, 291, 59, 14])
print('Наш отсортированный массив: ', np.sort(my_array2))  # [ 14  38  50  59 291]
print('Медиана в массиве [50, 38, 291, 59, 14] будет равна: ', np.median(my_array2))  # 50.0

###################################################################################
# Задание
# 1. Вы исследуете семейные доходы и наткнулись на следующий небольшой набор
# данных:
# Вычислите медиану, не используя Numpy, и сохраните значение в переменной
# small_set_median.
# 2. По мере того как вы продолжаете свое исследование, вы обнаруживаете кладезь
# исследований в файле home_income.csv (данные ниже), который необходимо
# поместить в переменную large_set.
# Используйте NumPy, чтобы найти медиану large_set и сохранить результат в переменной
# large_set_median.
# 3. Вывести полученные результаты в консоль


import statistics

small_set_median = ([10100, 35500, 105000, 85000, 25500, 40500, 65000])
small_set_median = statistics.median(small_set_median)
print('Медиана нашего массива с использованием библиотеки statistics, будет равна: ', small_set_median)  # 40500


import numpy as np

large_set = np.genfromtxt('home_income.csv', delimiter='.')
large_set = np.median(large_set)
print('Медиана из нашего файла с использованием библиотеки Numpy, будет равна: ', large_set)  # 86502.5


###################################################################################
# Задание
# 1. Компания, в которой вы работаете, хочет знать среднее количество времени, которое
# кто-то проводит на веб-сайте компании в минутах. На основании данных ниже
# создайте файл CSV. Импортируйте этот набор данных в вашу программу как
# time_spent
# 3. Найдите среднее количество времени в минутах, проведенных на веб-сайте, и
# сохраните его в переменной minutes_mean.
# 4. Теперь найдите медианное значение массива и сохраните его в переменной
# minutes_median.
# 5. Теперь найдите медианное значение массива и сохраните его в переменной
# minutes_median.
# 6. Выведите значение среднего и медианы в консоль
# 7. Обратите внимания на разницу между двумя значениями. Как вы думаете, какой из
# них лучше всего отражает большинство имеющихся данных?
# Выберите переменную, представляющую это значение, и сохраните ее в переменной
# best_measure.


import numpy as np

minutes = np.genfromtxt('time_spent.csv', delimiter='.')
minutes_mean = np.mean(minutes)
print('Среднее количество времени в минутах, проведенных на веб-сайте: ', round(minutes_mean, 2))  # 7.661904761904762

minutes_median = np.median(minutes)
print('Медианное значение массива: ', minutes_median)  # 2.0

best_measure = minutes_mean - minutes_median
print('Значение среднего и медианы: ', best_measure)  # 5.661904761904762


###################################################################################
# Процентили, часть I
# Как мы знаем, медиана — это середина набора данных: это число, для которого 50%
# выборок находятся ниже, а 50% выборок - выше. Но что, если бы мы хотели найти точку, в
# которой 40% образцов находятся ниже, а 60% образцов находятся выше?
# Этот тип точки называется процентилем. N-й процентиль определяется как точка N%
# выборок, лежащих ниже него. Таким образом, точка, в которой ниже 40% выборок,
# называется 40-м процентилем. Процентили - полезные измерения, потому что они могут
# сказать нам, где находится конкретное значение в более крупном наборе данных.
# Давайте посмотрим на следующий массив:
# В наборе данных 11 чисел. 40-й процентиль будет иметь 40% из 10 оставшихся чисел под
# ним (40% от 10 равно 4) и 60% чисел над ним (60% от 10 равно 6). Итак, в этом примере
# 40-й процентиль равен 4.


import numpy as np

d = [1, 2, 3, 4, 4, 4, 6, 6, 7, 8, 8]
d = np.array(d)
d = np.percentile(d, 40)

print('40-й процентиль из нашего массива [1, 2, 3, 4, 4, 4, 6, 6, 7, 8, 8] будет равен: ', d)  # 4.0


###################################################################################
# Задание
# 1. Местная публичная библиотека хочет узнать, сколько часов в неделю их посетители
# используют компьютеры. Вверху script.py мы включили образцы данных от 11
# пользователей в массив NumPy
# Используйте NumPy, чтобы найти 30-й процентиль отсортированного массива и сохранить
# его в переменной с именем thirtieth_percentile.
# 2. Затем используйте NumPy, чтобы найти 70-й процентиль и сохранить его в
# переменной seventieth_percentile.
# 3. Выведите в консоль результаты расчета


import numpy as np

patrons = np.array([2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])
thirtieth_percentile = np.percentile(patrons, 30)
print('30-й процентиль из нашего массива будет равен: ', thirtieth_percentile)  # 3.0

seventieth_percentile = np.percentile(patrons, 70)
print('70-й процентиль из нашего массива будет равен: ', seventieth_percentile)  # 8.0

###################################################################################
# Процентили, часть II
# Некоторые процентили имеют определенные имена:
# • 25-й процентиль называется первым квартилем.
# • 50-й процентиль называется медианой.
# • 75-й процентиль называется третьим квартилем.
# Минимум, первый квартиль, медиана, третий квартиль и максимум набора данных
# называются сводкой из пяти чисел. Этот набор чисел отлично подходит для вычисления,
# когда мы получаем новый набор данных.
# Разница между первым и третьим квартилями — это величина, называемая
# межквартильным размахом. Например, допустим, у нас есть следующий массив

import numpy as np

num_mas = [1, 2, 3, 4, 4, 4, 6, 6, 7, 8, 8]

# Мы можем вычислить 25-й и 75-й процентили, используя np.percentile
d = np.percentile(num_mas, 25)
print('25-й процентиль из нашего массива будет равен: ', d)

result = np.percentile(num_mas, 75)
print('75-й процентиль из нашего массива будет равен: ', result)

# Затем, чтобы найти межквартальный размах, мы вычитаем значение 25-го процентиля из значения 75-го
result = result - d
print('Межквартальный размах будет равен: ', result)

# 50% набора данных будет находиться в пределах межквартального диапазона.
# Межквартальный размах дает нам представление о разбросе наших данных. Чем меньше
# значение межквартального размаха, тем меньше разброс в нашем наборе данных. Чем
# больше значение, тем больше дисперсия.

###################################################################################
# Задание
# 1. Компания стриминговый сервис фильмов хочет знать, сколько фильмов
# пользователи смотрят за одну неделю. Мы включили образцы данных от 15
# пользователей в массив
# Найдите 25-й и 75-й процентили и сохраните их в соответствующих переменных:
# first_quarter и 3rd_quarter.
# 2. Создайте переменную с именем interquartile_range. Вычислите межквартальный
# размах и сохраните его в этой переменной.
# 3. Вывести в консоль результаты


import numpy as np

movies_watched = np.array([2, 3, 8, 0, 2, 4, 3, 1, 1, 0, 5, 1, 1, 7, 2])
first_quarter = np.percentile(movies_watched, 25)
print('25-й процентиль из нашего массива будет равен: ', first_quarter)  # 1.0

rd_quarter = np.percentile(movies_watched, 75)
print('75-й процентиль из нашего массива будет равен: ', rd_quarter)  # 3.5

interquartile_range = first_quarter - rd_quarter
print('Межквартальный размах будет равен: ', interquartile_range)  # -2.5


###################################################################################
# NumPy и стандартное отклонение, часть II
# Как мы видели в последнем упражнении, знание стандартного отклонения набора данных
# может помочь нам понять, насколько разбросан наш набор данных.
# Мы можем найти стандартное отклонение набора данных с помощью функции Numpy
# np.std:


import numpy as np

nums = np.array([65, 36, 52, 91, 63, 79])
nums = np.std(nums)
print('Стандартное отклонение набора данных из нашего массива будет равно: ', nums)  # 17.716909687891082

###################################################################################
# Задание
# 1. Вас попросили оценить ежегодный фестиваль сквоша в вашем городе. Организатор
# фестиваля дает вам список, в котором указаны все веса для двух соревнований,
# которые вы судите: тыквы и желудевые сквоши.
# Учитывая два набора данных, найдите средний вес для каждого соревнования и сохраните
# его в переменных pumpkin_avg и acorn_squash_avg.
# 2. Теперь остальные судьи хотят, чтобы вы дали им представление о том, насколько
# репрезентативны средние значения по отношению к полноте представленных
# материалов. Вычислите стандартное отклонение для каждого набора данных, чтобы
# найти и сохранить их в переменных pumpkin_std и acorn_squash_std. Выведите их на
# консоль, чтобы увидеть их значения.
# 3. Определите набор данных сквоша, который имеет большее стандартное
# отклонение, и сохраните его для переменной winner.


import numpy as np

pumpkin = np.array([68, 1820, 1420, 2062, 704, 1156, 1857, 1755, 2092, 1384])
acorn_squash = np.array([20, 43, 99, 200, 12, 250, 58, 120, 230, 215])

pumpkin_avg = np.mean(pumpkin)
print('Средний вес для соревнования сквоши тыквы будет равен: ', pumpkin_avg)

acorn_squash_avg = np.mean(acorn_squash)
print('Средний вес для соревнования желудевые сквоши будет равен: ', acorn_squash_avg)

pumpkin_std = np.std(pumpkin)
print('Стандартное отклонение сквоши тыквы равно: ', (round(pumpkin_std, 2)))

acorn_squash_std = np.std(acorn_squash)
print('Стандартное отклонение желудевые сквоши равно: ', (round(acorn_squash_std, 2)))

winner = max(pumpkin_std, acorn_squash_std)
print('Набор данных сквоша, который имеет большее стандартное отклонение: ', (round(winner, 2)))

###################################################################################
# Задание
# 1. Группа ученых собирала данные об осадках в Сиэтле. Они представили вам свои
# данные в виде среднемесячных значений, измеряемых в дюймах.
# Сохраните эти данные в массиве NumPy rainfall.
# 2. Найдите среднее значение массива осадков и сохраните его в переменной rain_mean.
# 3. Найдите медианное значение массива осадков и сохраните его в переменной
# rain_median.
# 4. Найдите 25-й и 75-й процентили исходного массива осадков и сохраните их в
# массивах first_quarter и third_quarter соответственно.
# 5. Вычислите межквартальный размах и сохраните его в переменном межквартальном
# размахе.
# 6. Определите стандартное отклонение набора и сохраните его в переменной rain_std.
# 7. Вывести результаты в консоль


import numpy as np

rainfall = np.array([5.21, 3.76, 3.27, 2.35, 1.89, 1.55, 0.65, 1.06, 1.72, 3.36, 4.82, 5.11])
rain_mean = np.mean(rainfall)
print('Среднее значение массива осадков: ', rain_mean)

rain_median = np.median(rainfall)
print('Медианное значение массива осадков', rain_median)

first_quarter = np.percentile(rainfall, 25)
print('25-й процентиль исходного массива осадков: ', first_quarter)

third_quarter = np.percentile(rainfall, 75)
print('75-й процентиль исходного массива осадков: ', third_quarter)

interquartile_quarter = first_quarter - third_quarter
print('Межквартальный размах будет равен: ', interquartile_quarter)

rain_std = np.std(rainfall)
print('Стандартное отклонение набора, будет равно: ', rain_std)

###################################################################################
# Дан набор данных по ценам на недвижимость (столбцы обозначают Общую площадь,
# жилую площадь, площадь кухни, цену на квартиру в тыс.руб.). Необходимо:
# 1. Найти максимум и минимум
# 2. Найти среднее значение
# 3. Найти моду и медиану
# 4. Разделить набор данных на три отдельных набора данных по признаку квартир
# (отдельно однокомнатные, двухкомнатные, четырёхкомнатные)
# 5. Рассчитать показатели из 1–4 пункта для каждого из наборов данных
# 6. Отсортировать по убыванию цены
# Максимальная общая площадь квартиры
# Максимальная жилая площадь квартиры
# Максимальная площадь кухни
# Максимальная цена квартиры % тыс. руб.


import numpy as np

data_list = np.genfromtxt('Nedvig2.csv', delimiter=';')
np.set_printoptions(suppress=True)
# print(data_list)

# Найти максимум
max_val = np.max(data_list, axis=0)
# print('Максимальная общая площадь квартиры: ', max_val[0])
# print('Максимальная жилая площадь квартиры: ', max_val[1])
# print('Максимальная площадь кухни: ', max_val[2])
# print('Максимальная цена квартиры ', max_val[3], ' тыс. руб.')

# Найти минимум
min_val = np.min(data_list, axis=0)
# print(min_val)
# print('Минимальная общая площадь квартиры: ', min_val[0])
# print('Минимальная жилая площадь квартиры: ', min_val[1])
# print('Минимальная площадь кухни: ', min_val[2])
# print('Минимальная цена квартиры ', min_val[3], ' тыс. руб.')

# Найти среднее значение
average_value = np.mean(data_list, axis=0)
# print(average_value)
# print('Средняя общая площадь квартиры: ', round(average_value[0], 2))
# print('Средняя жилая площадь квартиры: ', round(average_value[1], 2))
# print('Средняя площадь кухни: ', round(average_value[2], 2))
# print('Средняя цена квартиры ', round(average_value[3], 2), ' тыс. руб.')

# Найти моду
moda_val = [data_list[3] * data_list[0] for index in range(len(data_list))]
# print(moda_val)

# Найти медиану
median_val = np.median(data_list, axis=0)
# print(median_val)
# print('Медиана общей площади квартиры: ', median_val[0])
# print('Медиана жилой площади квартиры: ', median_val[1])
# print('Медиана площади кухни: ', median_val[2])
# print('Медиана цены квартиры ', median_val[3], ' тыс. руб.')

# Разделить набор данных на три отдельных набора данных по признаку квартир
# (отдельно однокомнатные, двухкомнатные, четырёхкомнатные)


# Рассчитать показатели из 1–4 пункта для каждого из наборов данных


# Отсортировать по убыванию цены
