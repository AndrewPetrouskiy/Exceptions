    # public static void main(String[] args) throws Exception {
    #     try {
    #         int a = 90; 
    #         int b = 3;          - тут можно сделать проверку на деление на 0
    #         System.out.println(a / b);
    #         printSum(23, 234);
    #         int[] abc = { 1, 2 };      
    #         abc[3] = 9;         
    #     } catch (Throwable ex) {  - вот это исключение САМОЕ ГЛАВНОЕ И ОТ НЕГО НАСЛЕДУЮТСЯ все остальные исключения!!!!!!!!!!
    #         System.out.println("Что-то пошло не так...");
    #     } catch (NullPointerException ex) {
    #         System.out.println("Указатель не может указывать на null!");
    #     } catch (IndexOutOfBoundsException ex) {
    #         System.out.println("Массив выходит за пределы своего размера!");
    #     }
    # }
    # public static void printSum(Integer a, Integer b) throws FileNotFoundException {  - это исключение не нужно т.к мы не работаем с файлом
    #     System.out.println(a + b);
    # }
try:

    def printSum(a, b):
        print(a+b)
    

    a = 90
    b = 3
    print(a/b)
    printSum(23, 234)
    abc = [1,2]
    abc.insert(3, 9)
except ZeroDivisionError as ex:
    print(f"Catching exception: {ex}")
except IndexError as ex:
    print("Массив выходит за пределы своего размера!")  #массивы в python динамические так что такой ошибки тут не будет
except TypeError as ex:
    print("Указатель не может указывать на None!")  # тут это не выполняется т.к. нет тут значений с None
# можно было бы просто вместо всех этих исключений использовать аналог
    # } catch (Throwable ex) 
    # System.out.println("Что-то пошло не так..."); - но в таком случае не понятно какое именно исключение тут было поймано и залогировано
