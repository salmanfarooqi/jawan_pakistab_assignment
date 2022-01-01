
 # kamyab jawan  pakistan Assignment #1
 
 
 
 # Q.No 1 write a python programe to print the following string in a  specific formate(see output) 

        #   winkle ,Twinkle, little star,
        #          How i wonder what you are!
        #                  up above the world  so High,
        #                 like a diamond in the sky.
        
        # Twinkle , Twinkle , little star,
        #           How i wonder what you ar




print('''
      
        Twinkle ,Twinkle, little star,
                 How i wonder what you are!
                         up above the world  so High,
                        like a diamond in the sky.
        
        Twinkle , Twinkle , little star,
                  How i wonder what you are
      
     ''' )


# Q.No 2:  write a python programe to get the python  version you using.
import sys
print(sys.version)
 
 #Q.No 3  write a programe to display the current date and time.

import datetime
date_time = datetime.datetime.now()
print ("current date and time is :",date_time)


# Q.No 4 write a python programe which takes the radius from the user and display the area.

from math import pi # pi=3.14
radius=float(input("enter the radius of the circle"))
area=pi*radius**2
print("area is",area)

# Q.No 5 write a python programe which takes ist name and last name from the user and display it in reverse
# order with space between them.


ist_name=input("enter your ist name:")
last_name=input("enter your last name:")
full_name=ist_name + " " + last_name
print("your name in reverse order is:",full_name[::-1])


# Q. No 6 write a python programe which takes two input from user and add them.

ist_number=int(input("enter ist number"))
number_2nd=int(input("enter 2nd number:"))
addition=ist_number + number_2nd
print("addition is:" , addition)