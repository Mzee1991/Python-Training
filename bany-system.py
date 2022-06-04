#  EDGARS DUKA
#  R00103479
# Please uncomment line 36 for testing purposes only

import random

def main():
    print("Welcome To A Banking System")
    name_list, acc_num_list, acc_blc_list = read_file()
    option = 0
    while option != 6:

        # displaying option menu
        banking_menu = ["1. Open Account", "2. Close Account", "3. Withdraw Money",
                        "4. Deposit Money", "5. Report for Management", "6. Quit"]

        for option in banking_menu:
            print(option)
        user_input = False

       # validation for user input
        while not user_input:
            try:
                option = int(input("Please enter an option:"))
                if 0 < option < 7:
                    user_input = True
                else:
                    print("\nPlease enter a number greater than 0 and less than 7\n")
                    for option in banking_menu:
                        print(option)
            except:
                print("\nError -- Please enter a number between 1 to 6 only\n")
                for option in banking_menu:
                    print(option)

        print(name_list + acc_num_list + acc_blc_list)

# if statement for all of the options
        if option == 1:
            name_list, acc_num_list, acc_blc_list = open_acc(name_list, acc_num_list, acc_blc_list)

        elif option == 2:
            name_list, acc_num_list, acc_blc_list = shutdown_acc(name_list, acc_num_list, acc_blc_list)

        elif option == 3:
            name_list, acc_num_list, acc_blc_list = cash_out(name_list, acc_num_list, acc_blc_list)

        elif option == 4:
            name_list, acc_num_list, acc_blc_list = add_money(name_list, acc_num_list, acc_blc_list)

        elif option == 5:
            report(name_list, acc_num_list, acc_blc_list)

        elif option == 6:
            exit(name_list, acc_num_list, acc_blc_list)


# Functions for all of the switch statement
def read_file():
    name_list = []
    acc_num_list = []
    acc_blc_list = []

# reading the text file
    f = open("bank.txt", "r")
    lines = f.readlines()
    for line in lines:
        information = line.split()
        acc_num_list.append(information[0])
        acc_blc_list.append(float(information[1]))
        name_list.append(information[2])
    return name_list, acc_num_list, acc_blc_list


# Function for opening an account
def open_acc(name_list, acc_num_list, acc_blc_list):
    name = input("Please enter your name:")
    print("Your name:", name)
    name_list.append(name)
    # found = True
    # while found:
    number = str(random.randint(1, 1000000))
    # check the number
    print("your account number:", number)
    acc_num_list.append(number)
    acc_blc_list.append(0.0)
    return name_list, acc_num_list, acc_blc_list


# Function for closing an account
def shutdown_acc(name_list, acc_num_list, acc_blc_list):
    account_number = input("\nEnter your account number:\n")
    index = 0
    found = False
    for i in acc_num_list:
        if i == account_number:
            found = True
            break
        index = index + 1
    if found:
        print("\nSorry to see you go", name_list[index], "\n")
        # deletes the 3 lists from their index position.
        del acc_num_list[index]
        del acc_blc_list[index]
        del name_list[index]

    else:
        print("\nError -- No account exists under the number you provided\n")
    return name_list, acc_num_list, acc_blc_list


# Function for Withdrawing money from an account
def cash_out(name_list, acc_num_list, acc_blc_list):
    account_number = input("\nEnter your account number:\n")
    index = 0
    found = False
    for i in acc_num_list:
        if i == account_number:
            found = True
            break
        index = index + 1
    if found:
        problem = True
        while problem:
            try:
                withdraw_amount = float(input("Enter the amount you want to withdraw:"))
                # The Amount is the new amount the customer has withdrawn
                if withdraw_amount < 0:  # if not a positive int print message and ask for input again
                    print("ERROR -- input must be a positive integer, try again")
                    break
                amount = acc_blc_list[index] - withdraw_amount
                # if the amount is greater than or = 0 it will take the amount away from the balance list.
                if amount > 0:
                    acc_blc_list[index] = acc_blc_list[index] - withdraw_amount
                    print("An amount of ", "€", format(withdraw_amount, ".2f"), " is removed from your account ",
                          account_number,
                          sep="")
                    print("Your current balance is ", "€", format(acc_blc_list[index], ".2f"), sep="")
                    print("")
                    problem = False
                else:
                    print("Unfortunately you don't have a sufficient funds",
                          name_list[index])
                    print("Your balance after your current transaction is ", "€",
                          format(acc_blc_list[index], ".2f"), sep="")
                    print("")
                    break
            finally:
                return name_list, acc_num_list, acc_blc_list
    else:
        print("\n Sorry that account number does not exist \n")
        return name_list, acc_num_list, acc_blc_list


# Function for depositing an amount to an account
def add_money(name_list, acc_num_list, acc_blc_list):
    account_number = input("\nEnter your account number:\n")
    index = 0
    found = False
    for i in acc_num_list:
        if i == account_number:
            found = True
            break
        index = index + 1
    if found:
        problem = True
        while problem:
            try:
                deposit_amount = float(input("Enter the amount you want to deposit:"))
                # The Amount of customer chooses to deposit
                if deposit_amount < 0:  # if not a positive int print message and ask for input again
                    print("ERROR -- input must be a positive integer, try again")
                    break
                amount = acc_blc_list[index] + deposit_amount
                # if the amount is greater than or = 0 it will added to the balance list.
                if amount > 0:
                    acc_blc_list[index] = acc_blc_list[index] + deposit_amount
                    print("An amount of ", "€", format(deposit_amount, ".2f"), " is added from your account ",
                          account_number,
                          sep="")
                    print("Your current balance is ", "€", format(acc_blc_list[index], ".2f"), sep="")
                    print("")
                    problem = False
                else:
                    print("Error -- Please enter a positive number",
                          name_list[index])
                    print("Your balance after your current transaction is ", "€",
                          format(acc_blc_list[index], ".2f"), sep="")
                    print("")
                    break
            finally:
                return name_list, acc_num_list, acc_blc_list
    else:
        print("\n Sorry that account number does not exist \n")
        return name_list, acc_num_list, acc_blc_list


# Function to display a report for all the accounts details
def report(name_list, acc_num_list, acc_blc_list):
    for i in range(len(acc_num_list)):
        print("\nClient ", name_list[i], " who's account number is ", acc_num_list[i], "has €", acc_blc_list[i])
        total = sum(acc_blc_list)
    print("\nTotal amount of deposit in the system is", format(total, ".2f"))
    largest_deposit = max(acc_blc_list)
    print("\nThe largest amount of deposit in the system is €", str(largest_deposit), "and it belongs to " + (name_list[i] + "\n"))


def exit(name_list, acc_num_list, acc_blc_list):
    print("Thank You For Using Our Banking System")
    quit_file = open("bank.txt", "w")
    for i in range(len(acc_num_list)):
        save = acc_num_list[i] + " " + str(acc_blc_list[i]) + " " + name_list[i] + "\n"
        quit_file.write(save)
    quit_file.close()


main()
