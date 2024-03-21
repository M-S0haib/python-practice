print("\n")
print("\033[1;34m" + "Welcome to RIDE BOOKING" + "\033[0m")
print("\n")
print("\033[1;32m" + "Please select an option:" + "\033[0m")
print("1. Sign Up")
print("2. Login")
print()

while True:
    option = input("Enter your choice (1 or 2): ")
    print()

    if option == '1':
        print("\033[1;33mSign Up\033[0m")
        name = input("Enter your name: ")
        email = input("Enter your email address: ")
        password = input("Enter your password: ")
        print()
        print("\033[1;36m" + "You have signed Up successfully :)" + "\033[0m")
        print("")
        break  

    elif option == '2':
        print("\033[1;33mLogin\033[0m")
        email = input("Enter your email address: ")
        password = input("Enter your password: ")
        print()
        print("\033[1;36m" + "You have Logged In successfully :)" + "\033[0m")
        break

    else:
        print("\033[1;91m" + "Invalid option. Please select 1 or 2." + "\033[0m")

print()

print("\033[1;32m" + "We have 4 categories of vehicles, select the suitable ride" + "\033[0m")
print()

print("\033[1m" + "1: BIKE 2: AUTO 3: MiniCAR 4: AcCAR" + "\033[0m")
print()

while True:
    try:
        rideOption = int(input("\033[1m" + "Please enter the option 1, 2, 3, or 4: " + "\033[0m"))
        print()

        if 1 <= rideOption <= 4:
            if option == '1':
                if rideOption == 1:
                    print("\033[1;34m" + "You have selected bike ride" + "\033[0m")
                    charges = 100
                    discount = (charges*5)/100
                    disCharges = charges - discount
                    
                elif rideOption == 2:
                    print("\033[1;34m" + "You have selected Auto ride" + "\033[0m")
                    charges = 200
                    discount = (charges*7)/100
                    disCharges = charges - discount

                elif rideOption == 3:
                    print("\033[1;34m" + "You have selected MiniCar ride" + "\033[0m")
                    charges = 300
                    discount = (charges*10)/100
                    disCharges = charges - discount

                elif rideOption == 4:
                    print("\033[1;34m" + "You have selected AcCar ride" + "\033[0m")
                    charges = 400
                    discount = (charges*12)/100
                    disCharges = charges - discount
                    break 
     
                else:
                     print("\033[1;91m" + "Invalid option. Please select 1 to 4." + "\033[0m")

            if option == '2':
                if rideOption == 1:
                    print("\033[1;34m" + "You have selected bike ride" + "\033[0m")
                    charges = 100
                    
                elif rideOption == 2:
                    print("\033[1;34m" + "You have selected Auto ride" + "\033[0m")
                    charges = 200

                elif rideOption == 3:
                    print("\033[1;34m" + "You have selected MiniCar ride" + "\033[0m")
                    charges = 300
                elif rideOption == 4:
                    print("\033[1;34m" + "You have selected AcCar ride" + "\033[0m")
                    charges = 400
                    break 
     
                else:
                     print("\033[1;91m" + "Invalid option. Please select 1 to 4." + "\033[0m")

    except:
        print("\033[1;91m" + "Invalid option. Please enter a valid number." + "\033[0m")

print()

print("\033[1;32m" + "We are offering five routes" + "\033[0m")
print()

print("\033[1m" + "1: Numaish, 2: Nazimabad, 3: Boardoffice, 4: Hyderi, 5: Abdullahchok" + "\033[0m")

while True:
    print()
    print("\033[1m" + "Please Select the route via number" + "\033[0m")
    try:
        route = int(input())

        if 1<= route <=5:

            if route == 1:
                routeCharges = 100
            elif route == 2:
                routeCharges = 200
            elif route == 3:
                routeCharges = 300
            elif route == 4:
                routeCharges = 400
            elif route == 5:
                routeCharges = 500
            break
        else:
            print("\033[1;91m" + "Invalid option. Please select 1 to 5." + "\033[0m")
    except :
        print("\033[1;91m" + "Invalid option. Please enter a valid number." + "\033[0m")

print()

print("\033[1;32m" + "Enter the Pickup location" + "\033[0m")
pickup = input()

if option == '1':
    totalCharges = disCharges + routeCharges

elif option =='2':
     totalCharges = charges + routeCharges

print()

print("\033[1;34mTotal charges will be\033[0m", totalCharges)

while True:
    confirm = input(("\033[1m" + "Enter done to confirm the ride: " + "\033[0m"))
    print()

    if confirm.lower() == "done":
        print("\033[1;32mYour ride is booked. Our rider is on its way :)\033[0m")
        print()
        break
    else:
        print("\033[1;31m" + "Please enter 'done' to confirm the ride." + "\033[0m")
