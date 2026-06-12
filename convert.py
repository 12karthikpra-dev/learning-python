def convert_temperature():
    print("which conversion do you want to choose:-")
    print("1. celcius to faranheit")
    print("2. faranheit to celcius")
    choice = int(input("enter your choice"))
    if choice == 1:
        temp = float(input("enter the temp in celcius:\t"))
        print(f"{temp} degree celcius is equal to {(temp*9/5)+2} degree in faranheit")
    elif choice == 2:
        temp = float(input("enter the temperature in faranheit:\t"))
        print(f"{temp} dgree in faranheit is equal to {(temp-32)*5/9} degree in celcius")
    else:
        print("INVALID INPUT....")

def convert_currency():
    print("which conversion do you want to choose: ")
    print("1. Dollars to pound")
    print("2. Pounds to Dollars")
    choice = int(input("Enter currency in dollar: "))
    if choice == 1:
        value = float(input("enter the currency in dollars:-\t"))
        print(f"{value} dollars in pounds will be {value*0.73}")
    elif choice == 2:
        value = float(input("enter currency in pounds:-\t"))
        print(f"{value} pounds in dollars will be {value/0.73}")
    else:
        print("INVALID INPUT...")

def convert_lengths():
    print("Which conversion do you want to choose:-")
    print("1. Centimeters to foot and inches")
    print("2. Foot and inches to Centimeters")
    choice = int(input("Enter your choice:-\t"))
    if choice == 1:
        value = float(input("Enter length in cms:\t"))
        inches = value/2.54
        feet = inches/12
        print(f"{value}centimters is equal to {feet} foot and {inches} inches")
    elif choice == 2:
        feet = float(input("enter length in feet:-\t"))
        inches = float(input("enter length in inches:-\t"))
        length = (feet*12 + inches)*2.54
        print(f"{feet}feet and{inches} inches in centers will be {length}cms")
    else:
        print("INVALID INPUT...")

print("==== WELCOM TO VALUE CONVERTER ====")
while 1:
    print("which option you would like to choose:")
    print("1. convert temperature")
    print("2. convert currency")
    print("3. convert lengths")
    choice = int(input("enter your choice:_\t"))
    if choice == 1:
        convert_temperature()
    elif choice == 2:
        convert_currency()
    elif choice == 3:
        convert_lengths()
    else:
        print("INVALID INPUT....")

    