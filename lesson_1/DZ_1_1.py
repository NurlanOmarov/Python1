# Задача 1.1
# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

min = 60
hour = 3600
day = 86400
duration = int(input('Введите продолжительность в секундах: '))
if duration < min:
    print(duration, 'сек')
elif min <= duration < hour:
    print(duration // min, 'мин', duration % min, 'сек' )
elif hour <= duration < day:
    print(duration // hour, 'час', duration % hour // min, 'мин', duration % min, 'сек')
else:
    print(duration // day, 'дн', duration % day // hour, 'час', duration % hour // min, 'мин', duration % min, 'сек')