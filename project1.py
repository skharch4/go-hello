print("Hello,Everybody")
if 26>25:
    print ("Twenty six is bigger than twenty five")
    #Is it correct?
    #Is it wrong?
    x = 21
    y = "Steve"
    print(x)
    print(y)
    x = str(21) # x will be '21'
    y = int(21) # y will be 21
    z = float (21) # z will be 21.0
    print(x)
    print(y)
    print(z)
    print (type(x))
    print (type (y))
    print(type(z))
    b = 4
    B = 5
    
    print(b)
    print(B)
    #Testing Variables
    myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
myvar = "Jimmy"
print(myvar)
my_var = "Billy"
print(my_var)
myVariableName = "Jimmy"
my_variable_name = "Jimmy"
x,y,z = "a","b","c"
print(x)
print(y)
print(z)
x=y=z= "Alphabet"
print (x)
print (y)
print (z)
Cities = ["London","Paris","Chicago"]
x,y,z= Cities
print(x)
print(y)
print (z)
print(x,y,z)
print(x+y+z)
Numbers = ["2","17","23"]
x,y,z= Numbers
print(x+y+z)
print(x,z,y)
x=17
y=23
print(x,y)
print(x+y)
x= "Steve"
y=21
z= "y.o"
print(x,y,z)
x= "amazing"
y= "Mineral Water "
z= "is "
def myfunc():
    x= "taste"
    print(y+z+x)
myfunc()
print(y+z+x)
def myfunc():
    global x
    x= "superb"
myfunc()
print("This water is " + x)
x= "awesome"
def myfunc():
    global x
    x= "superb"
myfunc()
print( "This thing is " + x)
Carnames = ["Volvo","Subaru","Land Rover"]
x,y,z = Carnames
print(x,y,z)
x=y=z="Samsung"
print(x,y,z)
#Testing types below
x = int (21)
print(x)
print(type(x))
x= bytearray(5)
print(x)
print(type(x))
z=b"Type below"
print(z)
print(type(z))
#Testing types of numbers below
x= 253j
print (x)
print(type(x))
z=25
print(z)
print(type(z))
y=23.17
print(y)
print(type(y))
x=0
print(x)
print(type(x))
y=31498432958234
print(y)
print(type(y))
z=-31425312234
print(z)
print(type(z))   
x=5
print(x)
print(type(x))
x=5.3
print(x)
print(type(x))
x = int(1)
y = int(2.34)
z = int(2.501)
print (x,y,z)
x = float(1)
y = float(2.34)
z = float(2.564) 
print(x,y,z)
x = str(21)
y= str(25.123)
z= str (1j)
print (x,y,z)
V = "Variety"
print(V)
b = "White"
print (b)
x = '''London is a capital of England. England is a part of Great Britian'''
print (x)
a = "White,mineral, water"
print(a[6]) 
for y in "Europe Union":
    print(y)
a = "Good Morning, everyone!"
print(len(a))
txt = "Henry Ford was born in 1861, Detroit"
print ("born" in txt)
print ("London" in txt)
if "Ford" in txt:
    print("Yes, his name Ford")
if "Subaru" in txt:
    print("Yes, his name Ford")
txt = "Life is wonderfull"
if "is" in txt:
    print("Yes,it is")
if "am" not in txt:
        print("No, it isn'ht")
txt = "I really like music of 1970s-1980s"
print(txt)
if "1990s" not in txt:
    print("I don't like music of 1990s")
x = "Hello world!!!"
print(x)
print (x[3:9])
print(x[:10])
print(x[5:])
print(x[-9:-3])
b = "Good Morning, guys!"
print(b.upper())
print(b.lower())
print(b.strip())
print (b.replace("guys","everybody"))
print(b.split("guys"))
a = "Coca"
b ="Cola"
c = a+"&"+b
print(c)
age = 34
txt = "My name is John, I am {}"
print(txt.format(age))
quality = "perfect"
price = 99.99
amount = 13
myorder = "I want those {} pants, about {} of it, i heard that price is {}"
print(myorder.format(quality,amount,price))
txt = "Modern phones are also known as \"smartphones\""
print(txt)