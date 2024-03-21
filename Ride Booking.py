title = "\033[92mSwiftGo - RIDE BOOKING - Your Route, Your Rules!\033[0m"
print(title.center(90))

print("\n")

welcome = ("\033[93mWelcome to SwiftGo! Please Sign Up or Login to book your ride. \033[0m")
print(welcome)


print("\n")
print("\033[92m" + "Please Select an Option:" + "\033[0m")
print("1. Sign Up")
print("2. Login")
print()
while True:
    option = input("Enter your choice (1 or 2): ")
    print()

    if option == '1':
        print("\033[93mSign Up\033[0m")
        first_name = input("First Name: ").capitalize()
        last_name = input("Last Name: ").capitalize()
        email = input("Enter Your Email address: ")
        password = input("Enter Your password: ")
        print()
        sign = f"\033[92m" + f"Dear {first_name} {last_name}, Thanks for Signing up to SwiftGo! :)" + "\033[0m"
        print(sign)
        print("")
        break

    elif option == '2':
        print("\033[93mLogin\033[0m")
        email = input("Enter Your Email Address: ")
        password = input("Enter Your Password: ")
        print()
        print("\033[36m" + "You have Logged In successfully :)" + "\033[0m")
        break

    else:
        print("\033[91m" + "Invalid Option! Please Select 1 or 2." + "\033[0m")


print("\n")

print("Book a suitable ride! SwiftGo offers...")
print("\033[94m 1.Bike    2.Auto    3.Mini Car    4.AC Car\033[0m")
print()

while True:
    try:
        rideOption = int(input("Please Enter the Option 1 , 2 , 3 , or 4 : "))
        print()

        if 1 <= rideOption <= 4:
            if option == '1':
                if(rideOption == 1):
                    print("\033[94m" + "Bike Selected!" + "\033[0m")
                    charges = 100
                    discount = (charges * 5) / 100
                    disCharges = charges - discount
                    break

                elif(rideOption == 2):
                    print("\033[94m" + "Auto Selected!" + "\033[0m")
                    charges = 200
                    discount = (charges * 5) / 100
                    disCharges = charges - discount
                    break

                elif(rideOption == 3):
                    print("\033[94m" + "Mini Car Selected!" + "\033[0m")
                    charges = 300
                    discount = (charges * 5) / 100
                    disCharges = charges - discount
                    break

                elif(rideOption == 4):
                    print("\033[94m" + "AC Car Selected!" + "\033[0m")
                    charges = 400
                    discount = (charges * 5) / 100
                    disCharges = charges - discount
                    break

            if option == '2':
                if rideOption == 1:
                    print("\033[94m" + "Bike Selected!" + "\033[0m")
                    charges = 100
                    break

                elif rideOption == 2:
                    print("\033[94m" + "Auto Selected!" + "\033[0m")
                    charges = 200
                    break

                elif rideOption == 3:
                    print("\033[94m" + "Mini Car Selected!" + "\033[0m")
                    charges = 300
                    break

                elif rideOption == 4:
                    print("\033[94m" + "AC Car Selected!" + "\033[0m")
                    charges = 400
                    break
                
        else:
            print("\033[91m" + "Invalid Option! Please Select 1 to 4." + "\033[0m")

    except:
        print("\033[91mInvalid option! Enter a number from 1-4 to proceed. \033[0m")
        print()


print()

print("\033[92m" + "We are offering five routes" + "\033[0m")

print("\033[33m1.\033[0mNumaish     \033[33m2.\033[0mNazimabad     \033[33m3.\033[0mBoard Office     \033[33m4.\033[0mHyderi     \033[33m5.\033[0mAbdullah Chok")

print()

while True:
    print("Please Select the route via number: ")
    try:
        route = int(input())

        if 1 <= route <= 5:
            if route == 1:
                routeCharges = 100
                dropOff = "Numaish"
                print(dropOff)
            elif route == 2:
                routeCharges = 200
                dropOff = "Nazimabad"
                print(dropOff)
            elif route == 3:
                routeCharges = 300
                dropOff = "Board Office"
                print(dropOff)
            elif route == 4:
                routeCharges = 400
                dropOff = "Hyderi"
                print(dropOff)
            elif route == 5:
                routeCharges = 500
                dropOff = "Abdullah Chowk"
                print(dropOff)
            break
        else:
            print("\033[1;91mInvalid option. Please select a number from 1 to 5.\033[0m")
    except ValueError:
        print("\033[91mInvalid option! Enter a number from 1-5 to proceed.\033[0m")

print()

print("\033[92mEnter Pickup location: \033[0m")
pickup = input().capitalize()


if option == '1':
    print("\033[93mCongrats! As a new user of SwiftGo, You got a discount of 5%!!\033[0m")
    print()
    totalCharges = disCharges + routeCharges
    tax = totalCharges * 2 / 100
    final_amount = totalCharges + tax
    print(f"Original Fare(with discount): Rs.{totalCharges}/- + TAX(Rs.{tax}/-)")
    print(f"Total charges after discount will be \033[93m Rs.{final_amount} \033[0m")

elif option == '2':
    totalCharges = charges + routeCharges
    tax = totalCharges * 2 / 100
    final_amount = totalCharges + tax
    print(f"Original Fare: Rs.{totalCharges}/- + TAX(Rs.{tax}/-)")
    print(f"Total charges will be \033[93m Rs.{final_amount} \033[0m")

print()

while True:
    confirm = input(("Enter \033[93m'done'\033[0m to confirm the ride: ")).lower()
    print()

    if( confirm == "done"):
        print(f"Your ride is booked from \033[93m{pickup}\033[0m to \033[93m{dropOff}\033[0m. "
              f"Rider will be arriving shortly to pick you up. Have a safe journey! :)")
        print()
        print("\033[93mThanks for using SwiftGo!\033[0m")
        break

    else:
        print("\033[91mPlease make sure 'done' is entered correctly :(\033[0m")
