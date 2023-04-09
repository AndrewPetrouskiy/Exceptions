# * Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив, 
# каждый элемент которого равен частному элементов двух входящих массивов в той же ячейке. Если длины массивов не равны, 
# необходимо как-то оповестить пользователя. 
# Важно: При выполнении метода единственное исключение, которое пользователь может увидеть - RuntimeException, т.е. ваше.


from random import randint

class InvalidLengthArrays(Exception):
    '''When length of two arrays is different'''

def different_of_two_arrays(arr1: list, arr2:list) -> list:
    if len(arr1) != len(arr2):
        raise InvalidLengthArrays("The length these two arrays isn't the same")
    diff_arr = []
    for i in range(len(arr1)):
        if arr1[i] == None or arr2[i] == None:
            raise TypeError("One or more of the elements in the arrays is None")
        if isinstance(arr1[i], str) or isinstance(arr2[i], str):
            raise TypeError('One or more of the elements in the arrays is the string')
        if arr2[i] == 0:
            raise ZeroDivisionError("The divider can't be equal 0")
        diff_arr.append(round(arr1[i] / arr2[i], 2))
    return diff_arr


if __name__ == "__main__":
    # with exceptions

# InvalidLengthArrays 
    # arr1= [randint(10, 50) for _ in range(11)]
    # print(arr1)
    # arr2= [randint(10, 50) for _ in range(10)]
    # print(arr2)
    # dif_arr = different_of_two_arrays(arr1=arr1, arr2=arr2)
    # print(dif_arr)

# ZeroDivisionError
    # arr1= [randint(10, 50) for _ in range(10)]
    # print(arr1)
    # arr2= [randint(0, 2) for _ in range(10)]
    # print(arr2)
    # dif_arr = different_of_two_arrays(arr1=arr1, arr2=arr2)
    # print(dif_arr)

# TypeError
    # arr1= [randint(10, 50) for _ in range(10)]
    # print(arr1)
    # arr2= ['a',5,3,8,5,2,9,44,2,9]
    # print(arr2)
    # dif_arr = different_of_two_arrays(arr1=arr1, arr2=arr2)
    # print(dif_arr)

# TypeError with None
    # arr1= [randint(10, 50) for _ in range(10)]
    # print(arr1)
    # arr2= [None,5,3,8,5,2,9,44,2,9]
    # print(arr2)
    # dif_arr = different_of_two_arrays(arr1=arr1, arr2=arr2)
    # print(dif_arr)


# without exception
    arr1= [randint(10, 50) for _ in range(10)]
    print(arr1)
    arr2= [randint(10, 50) for _ in range(10)]
    print(arr2)
    dif_arr = different_of_two_arrays(arr1=arr1, arr2=arr2)
    print(dif_arr)