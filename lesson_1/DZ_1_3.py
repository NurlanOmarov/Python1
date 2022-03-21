# Зададча 1.3
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

percent = int(input('Введите число процента: '))
if percent == 11:
    print(percent, 'процентов')
elif percent % 10 == 1:
    print(percent, 'процент')
elif percent % 10 == 2 or percent % 10 == 3 or percent % 10 == 4:
    print(percent, 'процента')
else:
    print(percent, 'процентов')