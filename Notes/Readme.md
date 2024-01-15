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