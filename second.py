#write a program to check whether a number is prime or not

def prime(n):
   if (n>1):

       for i in range(2,n):
           if(n%i)==0:
               print(n ,"is not prime")
               break
       else:
            print(n,"is prime")

# def prime(n):
#     if n>1:
#         for i in ran5ge(2,n):
#             if (n%i) == 0:
#                 print("not prime")
#                 break
#         else:
#             print("prime")
    

number = int(input("enter the number :"))
prime(number)