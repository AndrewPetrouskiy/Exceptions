# Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, 
# и возвращающий новый массив, каждый элемент которого равен разности элементов двух входящих массивов в той же ячейке. 
# Если длины массивов не равны, необходимо как-то оповестить пользователя.

from random import randint

class InvalidLengthArrays(Exception):
    '''When length of two arrays is different'''

def different_of_two_arrays(arr1: list, arr2:list) -> list:
    if len(arr1) != len(arr2):
        raise InvalidLengthArrays("The length these two arrays isn't the same")
    diff_arr = []
    for i in range(len(arr1)):
        diff_arr.append(arr1[i] - arr2[i])
    return diff_arr


if __name__ == "__main__":
    # with exception
    arr1= [randint(10, 50) for _ in range(11)]
    print(arr1)
    arr2= [randint(10, 50) for _ in range(10)]
    print(arr2)
    dif_arr = different_of_two_arrays(arr1=arr1, arr2=arr2)
    print(dif_arr)

    # without exception
    # arr1= [randint(10, 50) for _ in range(10)]
    # print(arr1)
    # arr2= [randint(10, 50) for _ in range(10)]
    # print(arr2)
    # dif_arr = different_of_two_arrays(arr1=arr1, arr2=arr2)
    # print(dif_arr)