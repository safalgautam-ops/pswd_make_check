import re
import secrets
import string
import os

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

#file path for storage
storage_File = "password.txt"

#function to store password 
def pwd_saver(service,password):
    with open(storage_File,"a") as file:
        file.write(f"Service:{service} | Password:{password} \n")
    print("Saved Successfully!")


#taking user input
def main():
    user_input = int(input("Which of the service you want to use? \n 1. Generating Password \n 2. Saving Password \n 3. Checking Password Strength \n :"))
    if (user_input == 3):
    #password checker
        password = input("Enter your password: ")
        strength = check_pswd_strength(password)
        print (f"Your password strength is {strength}")

    elif (user_input == 1):
    #password generator
        lengthof_pwd = int(input("Enter the length of password you want to generate of: "))
        generated_pwd = password_generator(lengthof_pwd)
        print(f"Your password is {generated_pwd}")
    
    elif (user_input == 2):
    #password storage
        service = input("Enter the service name of password: ")
        pwd = input("Enter the password to save")
        pwd_saver(service,pwd)
    
    else:
        print("Please Enter Correct Number")


#this runs when executed directly
if __name__ == "__main__" :
    main()