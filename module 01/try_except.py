#程序异常处理
try:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter tne second number:"))
    print(num1 / num2)
except Exception as err:
    print("Something went wrong!")
    print(err)
