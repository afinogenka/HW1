import time
import math


def first_decorator(func):
    func()
    time_zero = time.time()
    time_to_complete = time.time() - time_zero
    print(f"Была вызвана функция {func.__name__} Затраченное время {time_to_complete}")


a = float(input('введите длину: '))
b = float(input('введите ширину: '))


@first_decorator
def feet_to_acres():
    area = a * b
    acr = area * 0.00002295684113830358
    print(f'Плошадь в акрах =  {acr}')


vzero = 0
acceler = 9.8
dist = float(input('Введите высоту в метрах: '))


@first_decorator
def free_fall():
    vtouchdown = math.sqrt(vzero ** 2 + 2 * acceler * dist)
    print(f"V при соприкосновении объекта с землей {vtouchdown}")