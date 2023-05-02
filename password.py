import random

passAlp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "/", "!", "?", "*", "$", "-", "_"]
pasAlpMini = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
passNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

passLength = 15

password = ''.join([str(random.choice(passAlp + pasAlpMini + passNum))
                   for i in range(passLength)])

print("Пароль👉: ", password)
