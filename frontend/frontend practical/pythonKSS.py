#sum of numbers between m and n: 
m=int(input("the first number is:"))
n=int(input("the last number is:"))
sum=0
for i in range(m,n+1):
    sum= (sum+i)
    print("sum is:",sum)
    
#check whether the no. is perfectly divided or not:
m=int(input("the first no. is :"))
n=int(input("the another no. is :"))
if m%n==0:
    print("perfectly divided")
else:
    print("not perfectly divided")
    
#find area and parameter of circle:
import math
diameter=int(input("diameter is:"))
r=(diameter/2)
pie=3.14
area=(pie*r*r)
print ("area:",area)
parameter=(2*pie*r)
print ("parameter:",parameter)

#find the factorial of a :
a=int(input("number is:"))
factorial=1
for i in range(1,a+1):
  factorial*=i
  print(factorial)
   
#print the pattern
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()