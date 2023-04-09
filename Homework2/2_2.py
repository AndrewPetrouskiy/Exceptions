# Задание 2
# try {
#    int d = 0;
#    double catchedRes1 = intArray[8] / d;
#    System.out.println("catchedRes1 = " + catchedRes1);
# } catch (ArithmeticException e) {
#    System.out.println("Catching exception: " + e);
# }
# Исправить код
# тут не хватает еще несколько exception: 
# длина массива может быть меньше
# массив хоть и может называться intArray, но значения там могут быть не обязательно int,он может быть строковы и сюда же можно добавить и None

try:
    int_array = [4,5,7]
    d = 0
    catchedRes1 = int_array[8] / d
    print(f"catchedRes1 =  + {catchedRes1}")
except ZeroDivisionError as ex:
    print(f"Catching exception: {ex}") 
except IndexError as ex:
    print(f"Catching exception: {ex}") 
except TypeError as ex:
    print(f"Catching exception: {ex}")
 


