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

print("BIKE AUTO MiniCAR AcCAR ")

ride = str(input())

print(" ENTER YOUR PICKUP LOCATION")
pickUp = str(input())

print(" Select the DropOff")

print("lasbella Nazimabad FiveStar Nagan NorthKarachi")

dropOff = str(input())

location = " Lasbella" ,  "Nazimabad" , "FiveStar" , "Nagan" , "NorthKarachi"

