from string import ascii_letters,digits
from random import choice

chars = ascii_letters + digits + "!@#$%&*"

length = int(input("Enter Length Of Your Password : "))

pas = ''

for i in range(length):
    pas = pas + choice(chars)

print("Your Password = " + pas)