# Импортируем модуль для рандома
import random

passSymbols = [" ", "!", "'", "$", "%", "(", "&", ")", "[", "]", "{", "}", "?", "/", "|", ".", ",", "*", "^", ";", ":", "<", ">", "#", "@", "+", "_", "-", "=", "`", "~"]

passAlpMini = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Массив для больших букв получаем из маленьких методом upper()
passAlp = [char.upper() for char in passAlpMini]

# Массив для цифр
passNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Запрашиваем длину пароля
passLength = int(input("Длина вашего пароля: "))

# берем по рандому символы из всех массивов для пароля
password = ''.join([str(random.choice(passAlpMini + passAlp + passNum + passSymbols))
                   for i in range(passLength)])

# Выводим наш сочный пароль
print("Пароль👉: ", password)
