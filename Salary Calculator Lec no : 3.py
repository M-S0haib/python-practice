print("**----SALARY CALCULATOR----**")

print("ENTER YOUR NAME")
name = input()

print("ENTER YOUR EMPLOYEE NUMBER")
empNum = int(input())

print("ENTER YOUR SALARY")
salary = int(input())

if(salary >= 50000):
    tax = (salary * 15) / 100
    salary1 = salary - tax

elif(salary>=40000):
    tax = (salary * 10) / 100
    salary1 = salary - tax

elif(salary>=30000):
    tax = (salary * 5) / 100
    salary1 = salary - tax

else:
    salary1 = salary

allowance = (salary1 * 0.5)  / 100    

finalSalary = allowance + salary1

print("YOU GOT A MOBILE ALLOWANCE & YOUR SALARY IS : " , finalSalary)

