#program to print hello world

print("hello world")
#print statement in python

a = "chandan"
chandan = a

print(chandan[0:3 ])
#write a program to print 2 numbers

# a = int(input("enter first number :"))
# b = int(input("enter second number :"))
# # z = a+b
# print(a+b)

#write a function to create a calculator

# def add(num1,num2):
#     return num1+num2

# def sub(num1,num2):
#     return num1-num2

# def mul(num1,num2):
#     return num1*num2

# def div(num1,num2):
#     return num1//num2

# num1 = int(input("enter first number :")) 
# num2 = int(input("enter second number :"))   

# print(div(num1,num2))
# print(add(num1,num2))
# print(mul(num1,num2))
# print(sub(num1,num2))

#write a program to check number is even or odd

def evenodd(n):
    if(n%2==0):
        print(n,"number is even")

    else:
       print(n,"number is odd")

number = int(input("enter the number :"))
evenodd(number)