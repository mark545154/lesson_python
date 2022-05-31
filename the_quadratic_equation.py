a = float(input('Введите а: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))
if a!=0:
    if b!=0 and c!=0: # Проверяем является уравнение полным
        d = b**2-4*a*c
        print ("Уравнение вида ах**2+b+c = 0")
        if d < 0:
            print ('Нет корней')
        elif d == 0:
            x = (-b/2*a)
            print ("Один корень, х=", x)
        else:
            x1 = (-b+d**0.5)/2*a
            x2 = (-b-d**0.5)/2*a
            print ("Два корня, х1=%s, x2=%s" % (x1, x2))
    elif b!=0 and c==0:
        print ("Уравнение вида ах**2+b = 0")
        x1=0
        x2 = -b/a
        print ("Два корня, х1=%s, x2=%s" % (x1, x2))
    elif b==0 and c > 0:
        if a > 0: print ('Уравнение вида ax**2 +c = 0 не имеет корней')  # уравнение не будет иметь корней, так как квадратный корень нельзя извлечь из отрицательного числа.
        else:
            x1 = -((-c/a)**0.5)
            x2 = (-c/a)**0.5
            print ("'Уравнение вида ax**2 +c = 0. Два корня, х1=%s, x2=%s" % (x1, x2))
    elif b==0 and c < 0:   #
        print ("Уравнение вида ах**2 - c = 0")
        x1 = -((-c/a)**0.5)
        x2 = (-c/a)**0.5
        print ("Два корня, х1=%s, x2=%s" % (x1, x2))
    else: # b==0 & c==0:
        print (" Уравнение вида ах**2 = 0 имеет один корень х = 0")
else:
    print (" Вы задали не квадратное уравнение. Попробуйте еще раз")
