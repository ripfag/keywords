def max_number(a, b):
    if a > b:
        return a
    return b


def empty_function():
    pass


def even_numbers(n):
    for numbers in range(0, n + 1, 2):
        yield numbers


def max_number_check():
    assert max_number(1, 1) == 1, "Числа равны!"
    assert max_number(5, 4) == 5, "Ошибка, 5 > 4"
    assert max_number(100, 1000) == 1000, "Ошибка, 1000 > 100"
    assert max_number(-20, 10) == 10, "Ошибка, 10 > -20"


max_number_check()
print("Тесты пройдены!")
print(max_number(10,20))
for num in even_numbers(20):
    print(num)


