import streamlit as Huzaifa
import random
import string

def generate_password(lenght , use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _  in range(lenght))

Huzaifa.title("Password Generator")

lenght = Huzaifa.slider("Select Password Lenght" , min_value =4 , max_value=50 , value=10 )

use_digits = Huzaifa.checkbox("Include Digits")
use_special = Huzaifa.checkbox("Include Special Characters")

if Huzaifa.button("Generate Passoword"):
    password = generate_password(lenght , use_digits, use_special)
    Huzaifa.write(f"Generated Password : {password}" )
else:
    Huzaifa.write("Please click on the Generate Password button to get your password")

    Huzaifa.write("-----------------------------------------------------")

    Huzaifa.write("Build with 💖 by [Huzaifa](https://github.com/Huzaifaabdulrab/)") 