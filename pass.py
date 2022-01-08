import random
rand_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()abcdefghijklmnopqrstuvwxy1234567890!@#$%^&*()"
pas_out = ""
pas_out_one = ""
pas_out_two = ""
inp_num = int(input("How many letters in password: "))
print()
choice = input("do yuu need some special word in between the password (y/n)")

if choice.lower().strip() == "y":
    want_char = input("pleas enter what character you want to see inside your password: ")
    counter = 0
    for c in want_char:
        counter += 1
    # print(counter)
    if counter > inp_num:
        print("your character length is more than the length of the password you decided :(")
    else:
        left_digit = inp_num - counter
        # print(left_digit)
        if left_digit % 2 == 0:
            left_digit_o = int(left_digit/2)
            for x in range(0, left_digit_o):
                out_choice_one = random.choice(rand_list)
                pas_out_one = pas_out_one + out_choice_one

            for x in range(0, left_digit_o):
                out_choice_two = random.choice(rand_list)
                pas_out_two = pas_out_two + out_choice_two
            print()
            print("\033[0;37;40m your random password is (1.2.0):  " + (pas_out_one+want_char+pas_out_two))
        else:
            left_digit_a = int(left_digit/2)
            left_digit_added = left_digit_a + 1

            for x in range(0, left_digit_added):
                out_choice_one = random.choice(rand_list)
                pas_out_one = pas_out_one + out_choice_one

            for x in range(0, left_digit_a):
                out_choice_two = random.choice(rand_list)
                pas_out_two = pas_out_two + out_choice_two

            print("\033[0;37;40m your random password is (1.3.0):  " + (pas_out_one + want_char + pas_out_two))

elif choice.lower().strip() == "n" or choice.lower().strip() == "":
    for x in range(0, inp_num):
        out_choice = random.choice(rand_list)
        pas_out = pas_out + out_choice

    print()
    print("\033[0;37;40m your random password is (1.2.0):  " + pas_out)

else:
    print("pleas enter y/n")
