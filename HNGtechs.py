from random import choice
from string import ascii_letters


employee_data = []

def main():
    question=input("\nNew employee? (Type Y for Yes and N for No): ")
    cont=True
    while cont:
        #convert all strings to uppercase
        if question.upper()=="Y":
            return Create_password()
        elif question.upper()=="N" and employee_data!=[]:

            print("\nThese Are The Newly Registered Employee(s)\n")
            for employee in employee_data:
                print(f"\nHello {employee['First name']} {employee['Last name']},\n Your email address is: "
                      f"{employee['email address']} \nAnd your password is: {employee['Password']}\n")
            print("\nThank you. Bye!")
            break
        elif question.upper()=="N" and employee_data==[]:
            print("\nWe only Register new Employee. Bye!")
            break
        else:

            question=input("\nNew employee? (Type Y for Yes and N for No): ")



def employee_info():
    print("\nWelcome To HNG Tech!, Please provide us with some details.\n")

    first = str(input("\nPlease Enter your First name: "))
    last = str(input("\nPlease Enter your Last name: "))
    email_address = str(input("\nPlease Enter your Email address: "))
    first_name=first.title()
    last_name=last.title()
    email=email_address.lower()

    employee_details = {
        "First name": first_name,
        "Last name": last_name,
        "email address": email
        }
    employee_data.append(employee_details)
    return employee_details, employee_data

def Create_password():

    details, data =employee_info()
    password=details["First name"][0:2]+details["Last name"][-2:]+''.join(choice(ascii_letters) for x in range(5))
    print(f"\nBased on our suggestion {details['First name']}, your password is {password}\n")

    while True:
        new_password=str(input("\nDo you like this Suggested Password? (Type Y for Yes and N for No): "))
        if new_password.upper()=="Y":

            print(" \nRegistration Successful. Thank you for registering!\n")
            break

        elif new_password.upper()=="N":
            change_password=str(input("\nPlease enter your desired password. Make sure that it has atleast 7 characters: "))

            while len(change_password)<7:
                change_password=str(input("\nPlease enter your desired password. Make sure that it has atleast 7 characters: "))
            else:
                password=change_password
                print("\nThank you for registering!")
                break
        else:
            print("\nRetry Process again ")
    details["Password"]=password

    return data, main()


main()
