# Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку. 
# Пользователю должно показаться сообщение, что пустые строки вводить нельзя.

def get_string():
    while True:
        reply = input("Enter a text  ")
        if len(reply) == 0 or reply.isspace():
            raise Exception("The string can't be empty and has only space")
        continue




text = get_string()
print(text)