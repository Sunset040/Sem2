# Ex1
x = int(input("Число X: "))
y = int(input("Число Y: "))

def findMax(x, y):
    if x < y:
        return y
    else:
        return x

def findMin(x, y):
    if x > y:
        return y
    else:
        return x

if x == y:
    print("Цифры одинаковые")
else:
    max = findMax(x, y)
    min = findMin(x, y)
    while (max is not min):
        if max % 3 == 0 and max % 2 == 0:
            print(max)
        max -= 1




# Ex 2
max_first = 0
max_second = max_first - 1

iteration = int(input("Введите количество чисел: "))

for i in range(0, iteration):
    number = int(input("Введите число: "))

    if max_first > max_second and number > max_first:
        max_second = max_first
        max_first = number

print("Первое максимальное число = ", max_first)
print("Второе максимальное число = ", max_second)




# Ex 3
n1 = 25
n2 = 10
n3 = 3
n4 = 1

number = int(input("Введите зп: "))

if number >= n1:
    count_n1 = number // n1
    number = number - count_n1 * n1
    print(count_n1, " штук ", n1, " рублевых")

if number >= n2:
    count_n2 = number // n2
    number = number - count_n2 * n2
    print(count_n2, " штук ", n2, " рублевых")

if number >= n3:
    count_n3 = number // n3
    number = number - count_n3 * n3
    print(count_n3, " штук ", n3, " рублевых")

if number >= n4:
    count_n4 = number // n4
    number = number - count_n4 * n4
    print(count_n4, " штук ", n4, " рублевых")



# Ex4
result = "упорядочена по возрастанию"

number = input("Введите многозначное чило: ")
array = list(number)
prevNumber = int(number[0])

for i in array:
    if int(i) < prevNumber:
        result = "не упорядочено по возрастанию"
        break

print(number, result)
