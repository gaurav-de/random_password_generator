import random  
import numpy
import pyperclip
source_ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()abcdefghijklmnopqrstuvwxy1234567890!@#$%^&*()"
counter = temp_num = 0
temp_1 = temp_2 = blank = temp_3 = ""

def choose_odd_eve(a, mid, i, o, p):
    if a % 2 == 0:
        b = generator(i, o, p)
        q = generator(i, o, p)
    else:
        g = i + 1
        b = generator(g, o, p)
        q = generator(i, o, p)
    return b + mid + q
    saving(b + mid + q)

def saving(t_1, t_2, t_3):
    pyperclip.copy((t_1 + t_2 + t_3))
    spam = pyperclip.paste()
    print("Copies Successfully! ")

def generator(password_length, password_1, source):
    for x in range(0, password_length):
        random_password = random.choice(source)
        password_1 += random_password
    return password_1

def show_menu():
    print("*******))-OTHER_OPTIONS-((*******")
    print("1. custom character in center   (>_<)(1)")
    print("2. custom character in left      (_<)(2)")
    print("3. custom character in right     (>_)(3)")
    print("4. custom character shuffled    (<>_)(4)")

password_length_by_user = int(input("How much length you want of your password: "))
print("")
SpecialChoice = input("do yuu need some special word in between the password (y/n)")

if SpecialChoice.lower().strip() == "y":
    want_char = input("pleas enter what character you want to see inside your password: ").strip()
    for c in want_char:
        counter += 1
    left_digit = password_length_by_user - counter
    half_left_digit = int(left_digit / 2)
    print("")
    show_menu()
    input_choice_choice = int(input("enter your choice here: "))
    if input_choice_choice == 1:
        temp_1 = choose_odd_eve(left_digit, want_char, half_left_digit, blank, source_)
        print("\033[0;37;40m your password is: " + temp_1)
        saving(temp_1, "", "")
    elif input_choice_choice == 2 or input_choice_choice == 3:
        temp_1 = generator(left_digit, blank, source_)
        if input_choice_choice == 2:
            print("\033[0;37;40m your password is: " + (want_char + temp_1))
            saving(want_char, temp_1, "")
        else:
            print("\033[0;37;40m your password is: " + (temp_1 + want_char))
            saving(temp_1, want_char, "")
    elif input_choice_choice == 4:
        str_var = list(want_char)
        numpy.random.shuffle(str_var)
        temp_3 = ''.join(str_var)
        temp_1 = choose_odd_eve(left_digit, temp_3, half_left_digit, blank, source_)
        print("\033[0;37;40m your password is: " + temp_1)
        saving(temp_1, "", "")

elif SpecialChoice.lower().strip() == "n" or SpecialChoice.lower().strip() == "":
    temp_1 = generator(password_length_by_user, blank, source_)
    print("\033[0;37;40m your simple password is: " + temp_1)
    saving(temp_1, "", "")
