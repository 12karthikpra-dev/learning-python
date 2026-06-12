 import string
 import getpass

 def check_password_strength(password):
    lower_alpha_count = upper_alpha_count = number_count = whitespace_count = special_count = 0
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_alpha_count += 1
        elif char in string.ascii_uppercase:
            upper_alpha_count += 1
        elif char in string.digits:
            number_count += 1
        elif char == ' ':
            whitespace_count += 1
        else:
            special_char_count += 1
        strength = 0
        remarks = ''

        if lower_alpha_count >= 1:
            strength += 1
        if upper_alpha_count >= 1:
            strength += 1
        if number_count >= 1:
            strength += 1
        if whitespace_count >= 1:
            strength += 1
        if special_char_count >= 1:
            strength += 1

        if strength == 1:
            remarks = "that's a very weak password, try another"
        elif strength == 2:
            remarks = "that's not a good password, try another"
        elif strength == 3:
            remarks = "password is okay, but make it harder"
        elif strength == 4:
            remarks = "password can be more tough"
        else:
            remarks = "now that's one hell of a strong password !!! "

        print("YOUR PASSWORD HAS :- ")
        print(f"{lower_alpha_count} lowercase letters")
        print(f"{upper_alpha_count} uppercase letters")
        print(f"{number_count} digits")
        print(f"{whitespace_count} whitespaces")
        print(f"{special_char_count} special characters")
        print(f"password score: {strength}/5")
        print(f"remarks: {remarks}")

print("====WELCOME TO PASSWORD STRENGTH CHECKER====")
while 1:
    choice = input("do you want to check your password (y/n):\t")
    if 'y' in choice.lower():
        password = getpass.getpass("enter the password:\t")
        check_password_strength(password)
    elif 'n' in choice.upper():
        print('exiting...')
        break
    else:
        print("INVALID INPUT...")



