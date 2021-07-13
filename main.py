#method 1 to find thr prime number or not
num=675
if num>1:
    for i in range(2,num):
        if(num%1)==0:
            print(num,"is not a prime number")
            print(i,"timmes",num//i,"is",num)
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")
    
#second method to find the number is prime or not

import math
num=654
if num>1:
    for i in range(2,math.ceil(num/2)):
        if(num%1)==0:
            print(num,"is not a prime number")
            print(i,"times",num/1,"is",num)
            break
    else:
        print(num,"is  a prime number")
else:
    print(num,"is not a prime number")

    
