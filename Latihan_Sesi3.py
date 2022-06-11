# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:46:10 2022

@author: chris
"""

def my_function(p, l):
    "Function untuk mengitung luas"
    print(p * l)

my_function(2,4)

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)


# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)


# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme()

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme(str = "Hacktiv8")



# Function definition is here
def printinfo( name, nilai1, nilai2, nilai3, nilai4, nakhir ):
   "This prints a passed info into this function"
   nakhir=(nilai1*0.1)+(nilai2*0.2)+(nilai3*0.3)+(nilai4*0.4)
   print("Name: ", name)
   print("nilai 1: ", nilai1)
   print("nilai 2: ", nilai2)
   print("nilai 3: ", nilai3)
   print("nilai 4: ", nilai4)
   print("nilai akhir: ", nakhir)
   return;

# Now you can call printinfo function
printinfo(name='eva', nilai1=100, nilai2=90, nilai3=75, nilai4=60, nakhir=0)

def printinfo( name, nilai1, :
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   return;

# Now you can call printinfo function
printinfo( age=4, name="hacktiv8" )age ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   return;

# Now you can call printinfo function
printinfo( age=4, name="hacktiv8" )




def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return;
printinfo( 10 )
printinfo( 45, 80, 50, "b" )


def printinfo( arg1, *tuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for var in tuple:
      print(var)
   return;
printinfo( 10 )
printinfo( 45, 80, 50, "b" )



# Function definition is here
sum = lambda arg1, arg2, arg3, arg4: arg1 + arg2+ arg3+ arg4;

# def sum(arg1, arg2):
#     arg1 + arg2
    
# Now you can call sum as a function
# print("Absen : ", sum( 10, 20 ))
# print("tugas : ", sum( 20, 20 ))
# print("UTS : ", sum( 10, 20 ))
# print("UAS: ", sum( 20, 20 ))

print('nilai akhir':",sum(10,20,30,40,0))

# Function definition is here
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    total2 = total + arg1
    print("Inside the function : ", total)
    return total2

# Now you can call sum function
total = sum(10, 20)
print("Outside the function : ", total)


total = 0; 
def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("Inside the function local total : ", total)
   return total;

# def min():
sum( 10, 20 );
print("Outside the function global total : ", total)

total = 3; 
def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("total arg : ", total)
   return total;

# def min():
sum( 10, 20 );
print("total3 : ", total)


jumlahKucing = 20

def jumlahHewan():
    jumlahAnjing = 30
    return jumlahKucing + jumlahAnjing

def jumlahKelinci():
    return jumlahKucing + jumlahKucing

jumlahHewan()
jumlahKelinci()
print(jumlahHewan())
print(jumlahKelinci())




















