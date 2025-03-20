import re
import secrets
import string

#function for finding strength
def check_pswd_strength(password):
    strength_score = 0

    #criteria checks
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    number_criteria = bool(re.search(r"\d", password))
    special_char_criteria = bool(re.search(r"[!@#$%^&*()_+\-=\[\]{};':\\|,.<>/?]", password))
    double_quote_criteria = bool(re.search(r'"', password))

    #scoring
    if length_criteria:
        strength_score+=1
    if lowercase_criteria:
        strength_score+=1
    if uppercase_criteria:
        strength_score+=1
    if number_criteria:
        strength_score+=1
    if special_char_criteria or double_quote_criteria:
        strength_score+=1
    
    #strength_evulation
    if strength_score == 5:
        return "Very Strong"
    elif strength_score == 4:
        return "Strong"
    elif strength_score == 3:
        return "Moderate"
    elif strength_score == 2:
        return "Weak"
    else:
        return "Very Weak"

#function for generating passwords
def password_generator(l):
    pwd = "".join(secrets.choice(string.ascii_letters+string.digits) for i in range(l))
    return pwd

#function to store password 

#taking user input
def main():
    #password checker
    password = input("Enter your password: ")
    strength = check_pswd_strength(password)
    print (f"Your password strength is {strength}")

    #password generator
    lengthof_pwd = int(input("Enter the length of password you want to generate of"))
    generated_pwd = password_generator(lengthof_pwd)
    print(f"Your password is {generated_pwd}")



#this runs when executed directly
if __name__ == "__main__" :
    main()