import random
import string


password = ""
passwordLength = 12

letters = string.ascii_letters
digits = string.digits
specialChars = string.punctuation

alphabet = letters + digits + specialChars

for i in range(passwordLength):
    password += "".join(random.choice(alphabet))
print(password)