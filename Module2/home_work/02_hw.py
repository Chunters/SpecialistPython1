# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

print("Enter natural number")
number_of_cow = int(input("Количество коров: "))
variant_name = [2, 0, 1, 1, 1, 2]
cow_name = ['корова', 'коровы', 'коров']
if 4 < number_of_cow % 100 < 20:
    print(number_of_cow, cow_name[2])
elif number_of_cow % 10 < 5:
    print(number_of_cow, cow_name[variant_name[number_of_cow % 10]])
else:
    print(number_of_cow, cow_name[variant_name[5]])
