import random

passSymbols = ["/", "!", "?", "*", "$", "-", "_", "#", "&", "<", ".", ",", "|", "%", ">", "@", "`"]

passAlp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

pasAlpMini = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

passNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

passLength = int(input("Длина вашего пароля: "))

quantity_password = int(input("Колличество паролей: "))

for i in range(quantity_password):
    password = "".join(
        [
            str(random.choice(passAlp + pasAlpMini + passNum + passSymbols))
            for i in range(passLength)
        ]
    )
    print("Пароль👉: ", password)
