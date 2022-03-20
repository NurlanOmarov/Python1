#Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
#Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
#К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#* Решить задачу под пунктом b, не создавая новый список.


my_list = []
for num in range(1, 1001, 2):
    my_list.append(num ** 3)
total_sum = 0
for num in my_list:
    sub_sum = 0
    for sub_num in str(num):
        total_sum += int(sub_num)
    if sub_sum % 7 == 0:
        total_sum += num
print(total_sum)

total_sum = 0
for num in my_list:
    num += 17
    sub_sum = 0
    for sub_num in str(num):
        sub_sum += int(sub_num)
    if sub_sum % 7 == 0:
        total_sum += num
print(total_sum)