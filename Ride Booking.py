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
        break
    
    elif(rideOption == 2):
        print("You have selected Auto ride")
        break

    elif(rideOption == 3):
        print("You have selected MiniCar ride")
        break

    elif(rideOption == 4):
        print("You have selected AcCar ride")
        break

    else:
        print("Invalid option. Please select 1,2,3 or4")

print("ENTER YOUR PICKUP LOCATION")
pickUp = input()

print(" Enter the DropOff")

print("lasbella Nazimabad FiveStar Nagan NorthKarachi")

dropOff = input()

location = " Lasbella" ,  "Nazimabad" , "FiveStar" , "Nagan" , "NorthKarachi"

