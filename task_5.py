"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны
войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления
произведения всех элементов списка.Подсказка: использовать функцию reduce().
"""
from functools import reduce

def my_list(el_1, el_2):
    return el_1 * el_2
new_list = [el for el in range(100, 1001, 2)]
print(f"List\n{new_list}\nMultiplication of numbers\n{reduce(my_list, new_list)}")
