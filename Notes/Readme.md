# Basics

Variables
-

We use variables to temporarily store data in computer's memory

price = 10
rating = 4.9
course_name = ‘Python for Beginners’
is_published = True
In the above example,
- price is an integer (a whole number without a decimal point)
- rating is a float (a number with a decimal point)
- course_name is a string (a sequence of characters)
- is_published is a Boolean. Boolean values can be True or False. 


String
-

We can define strings using single (‘ ‘) or double (“ “) quotes.
To define a multi-line string, we surround our string with tripe quotes (“””).
We can get individual characters in a string using square brackets [].
- course = ‘Python for Beginners’
- course[0] # returns the first character
- course[1] # returns the second character
- course[-1] # returns the first character from the end
- course[-2] # returns the second character from the end

We can slice a string using a similar notation:
course[1:5]
- The above expression returns all the characters starting from the index position of 1
to 5 (but excluding 5). The result will be ytho
- If we leave out the start index, 0 will be assumed.
- If we leave out the end index, the length of the string will be assumed. 


We can use formatted strings to dynamically insert values into our strings:

***name = ‘Mosh’***

***message = f’Hi, my name is {name}’***

# Functions

1. Chr() - This takes in an integer i and converts it to a character c, so it returns a character string

    Convert integer 65 to ASCII character ('A')

        y = chr(65)
        print(type(y),y)

        output:
        <class'str'> A

2. ord() - This takes a single Unicode character (string of length 1) and returns an integer, so the format is :

    Convert ASCII Unicode Character 'A' to 65

        y = ord('A')
        print(type(y),y)

        <class'int'>65
# Class and Objects
A class represents a blueprint for creating objects (an object is an instance of a class).

- The user-defined object are created using the class keyword

Creating a class
-

Code - 

        class details:
            name = "vivek
            age = 24


Self parameter
-
 
The self parameter is a reference to the current instance of the class and is used to access variable that belongs to the class

It must be provided as the extra parameter inside the method definition

Code -

        class person:
            name = "vivek"
            cl = "Mca"
            def info(self):
                print(f"{self.name} is department of computer science student")
        a = person()
        a.name = "Vivek"
        a.cl = "BCA"

        a.info()

Constructors
-

A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructor. 

Constructor is invoked automatically when an object an object of a class is created

    Syntax : __init__(self,param1,param2)

A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign value to the data members of that class. It cannot return any value other than None.

Types of Constructors in Python
-

- **Parameterized Constructor** - When the constructor accepts arguments along with ***self***, it is known as parameterized constructor.

    These arguments can be used inside the class to assign the values to the data members.

    Code - 

        class Account:
            def __init__(self,name):
                self.name = name
            
            def info(self):
                print(f"hey {self.name} what is your occupation")

        a = Account("Vivek")
        a.info()


- **Default Constructor -** When the constructor doesn't accept any argument from the object and has only one argument ***self*** in the constructor it is known as a default constructor.

    Code - 

        class Acc:
            def __init__(self):
                print("How are you?")
        obj = Acc()
        


