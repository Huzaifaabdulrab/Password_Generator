import streamlit as Huzaifa
import random
import string
import re

def generate_password(lenght , use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _  in range(lenght))

Huzaifa.title("🔑 Password Generator")

lenght = Huzaifa.slider("Select Password Lenght" , min_value =4 , max_value=50 , value=10 )

use_digits = Huzaifa.checkbox("Include Digits")
use_special = Huzaifa.checkbox("Include Special Characters")

if Huzaifa.button("Generate Passoword"):
    password = generate_password(lenght , use_digits, use_special)
    Huzaifa.write(f"Generated Password : {password}" )
else:
    Huzaifa.write("Please click on the Generate Password button to get your password")

import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    remarks = ""
    
    # Length Check
    if len(password) >= 8:
        strength += 1
        
    # Capital Letter Check
    if re.search(r'[A-Z]', password):
        strength += 1
        
    # Small Letter Check
    if re.search(r'[a-z]', password):
        strength += 1
        
    # Number Check
    if re.search(r'[0-9]', password):
        strength += 1
        
    # Special Characters Check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
        
    if strength == 5:
        remarks = "Strong 🔥"
    elif strength >= 3:
        remarks = "Moderate 👍"
    else:
        remarks = "Weak 😢"
        
    return remarks

st.title("🔑 Password Strength Checker")

password = st.text_input("Enter Your Password", type='password')

if st.button("Check"):
    if password:
        result = check_password_strength(password)
        st.success(f"Password Strength: {result}")
    else:
        st.warning("Please enter a password")

Huzaifa.write("-----------------------------------------------------")

Huzaifa.write("Build with 💖 by [Huzaifa](https://github.com/Huzaifaabdulrab/)") 