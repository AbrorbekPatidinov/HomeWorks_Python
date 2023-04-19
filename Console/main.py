# Homeworks in Python
import random


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


task_16()

