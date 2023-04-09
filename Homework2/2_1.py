# Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float), и возвращает введенное значение.
# Ввод текста вместо числа не должно приводить к падению приложения, вместо этого, необходимо повторно запросить у пользователя ввод данных.

def get_number():
    while True:
        try:
            reply = float(input("Enter a float number ... "))
            if float(reply):
                return reply
        except ValueError as ex:
            print("Not a number... Try again")



if __name__ == "__main__":
    float_number = get_number()
    print(float_number)