# Таможенные отчисления
# Входные данные
age = float(input('Возраст авто: '))
volume = int(input('Объем двигателя (куб.см.): '))
price = int(input('Цена авто (евро): '))

# Основной расчет
if age < 3:  # Расчёт для авто моложе 3-х лет
    if price < 16700:
        # bet=2.5
        result_calc = 2.5 * volume
    elif price >= 16700 and price < 42300:
        # bet=5.5
        result_calc = 5.5 * volume
    elif price >= 42300 and price < 84500:
        # bet=7.5
        result_calc = 7.5 * volume
    elif price >= 84500 and price < 169000:
        # bet=15
        result_calc = 15 * volume
    else:
        # bet=20
        result_calc = 20 * volume
        # result_calc = volume * bet
    print('Таможенные отчисления на ваш автомобиль составят: ', result_calc)
elif age >= 3 and age <= 5:
    if volume < 1000:
        # bet=1.5
        result_calc = 1.5 * volume
    elif volume >= 1000 and volume < 1500:
        # bet=1.7
        result_calc = 1.7 * volume
    elif volume >= 1500 and volume < 1800:
        # bet=2.5
        result_calc = 2.5 * volume
    elif volume >= 1800 and volume < 2300:
        # bet=2.7
        result_calc = 2.7 * volume
    elif volume >= 2300 and volume < 3000:
        # bet=3
        result_calc = 3 * volume
    else:
        # bet=3.6
        result_calc = 3.6 * volume
        # result_calc = volume * bet
    print('Таможенные отчисления на ваш автомобиль составят: ', result_calc)
else:pass