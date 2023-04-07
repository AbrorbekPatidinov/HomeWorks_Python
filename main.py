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

