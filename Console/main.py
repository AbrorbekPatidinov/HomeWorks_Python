# Homeworks in Python

# Задача 2: Найдите сумму цифр трехзначного числа.
def summ_of_three_numbers(a, b, c):
    print("Task №2")
    print("Summ of three numbers: ", a + b + c)


# summ_of_three_numbers(1, 2, 3)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
def petya_katya_seryozha_made_paper_cranes(s, x, k):
    print("Task №4")
    s = int(input())
    x = s // 6
    k = (x + x) * 2
    print("Cranes are: ", x, k, x)


# petya_katya_seryozha_made_paper_cranes(2, 2, 4)


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
def lucky_ticket():
    print("Task №6")
    a = input("Enter your numbers on your ticket: ")
    sum_1 = int(a[0]) + int(a[1]) + int(a[2])
    sum_2 = int(a[3]) + int(a[4]) + int(a[5])
    if sum_1 == sum_2:
        print("Lucky numbers ) !")
    else:
        print("I apologize, but your number is not lucky ( ")


# lucky_ticket()


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
def chocolate_task():
    print("Task №8")
    n = int(input("Enter chocolate columns: "))
    m = int(input("Enter chocolate rows: "))
    k = int(input("Enter chocolate piece to take: "))
    if k < n * m and ((k % n == 0) or (k % m == 0)):
        print("Yes you can take !")
    else:
        print("My apologize, but you can't take or even eat the chocolate !")


# chocolate_task()

