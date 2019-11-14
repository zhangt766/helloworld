
N=10
countFound=0
num=3
print('---------------------------------------')
print('Looking for primes')
while countFound<N:

    isPrime=1
    for i in range(2,num-1):
        if (num % i)==0:
            isPrime=0
            break
    if isPrime==1:
        print(num)
        countFound=countFound+1
    num=num+1
print('---------------------------------------')

#print
print('hello,world')
print("hello,world")
#note "" & '' the same

print("line1...line2...line3")

a='abc'
b=a
a='xyz'
print(b)     #output=abc

print(9/3)   #output=3.0
print(9//3)  #output=3
print(10%3)  #output=1

print('中文')
ord('a')  #without print how to check the output

#list
classmates=['jak','may','adam']
len(classmates)       # length of the list
classmates.insert()   #insert variables into list, in "( )" , we can assign the position, eg:1,2,3
classmates.pop()     #delete variables in list, similar to
classmates[1]="bob"  #change may to bob, attention the first one statrs from 0

#tuple
#can not insert or delete any variables, more safe
classmates=('jak','may','adam')
t=(1,)         #attention, defining tuple with one varibale


#if else
age=3
if age>18:
    print("your age is : ", age)
    print('adult')
else:
    print("teenager")
#else if

age=3
if age>18:
    print("adult")
elif age>6:
    print('teenager')
else:
    print("kid")


#prime number
#checking if a prime number
num=21
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")
# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")


#find out all prime numbers
lower = 1
upper = 10
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
# all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


N=10
countFound=0
num=30
while countFound<N:
    isPrime=1
    for i in range(2,num-1):
        if (num % i)==0:
            isPrime=0
            break
    if isPrime==1:
        print(num)
        countFound=countFound+1




















