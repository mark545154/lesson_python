###################################################################################
# Машинное обучение с использованием Scikit-learn (лекция)

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split  # Делит нашу выборку на тестовую и обучающую
from sklearn.metrics import mean_absolute_percentage_error  # MAPE

df = pd.read_csv('Nedvig.csv', delimiter=';', encoding='cp1251')

print(df['Цена, тыс. руб.'].max())
print(df['Цена, тыс. руб.'].min())
print(df['Цена, тыс. руб.'].mean())
print(df['Цена, тыс. руб.'].std())

# Построение диаграммы рассеяния зависимости номера квартиры и цены (выяснили, какому номеру соответствует выброс)
plt.scatter(df.Номер, df['Цена, тыс. руб.'])
plt.show()
# Построение диаграммы рассеяния зависисмость цены от числа комнат
plt.scatter(df['Число комнат'], df['Цена, тыс. руб.'])
plt.show()
# Построение диаграммы рассеяния зависисмость цены от общей площади
plt.scatter(df['Общая'], df['Цена, тыс. руб.'])
plt.show()
# Построение гистограммы по цене
plt.hist(df['Цена, тыс. руб.'], bins=50)
plt.show()

# Сортировка по цене по убыванию (первые строчки - выбросы)
df.sort_values(by=['Цена, тыс. руб.'], inplace=True, ascending=False)
df.reset_index(inplace=True, drop=True)

# Удалили экстремальные значение (первые 2 строки)
df.drop([0, 1], inplace=True)
df.reset_index(inplace=True)

# Построение описательной статистики для очищенных данных (без экстремальных значений)
print(df['Цена, тыс. руб.'].describe())

# Построение гистограммы по цене без выбросов
plt.hist(df['Цена, тыс. руб.'], bins=20)
plt.show()

# Построение нормального распределения для цены
norm_rasp = np.random.normal(df['Цена, тыс. руб.'].mean(), df['Цена, тыс. руб.'].std(), size=10000)
plt.hist(norm_rasp, bins=20)
plt.show()
# Проверка пропущенных значений
print(df.isnull().sum())

# Удаление пропущенных значений
df.dropna(subset=['Общая', 'Жилая', 'Кухня', 'Цена, тыс. руб.'], inplace=True)

print(df.isnull().sum())

# Построение матрицы коэффициентов парной корреляции
sns.heatmap(df.corr(), annot=True, cbar=False)

# Фильтровка однокомнатных квартир в отдельный набор данных
df_1_room = df[df['Число комнат'] == 1]
# Построение описательной статистики для однокомнатных квартир
print(df_1_room.describe())


def lin_reg(x, y):
    # Разделение на тестовую и обучающую выборки. Объем обучающей выборки 90%,
    # параметр random_state фиксирует способ разбиения
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.9, random_state=3)
    # Создание пустой модели линейной регрессии (объект типа линейной регрессии)
    reg = LinearRegression()

    # Обучение модели (подбор параметров линейного уравнения m и b)
    reg.fit(x_train, y_train)
    # Подстановка x_train в уравнение и расчет результата (y расчетный) по обучающей выбоки
    y_pred = reg.predict(x_train)

    # Подстановка x_train в уравнение и расчет результата (y расчетный)
    y_pred2 = reg.predict(x_test)

    # выводим параметр b (сдвиг прямой из уравнения mx+b)
    print(reg.intercept_)  # b

    # выводим коэффициент при x, параметр m (наклон прямой из уравнения mx+b)
    print(reg.coef_)  # m

    # Оценка качества модели, расчет коэффициента детерминации (R^2)
    # Показывает, насколько хорошо x описывает y
    # Изменяется в пределах от 0 до 1. Чем ближе к 1, тем лучше модель
    print(r2_score(y_train, y_pred))

    # Точность модели (отклонение от факта).
    # Показывает, на сколько ошибается модель в процессе прогнозирования
    print(mean_absolute_percentage_error(y_test, y_pred2))  # (abs(y_test-y_pred2))/y_test
    print('====================')
    # plt.plot(x_train[name], y_train, 'o')
    # plt.plot(x_train[name], y_pred)
    # plt.show()
    return y_pred
    # Вызов функции регрессии с параметрами df[['Жилая']] как x, и df['Цена, тыс. руб.'], как y


y = lin_reg(df[['Жилая']], df['Цена, тыс. руб.'])

# Такой же вызов для однокомнатных квартир
y_1_room = lin_reg(df_1_room[['Жилая']], df_1_room['Цена, тыс. руб.'])

###################################################################################
#
# df.sort_values(by=['Цена, тыс. руб.'], inplace=True,
#                ascending=False)  # сортировка по убыванию (ascending=False, если True то возрастание), inplace чтобы не создавать новый датафрейм, изменяет текущий
# df.reset_index(inplace=True, drop=True)
#
# df_clear = df[(df['Цена, тыс. руб.'] > df['Цена, тыс. руб.'].mean() - 5 * sigma) & (df['Цена, тыс. руб.'] < df[
#     'Цена, тыс. руб.'].mean() + 5 * sigma)]  # избавляемся от экстримальных значений (5 станд отклонений)
#
# print(df_clear['Цена, тыс. руб.'].describe())


