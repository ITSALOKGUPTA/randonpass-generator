import random
import string
print("Welcome to our Random Password Generator")
def main_function():
    length=int (input("Enter the length of password you want: "))
    lowerD=string.ascii_lowercase
    upperD=string.ascii_uppercase
    digitD=string.digits
    symbolsD=string.punctuation
    combine=lowerD+upperD+digitD+symbolsD
    x=random. sample (combine, length)
    password="". join(x)
    print(password)
    main_function()
main_function()
