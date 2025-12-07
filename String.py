# string basic operations
# without functions?
my_string = "Hello, World"
print(my_string)
print(len(my_string))
print(my_string[0])
print(my_string[-1])
print(my_string[0:5])
print(my_string.upper())
print(my_string.lower())
print(my_string.replace("Nitin", "Chalu"))
# next Questions
#string methods with explanaton and examples one by one
# 1. len() - Returns the length of the string
# example:
my_string = "Hello, World"
print(len(my_string))
# output: 13
# 2. upper() - converts all characters in the string to upper case
# example:
my_string = "Hello, World"
print(my_string.upper())
# output: "HELLO, WORLD"
# 3. lower() - converts all characters in the string to lower case
# example:
my_string = "Hello, World"
print(my_string.lower())
# output: "hello, world"
# 4. replace() - replaces a specified phrase with another specified phrase
# exmple:
my_string = "Hello, Nitin"
print(my_string.replace("Nitin","Chalu"))
# output: "Hello, Chalu"
# 5. split() - splits the string at the specified separator, and returns a list
# example:
my_string = "Hello, World"
print(my_string.split(","))
 # you can only give the example not the output and useless comments

# next questions
# string indexing and slicing with explanation and examples one by one
# 1. Indexing - accessing individual characters in a string using their position  
# example:
my_string = "Hello, World"
print(my_string[0])
#ok
#  String methods
spices = " apple, banana, cherry"
print(spices.strip())
# what is the leading and trailing whitespace


take = input("Enter your name:")
print("Hello", take)

take2 = int(input("Enter a first number:"))
take3 = int(input("Enter a Second number:"))

result = take2 + take3
print("The sum is:", result)

length = input("Enter Your name :")
print("The length of your name is:", len(length))

uppercase_name = input("Enter Your name:")
print("Your name in uppercase is:", uppercase_name.upper())


first_and_last = input("Enter Any Word:")
print("First letter: ", first_and_last [0])
print("Last Letter:", first_and_last [-1])

Check if the input string contains the word “hello”.
chek_word = input("Enter a sentence:")
if "hello" in chek_word.lower():
    print("The Word 'hello' is present in the sentence.")
else:
    print("The Word 'hello' is not present in the sentence.")
    


number = int(input("Enter a number:"))
if number % 2 == 0:
    print("The Number is Even.")
else:
    print("The Number is Odd.")


string = input("Enter a sentence:")
print("reversed sentence:", string[::-1])

replace = "Nitin is My Friend"
print(replace.replace("Nitin", "Chalu"))

Age = float(input("Enter Your Age:"))
if Age >= 18:
    print("You are a adult.")
else:
    print("You are  a minor.")