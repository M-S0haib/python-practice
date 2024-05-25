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
print("\033[94m 1.Mini Car    2.AC Car    3.Hi-Roof    4.BRV\033[0m")
print()

while True:
    try:
        rideOption = int(input("Please Enter the Option 1 , 2 , 3 , or 4 : "))
        print()

        if 1 <= rideOption <= 4:
            if option == '1':
                if (rideOption == 1):
                    print("\033[94m" + "Mini Car Selected!" + "\033[0m")
                    charges = 100
                    break

                elif (rideOption == 2):
                    print("\033[94m" + "AC Car Selected!" + "\033[0m")
                    charges = 200
                    break

                elif (rideOption == 3):
                    print("\033[94m" + "Hi-Roof Selected!" + "\033[0m")
                    charges = 300
                    break

                elif (rideOption == 4):
                    print("\033[94m" + "\033[93mPremium Ride: \033[0mBRV Selected!" + "\033[0m")
                    charges = 400
                    break

            if option == '2':
                if rideOption == 1:
                    print("\033[94m" + "Mini Car Selected!" + "\033[0m")
                    charges = 100
                    break

                elif rideOption == 2:
                    print("\033[94m" + "AC Car Selected!" + "\033[0m")
                    charges = 200
                    break

                elif rideOption == 3:
                    print("\033[94m" + "Hi-Roof Selected!" + "\033[0m")
                    charges = 300
                    break

                elif rideOption == 4:
                    print("\033[94m" + "\033[93mPremium Ride: \033[0mBRV Selected!" + "\033[0m")
                    charges = 400
                    break

        else:
            print("\033[91m" + "Invalid Option! Please Select 1 to 4." + "\033[0m")

    except:
        print("\033[91mInvalid option! Enter a number from 1-4 to proceed. \033[0m")
        print()

print()

print("\033[92m" + "Our Ride goes around these cities:" + "\033[0m")

print("\033[93m1.\033[0mKarachi        \033[93m2.\033[0mHyderabad     \033[93m3.\033[0mMirpurkhas   \033[93m4.\033[0mSukker     \n\033[93m5.\033[0mMultan        \033[93m6.\033[0mFaisalabad   \033[93m7.\033[0mLahore    \n\033[93m8.\033[0mIslamabad     \033[93m9.\033[0mSkardu       \033[93m10.\033[0mGilgit")

print()

cities = ['Karachi','Hyderabad', 'Mirpurkhas', 'Sukker', 'Multan', 'Faisalabad', 'Lahore', 'Islamabad', 'Skardu', 'Gilgit']

while True:
    try:
        pickup_station = int(input("Enter pickup station (1-10): "))
        dropoff_station = int(input("Enter drop-off station (1-10): "))

        if pickup_station != dropoff_station:


            if 1 <= pickup_station <= 10 and 1 <= dropoff_station <= 10:   
                
                    pickup_city = cities[pickup_station - 1]
                    dropoff_city = cities[dropoff_station - 1]
                    break

            else:
                print("Both stations must be between 1 and 10. Please try again.")

        else:
             print( "Pickup & Dropoff can't be the same")
             
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")


price_per_station = 2000
num_stations = abs(dropoff_station - pickup_station)
total_price = (num_stations * price_per_station) + charges

print()

if option == '1':
    print("\033[93mCongrats! As a new user of SwiftGo, You got a discount of 5%!!\033[0m")
    print()
    discount = (total_price * 5) / 100
    total = total_price - discount
    tax = total_price * 2 / 100
    final_amount = total + tax
    print(f"Original Fare(with discount): Rs.{abs(total)}/- + TAX(Rs.{abs(tax)}/-)")
    print(f"Total charges after discount will be \033[93m Rs.{abs(final_amount)} \033[0m")

elif option == '2':
    tax = total_price * 2 / 100
    final_amount = total_price + tax
    print(f"Original Fare: Rs.{abs(total_price)}/- + TAX(Rs.{abs(tax)}/-)")
    print(f"Total charges will be \033[93m Rs.{abs(final_amount)} \033[0m")

print()

while True:
    confirm = input(("Enter \033[93m'done'\033[0m to confirm the ride: ")).lower()
    print()

    if (confirm == "done"):
        print(f"Your ride is booked from \033[93m{pickup_city}\033[0m to \033[93m{dropoff_city}\033[0m. "
              f"Please reach the station ASAP! :)")
        print()
        print("\033[93mThanks for using SwiftGo!\033[0m")
        break

    else:
        print("\033[91mPlease make sure 'done' is entered correctly :(\033[0m")
