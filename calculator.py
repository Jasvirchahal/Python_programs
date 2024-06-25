#addition function
def add(num1,num2):
    return num1+num2
#subtract function
def subtract(num1,num2):
    return num1,num2
#multiplication function
def multiply(num1,num2):
    return num1*num2
#division function
def division(num1,num2):
    return num1/num2


print("Select operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.division")

opt=(input("Enter Operation numbers:-"))
num1=(int(input("Enter First number:-")))
num2=(int(input("Enter Second number:-")))

if opt=='1':
    print("Addition of two numbers is:-",num1,"+",num2,"=",add(num1,num2))
elif opt=='2':
    print("Subtraction of two numbers is:-", num1, "-", num2, "=", subtract(um1, num2))
elif opt=='3':
    print("Multiplication of two numbers is:-", num1, "*", num2, "=", multiply(num1, num2))
elif opt=='4':
    print("Division of two numbers is:-", num1, "/", num2, "=", division(num1, num2))
else:
    print("Invalid operation Number")
