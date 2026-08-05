#==================================================================
# DOCUMENTATION FOR PYTHON STRINGS AND PRINT() FUNCTION (LINE 5-50)
#==================================================================

#official documentation for python strings can be found at - https://docs.python.org/3/library/stdtypes.html#string-methods
#official documentation for print() function can be found at - https://docs.python.org/3/library/functions.html#print
#print() function is used to print the output on the console. It can take multiple arguments and print them in a single line.
#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) is the syntax of print() function. Here, *objects is a variable length argument list which means it can take any number of arguments. sep is used to specify the separator between the objects, end is used to specify what to print at the end of the output, file is used to specify the file where the output should be written, and flush is used to specify whether to forcibly flush the stream.



#When concatenating two or more strings in a print command, or a string and a variable, the use of comma and the
# plus sign makes no difference.
x=5
print("The value of x is",x, "-Used comma to concatenate") #This will work as we are using comma to concatenate the string and the variable

# print("The value of x is "+x)     This will give an error as x is an integer and cannot be concatenated with a string using the plus sign
print("The value of x is "+str(x)+" -Converted int x to string") #This will work as we are converting the integer to string using str() function
print()


#Accept user's name, remove whitespaces from left and right end of name, and capitalize first letter of every word
# in name
name = input("What is your name?\n").strip().title()

#Use .lstrip() and .rstrip() to remove whitespaces only on left side of string and only from right side of string
# ,respectively



#end current print command with '???' which allows next print command to be printed in the same line

#by default, when end='<custom ender>' is not given in the paranthesis, it uses \n as the default seperator which
# gives the same effect as using end='\n' manually in the paranthesis
print("hello",name, end="???")
print("byee")
#Above statements' output will give the output as - hello Rohan Naik???byee
print("Used end='???' to end the print command with '???' which allows next print command to be printed in the same line")
print()



print("hello",name,"-Used comma to concatenate") #This will work as we are using comma to concatenate the string and the variable
print(f"hello {name}","-F-string format") #f-string is used to format the string and print the value of variable name in the string
#The above two print statements will give the same output as - hello Rohan Naik
print()

#Splitting a string into a list of words using .split() method. By default, it splits the string by whitespace.
first, last = name.split() #This will split the name into first and last name and assign them to first and last variables respectively
print(f"First name is {first} and last name is {last} -Used .split() method to split the string into a list of words")



#==================================================================
# DOCUMENTATION FOR INT DATA TYPE (LINE 58-)
#==================================================================

#Resume CS50P 2022 video - Lecture 0 - @ 00:59:35 - Integers and Operations https://youtu.be/JP7ITIXGpHk?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&t=3575