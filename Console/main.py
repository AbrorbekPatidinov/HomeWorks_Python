# Homeworks in Python
import random
import re

# Задача 2: Найдите сумму цифр трехзначного числа.
def task_2(a, b, c):
    print("Task №2")
    print("Summ of three numbers: ", a + b + c)


# task_2(1, 2, 3)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
def task_4(s, x, k):
    print("Task №4")
    s = int(input())
    x = s // 6
    k = (x + x) * 2
    print("Cranes are: ", x, k, x)


# task_4(2, 2, 4)


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
def task_6():
    print("Task №6")
    a = input("Enter your numbers on your ticket: ")
    sum_1 = int(a[0]) + int(a[1]) + int(a[2])
    sum_2 = int(a[3]) + int(a[4]) + int(a[5])
    if sum_1 == sum_2:
        print("Lucky numbers ) !")
    else:
        print("I apologize, but your number is not lucky ( ")


# task_6()


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
def task_8():
    print("Task №8")
    n = int(input("Enter chocolate columns: "))
    m = int(input("Enter chocolate rows: "))
    k = int(input("Enter chocolate piece to take: "))
    if k < n * m and ((k % n == 0) or (k % m == 0)):
        print("Yes you can take !")
    else:
        print("My apologize, but you can't take or even eat the chocolate !")


# task_8()


#  Задача 10:
#  На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
# некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно
# перевернуть
def task_10():
    print("Task №10")
    n = int(input())
    coin_zero = 0
    coin_one = 0
    for i in range(n):
        other = int(input("Enter the side of the coin (0 or 1): "))
        if other == 1:
            coin_one += 1
        else:
            coin_zero += 1
    if coin_one > coin_zero:
        print("Coins with '1' is more than '0' !")
    else:
        print("Coins with '0' is more than '1' !")


# task_10()


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
def task_12():
    print("Task №12")
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))
    for i in range(number_1):
        for j in range(number_2):
            if number_1 == i + j and number_2 == i * j:
                print("Guessed numbers are: ", i, j)


# task_12()


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
def task_14():
    print("Task №14")
    n = int(input("Enter number: "))
    index = 0
    while 2 ** 1 <= n:
        print(2 ** index)
        index += 1


# task_14()


# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
def task_16():
    print("Task №16")
    x = int(input("Enter number (from 1 to 10): "))
    n = []
    for i in range(1, 10):
        n.append(random.randint(1, 10))
    if x in n:
        result = n.count(x)
        print("Numbers are: ", n)
        print("Your number: ", x)
        print("Count: ", result)
    else:
        print("There is no number such as you entered !")


# task_16()


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
def task_18():
    print("Task №18")
    count = abs(int(input("Enter count of elements in list A: ")))
    a_entered = input("Enter elements to list by spacing: ").split()
    a_number = list(map(int, a_entered))
    if len(a_number) != count or count == 0:
        print("Entered elements are not corresponded to declared quantity !")
    else:
        x = int(input("Enter the number x, with which to compare the elements of the list: "))
        minimum = abs(x - a_number[0])
        index = 0
        for i in range(1, count):
            count = abs(x - a_number[i])
            if count < minimum:
                minimum = count
                index = i
        print(
            f"Number {a_number[index]} in list A more near in number {x}, their difference is {abs(x - a_number[index])}")


# task_18()


# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
def task_20():
    print("Task №20")
    letters_english = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
    letters_russian = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФШЪ'}
    words = input("Enter word in english or in Russian: ")
    if words[0].lower() in letters_english:
        summ = 0
        for letter in words:
            for key, value in letters_english.items():
                if letter.upper() in value:
                    summ += key
        print("The cost of english word: ", summ)
    else:
        if words[0].lower() in letters_russian:
            summ = 0
            for letter in words:
                for key, value in letters_russian.items():
                    if letter.upper() in value:
                        summ += key
            print("The cost of english word: ", summ)


# task_20()


# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
def task_22():
    mol = [int(x) for x in input().split()]
    n = mol[0]
    m = mol[1]
    set_1 = set()
    set_2 = set()
    list_1 = list()
    a = [int(x) for x in input().split()]
    k = set(a)
    for i in k:
        set_1.add(i)
    b = [int(x) for x in input().split()]
    k1 = set(b)
    for i in k1:
        set_2.add(i)
    lok = set_1 & set_2
    kool = list(lok)
    kool.sort()
    for i in kool:
        print(i, end=' ')


# task_22()


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод
# — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
def task_24():
    n = int(input())
    arr = list()
    for index in range(n):
        x = int(input())
        arr.append(x)

    arr_count = list()
    for index in range(len(arr) - 1):
        arr_count.append(arr[index - 1] + arr[index] + arr[index + 1])
    arr_count.append(arr[-1] + arr[-1] + arr[0])
    print(max(arr_count))


# task_24()


# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
def task_26(a, b):
    if b == 0:
        return 1
    else:
        return a * task_26(a, b - 1)


# a = int(input("Enter the number: "))
# b = int(input("Enter the degree: "))
# result = task_26(a, b)
# print("Result is: ", result)


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
def task_28(a, b):
    if b == 0:
        return a
    else:
        return task_30(a + 1, b - 1)


# print(task_30(5, 3))
# print(task_30(10, 10))


# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
def task_30():
    a1 = int(input("Enter the first element: "))
    d = int(input("Enter the difference: "))
    n = int(input("Enter the count of elements: "))
    for i in range(n):
        print(a1 + i * d)


# task_32()


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
def task_32():
    list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    min_number = int(input("Enter the minimum number: "))
    max_number = int(input("Enter the maximum number: "))
    for i in range(len(list_1)):
        if min_number <= list_1[i] <= max_number:
            print(i)


# task_32()

# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
def task_34():
    poem = input("Введите стихотворение: ")
    syllables_count = []
    for phrase in poem.split():
        syllables_count.append(len(re.findall(r'[аеёиоуыэюя]', phrase, re.IGNORECASE)))
    if len(set(syllables_count)) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")

# task_34()


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
def print_operation_table_task_36(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        row = ''
        for j in range(1, num_columns + 1):
            row += str(operation(i, j)) + ' '
        print(row.strip())


# print_operation_table_task_36(lambda x, y: x * y)



