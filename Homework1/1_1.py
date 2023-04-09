# Реализуйте 2 метода, чтобы в каждом из них получить разные исключения
# Посмотрите на код, и подумайте сколько разных типов исключений вы тут сможете получить?

import math

# В этой функции я проверяю 3 стороны треугольника на 2 исключения:
# 1.1 - это если передоваемое значение в функцию является строкой, выдаем исключение TypeError
# 1.2 - если в функцию приходит отрицательное число, а треугольник не может быть с отрицатльной стороной мы выдаем исключение ValueError



def calc_square(ab, ac, bc) -> float:
    if isinstance(ab, str) or isinstance(ac, str) or isinstance(bc, str):
        raise TypeError('One of the sides is the string')
    if ab <= 0 or ac <= 0 or bc <= 0:
        raise ValueError('One of the sides is less or equal to 0.')

    p = (ab + ac + bc) / 2
    s = math.sqrt(p * (p-ab) * (p-ac) * (p-bc))
    return s


# по идеи еще можно проверить треугольник на валидность по сторонам, Требуется сравнить каждую сторону с суммой двух других. 
# Если хотя бы в одном случае сторона окажется больше либо равна сумме двух других, то треугольника с такими сторонами не существует.



# В этой функци я проверяю делитель и делимое на:
# 2.1 - это если передоваемое значение в функцию является строкой, выдаем исключение TypeError
# 2.2 - если делитель равен 0 выдаем исключение ZeroDivisionError

def divide(a, b) -> float:
    if isinstance(a, str) or isinstance(b, str):
        raise TypeError('One of the numbers is the string')
    if b == 0:
        raise ZeroDivisionError("The divider can't be equal 0")
    return a/b


if __name__ == "__main__":
    #1.1 TypeError exception
    # square = calc_square('bg', 8, 8)
    # print(square)
    #1.2 ValueError exception
    # square = calc_square(-2, 8, 8)
    # print(square)

    # 2.1 TypeError exception
    # divider = divide('b', 2)
    # print(divider)
    # 2.2 ZeroDivisionError exception
    divider = divide(6, 0)
    print(divider)
