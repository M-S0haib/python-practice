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

print("\033[1;32m" + "we have 4 categories of vehicles , select the suitable ride" + "\033[0m")
print()   

print("\033[1m" + "1:BIKE 2:AUTO 3:MiniCAR 4:AcCAR" + "\033[0m")
print()

while True:
    rideOption = int(input ("\033[1m" + "please enter the option 1 , 2 , 3 , or 4 : " + "\033["))
    print()

    if(rideOption == 1):
        print("\033[1;34m" + "You have selected bike ride" + "\033[0m")

        charges = 100
        break
    
    elif(rideOption == 2):
        print("\033[1;34m" + "You have selected Auto ride" + "\033[0m")
        charges = 200
        break

    elif(rideOption == 3):
        print("\033[1;34m" + "You have selected MiniCar ride" + "\033[0m")
        charges = 300
        break

    elif(rideOption == 4):
        print("\033[1;34m" + "You have selected AcCar ride" + "\033[0m")
        charges = 400
        break

    else:
       print("\033[1;91m" + "Invalid option. Please select 1 to 4." + "\033[0m")

print()

print("\033[1;32m" + "We are offering five routes" + "\033[0m")
print()

print("\033[1m" + "1: Numaish , 2: Nazimabad, 3: Boardoffice , 4: Hyderi , 5: Abdullahchok" +  "\033[0m" )

while True:
    print()
    print("\033[1m" + "Please Select the route via number" + "\033[0m")
    route = int(input())

    if (route == 1): 
        routeCharges = 100
        break

    elif (route == 2):
        routeCharges = 200
        break

    elif (route == 3):
        routeCharges = 300
        break

    elif (route == 4):
        routeCharges = 400
        break

    elif (route == 5):
        routeCharges = 500
        break

    else:
        print("\033[1;91m" + "Invalid option. Please select 1 to 5." + "\033[0m")
        
print()

print("\033[1;32m" + "Enter the Pickup location" + "\033[0m")
pickup = input()

totalCharges = charges + routeCharges

print()

print("\033[1;34mTotal charges will be\033[0m", totalCharges)


while True:
    confirm = input(("\033[1m" + "Enter done to confirm the ride : " + "\033[0m"))
    print()

    if( confirm == "done"):
        print("\033[1;32mYour ride is booked. Our rider is on it's way :) !\033[0m")
        print()
        break

    else:
        print("\033[1;31m" + "please enter correctly :(" + "\033[0m")

