def is_prime(func):
    """
    Декоратор для проверки, является ли результат функции простым числом.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Вызываем исходную функцию и получаем результат
        # Проверяем, является ли результат простым числом
        if result < 2:
            print("Составное")  # Числа меньше 2 не являются простыми
        else:
            for i in range(2, int(result**0.5) + 1):
                if result % i == 0:
                    print("Составное")  # Если число делится на i, оно составное
                    break
            else:
                print("Простое")  # Если не нашли делителей, число простое
        return result  # Возвращаем результат сложения

    return wrapper  # Возвращаем обертку

@is_prime
def sum_three(a, b, c):
    """
    Функция для сложения трех чисел.
    """
    return a + b + c

# Пример использования
result = sum_three(2, 3, 6)  # Сложение чисел
print(result)  # Выводим результат сложения