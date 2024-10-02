print('  -*-*-*-*-   ')
print("-->CBA BANK<--")
print("   ><><><     ")

a = input("ENTER YOUR NAME: ")
print("WELCOME SIR", a)

#while True:
#    b = input("ENTER YOUR CODE:")
#    if b == "54":
#        print("Your code is proceeding")
#        break
#    else:
#i        print("Please try again.")

while True:
    print("-*-*-*-*-*-*-*")
    print("-->CBA BANK<--")
    print("><_><_><_><_><")

    print("""
    OPTIONS:
    1. Create a new account
    2. Change password
    3. Transfer money
    4. Change address
    5. Block/delete account
    6. Change cell number
    """)

    x = input("ENTER YOUR OPTION:")

    if x == '1':
        print("You want to create your bank account.")
        e = input("ENTER YOUR NAME: ")
        age = int(input("ENTER YOUR AGE: "))
        if age < 18:
            print("Your age is under 18, so you are not able to create your account.")
            continue  # Go back to the options menu
        else:
            s = input("ENTER YOUR C N I C NUMBER:")
            def address():
             d=input("ENTER YOUR ADDRESS: ")
            r=int(input("ENTER YOUR NUMBER: "))
     #   while True:
            # Add some cash in the account
            u = int(input("ADD SOME CASH IN YOUR ACCOUNT: "))
            if u >= 10000:
                 print("YOUR CASH IS ENTERED SUCCESSFULLY.\nSIR",e)

            elif u <10000:
                print("ADD SOME CASH LESS THAN OR EQUAL TO 10,000.")
                continue

            # Generate a random password
            import random

            password = [
                "4321", "7601", "5613", "9970", "5372", "5248", "4733", "0193", "3216", "7695",
                "3617", "1029", "4169", "7834", "1267", "2390", "2271", "4100", "1067", "6908",
                "5634", "3965", "4590", "4312", "2154", "3469", "6996", "6900", "7856", "1221", "4343"
            ]
            print("YOUR BANK ACCOUNT PASSWORD IS:")
            print(random.choice(password))
            print("FROM CBA BANK: \n thank you sir! for using our services.\n i hope you can't face any problem,any time...\n THANKS.")
            break

    elif x == '2':
        passwords = [
            "4321", "7601", "5613", "9970", "5372", "5248", "4733", "0193", "3216", "7695",
            "3617", "1029", "4169", "7834", "1267", "2390", "2271", "4100", "1067", "6908",
            "5634", "3965", "4590", "4312", "2154", "3469", "6996", "6900", "7856", "1221",
            "4343"
        ]
        def change_password():
            print("YOU WANT TO CHANGE YOUR PASSWORD.")
            name = input("ENTER YOUR NAME: ")
            cell_number = int(input("ENTER YOUR CELL NUMBER: "))
          #  address()
            a= input("ENTER YOUR ADDRESS: ")

            old_password = input("ENTER YOUR OLD PASSWORD: ")
            if old_password in passwords:
                print("YOUR PASSWORD IS CORRECT.")
                new_password = input("ENTER YOUR NEW PASSWORD: ")
                passwords.append(new_password)
                print("PASSWORD CHANGED SUCCESSFULLY.\nSIR!",name)
            else:
                print("YOUR PASSWORD IS WRONG. TRY AGAIN.")

        while True:
            change_password()
            print("____________")
            print("FROM CBA BANK: \n thank you sir! for using our services.\n i hope you can't face any problem,any time...\n THANKS.")
            another_change = input("Do you want to change your password again? (yes/no): ").lower()
            if another_change != "yes":
                break


    elif x == "3":

        passwords = [
            "4321", "7601", "5613", "9970", "5372", "5248", "4733", "0193", "3216", "7695",
            "3617", "1029", "4169", "7834", "1267", "2390", "2271", "4100", "1067", "6908",
            "5634", "3965", "4590", "4312", "2154", "3469", "6996", "6900", "7856", "1221",
            "4343"
        ]
        def transfer_money():
         print("You want to transfer your money to someone else.")
         name = input("ENTER YOUR NAME: ")
         cell_number = int(input("ENTER YOUR CELL NUMBER: "))
        def lx():
           while True:
               t = int(input("ENTER YOUR CASH TO TRANSFER IT: "))

               if t >= 5000:
                   print("YOUR CASH IS TRANSFER.\nSIR!")
                   break


               elif t < 5000:
                   print("YOUR CASH IS NOT TRANSFER,\nPLEASE TRY AGAIN")
                   continue
        transfer_money()
        password = input("ENTER YOUR PASSWORD: ")
        if password in passwords:
                print("YOUR PASSWORD IS CORRECT.")
                lx()
                print("___________")
                print("FROM CBA BANK: \n thank you sir! for using our services.\n i hope you can't face any problem,any time...\n THANKS.")
                break

        else:
                print("YOUR PASSWORD IS WRONG PLEASE TRY AGAIN...")
                continue

       #else:
        #print("YOUR PASSWORD IS WRONG PLEASE TRY AGAIN...")
         #  continue


        #while True:
        #    transfer_money()
         #   break

    elif x == "4":
        passwords = [
            "4321", "7601", "5613", "9970", "5372", "5248", "4733", "0193", "3216", "7695",
            "3617", "1029", "4169", "7834", "1267", "2390", "2271", "4100", "1067", "6908",
            "5634", "3965", "4590", "4312", "2154", "3469", "6996", "6900", "7856", "1221",
            "4343"
        ]
        print("You want to change your address.")
        u=input("ENTER YOUR NAME:")
        r=input("ENTER YOUR PASSWORD:")
        if r in passwords:
            print("password entered")
        else:
            print("your password is not correct \nPLEASE TRY AGAIN.")
            continue
        k=input("ENTER YOUR CELL NUMBER:")
        z=input("ENTER YOUR ADDRESS:")
        d=input("ENTER YOUR NEW ADDRESS:")
        if z!=d:
            print("YOUR ADDRESS IS CHANGED SUCCESSFULLY.")
            print("____________")
            print("FROM CBA BANK: \n thank you sir! for using our services.\n i hope you can't face any problem,any time...\n THANKS.")
            break
        else:
            print("YOU ENTERED YOUR OLD ADDRESS.\n PLEASE REWRITE YOUR ADDRESS.")
            continue


    elif x == "5":

        passwords = [
            "4321", "7601", "5613", "9970", "5372", "5248", "4733", "0193", "3216", "7695",
            "3617", "1029", "4169", "7834", "1267", "2390", "2271", "4100", "1067", "6908",
            "5634", "3965", "4590", "4312", "2154", "3469", "6996", "6900", "7856", "1221",
            "4343","1010"
        ]

        def info():
            h = input("Do you want to DELETE/BLOCK your account: ")
            if h.lower() == "delete":
                print(""""
                 DELETE OPTIONS:
                1. Account Closure: Permanently closing the account.
                2. Fund Transfer: Handling remaining funds in the account.
                3. Loss of Access: Impact on account services and access.
                4. Payment Updates: Managing automatic payments and direct deposits.
                5. Transaction Limitation: Inability to use the account for banking transactions.
                """)
                a = input("WHY YOU WANT TO DELETE YOUR ACCOUNT: ")


                match str(a):

                    case "1":
                        print("Your account is closed permanently.")
                    case "2":
                        print(
                            "Any funds remaining in the account will be transferred or withdrawn according to your instructions.")
                        q = input("TELL ME YOUR INSTRUCTIONS:")
                        print(q, "YOUR INSTRUCTIONS ARE SUBMITTED SUCCESSFULLY.\nSIR!", l)
                    case "3":
                        print(
                            "You  lose access to the account's associated services, such as online banking and debit cards.")
                    case "4":
                        print(
                            "Automatic payments and direct deposits linked to the account are discontinued, and you  need to update your payment information with relevant parties.")
                    case "5":
                        print("You  no longer be able to use the account for any banking transactions.")
                    case _:
                        print(a,"YOUR ACCOUNT IS 'DELETED' SUCCESSFULLY.")


            elif h.lower() == "block":
                print(""""
                 BLOCK OPTIONS:
                1. Account Suspension: Temporarily blocking the account.
                2. Limited Access: Viewing balance without conducting transactions.
                3. Reasons for Blocking: Security, fraud, or legal issues for the block.
                4. Additional Documentation: Providing required information to remove the block.
                5. Security Investigation: Bank's scrutiny before lifting the block.
                """)
                n = input("WHY YOU WANT TO BLOCK YOUR ACCOUNT: ")

                match str(n):
                    case "1":
                        print( "Your account is temporarily suspended, and no transactions are allowed until the block is lifted.")
                    case "2":
                        print("You are still  able to access your account details and view the balance, but you won't  able to perform any new transactions.")

                    case "3":
                        print("The block may be due to security concerns, suspected fraudulent activity, or legal issues, and you  need to contact the bank to resolve the matter.")

                    case "4":
                        print("You  need to provide additional documentation or information to the bank to remove the block.")

                    case "5":
                        print("In this cases, the bank  conduct an investigation to ensure the account's security and authenticity before removing the block.")

                    case _:
                        print(n,"YOUR ACCOUNT IS 'BLOCKED' SUCCESSFULLY.")

        while True:
            print("You want to block/delete your account.")
            l = input("ENTER YOUR NAME: ")
            s = input("ENTER YOUR ADDRESS: ")
            f = input("ENTER YOUR CELL NUMBER: ")
            p = input("ENTER YOUR PASSWORD: ")
            if p in passwords:
                print("PASSWORD VERIFIED.")
              #  info()
               # break
            else:
               print('ENTER YOUR PASSWORD AGAIN.')
               continue
            info()
            print("____________")
            print("FROM CBA BANK: \n thank you sir! for using our services.\n i hope you can't face any problem,any time...\n THANKS.")
            break

        
    elif x == '6':

        passwords = [
            "4321", "7601", "5613", "9970", "5372", "5248", "4733", "0193", "3216", "7695",
            "3617", "1029", "4169", "7834", "1267", "2390", "2271", "4100", "1067", "6908",
            "5634", "3965", "4590", "4312", "2154", "3469", "6996", "6900", "7856", "1221",
            "4343", "1010"
        ]

        print('You want to change your cell number.')
        h=input("ENTER YOUR NAME: ")
        c=input("ENTER YOUR ADDRESS:")
        d=input("ENTER YOUR PASSWORD: ")
        if d in passwords:
            print("PASSWORD VERIFIED.")

            y=input("enter your old address:")
            z=input("enter your new address:")
            print(y.swapcase())
            print(z.swapcase())
            if y!=z:
             print("YOUR ADDRESS IS CHANGED.")
             print("____________")
             print("FROM CBA BANK: \n thank you sir! for using our services.\n i hope you can't face any problem,any time...\n THANKS.")
             break
            else:
               print("THERE ARE SOME PROBLEM IN ADDRESS.\nPLEASE TRY AGAIN...")
               continue
        else:print("PASSWORD NOT VERIFIED.")
        continue

    else:
     print("Invalid option.")
     break  # Exit the loop after executing the selected option
    print("Talha is a good programmer")
