import string

phone_number = input("Enter a 7-digit phone number, excluding 1 and 0: ")

while not phone_number.isdigit():
    phone_number = input("Enter a 7-digit phone number, excluding 1 and 0: ")
print(phone_number)

key = 3
letters = string.ascii_uppercase
trans = letters[key:] + letters[:key]
word_generated = phone_number.translate(str.maketrans(letters, trans))



