print("Welcome to RIDE BOOKING")
print("Select an option:")
print("1. Sign Up")
print("2. Login")

while True:
    option = input("Enter your choice (1 or 2): ")

    if option == '1':
        print("Sign Up")
        name = input("Enter your name: ")
        email = input("Enter your email address: ")
        password = input("Enter your password: ")
        print("You have signed Up successfully")
        break  

    elif option == '2':
        print("Login")
        email = input("Enter your email address: ")
        password = input("Enter your password: ")
        print("You have Logged In successfully")
        break 

    else:
        print("Invalid option. Please select 1 or 2.")


print("we have 4 categories of vehicles")

print("select the suitable ride")

print("1:BIKE  2:AUTO  3:MiniCAR  4:AcCAR ")

while True:
    rideOption = int(input ("please enter the option 1 , 2 , 3 , or 4 : "))
    if(rideOption == 1):
        print("You have selected bike ride")
        charges = 100
        break
    
    elif(rideOption == 2):
        print("You have selected Auto ride")
        charges = 200
        break

    elif(rideOption == 3):
        print("You have selected MiniCar ride")
        charges = 300
        break

    elif(rideOption == 4):
        print("You have selected AcCar ride")
        charges = 400
        break

    else:
        print("Invalid option. Please select 1 to 4")

print("We have five routes")

print("1:Numaish , 2:Nazimabad, 3:Boardoffice , 4:Hyderi , 5:Abdullahchok")

while True:
    print("Please Select the route via number")
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
        print("Invalid option. Please select between 1 to 5")
        

print("Enter the Pickup location")
pickup = input()


totalCharges = charges + routeCharges

print("Total charges will be" , totalCharges)

confirm = input("Please enter done to confirm the ride : ")
 
while True:
    print("Please enter done to confirm the ride : ")
    confirm = input()

    if( confirm == "done"):
        print("Your ride is booked :) ! Our rider is on it's way")
        break

    else:
        print("please enter correctly :(")
