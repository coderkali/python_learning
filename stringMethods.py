name= "Kali prasad padhi"

#name[0] = "R" # We cannot change the value of a string because strings are immutable in Python.

print(name)

a = len(name) # len() function is used to get the length of a string.
print(a)

print(name.upper()) # upper() function is used to convert a string to uppercase.
print(name)
print(name.lower()) # lower() function is used to convert a string to lowercase.
print(name)
print(name.capitalize()) # capitalize() function is used to convert the first character of a string to uppercase and the rest to lowercase.
print(name)
print(name.title()) # title() function is used to convert the first character of each word in a string to uppercase and the rest to lowercase.
print(name)
test = "   Hello World!   "
print(test.strip()) # strip() function is used to remove any leading and trailing whitespace from a string.
print(test.lstrip()) # lstrip() function is used to remove any leading whitespace from a string.
print(test.rstrip()) # rstrip() function is used to remove any trailing whitespace from a string.



text = "This is a sample text for testing the split() function."
print(text.find("sample")) # find() function is used to find the index of the first occurrence of a substring in a string. It returns -1 if the substring is not found.
print(text.find("test")) # It will return the index of the first occurrence of "test" in the string.
print(text.find("hello")) # It will return -1 because "hello" is not present in the string.

text1= text.replace("sample", "example");

print(text1) # replace() function is used to replace a substring with another substring in a string. It returns a new string with the replacements made.
print(text) # The original string remains unchanged because strings are immutable in Python.

print(text1.__hash__())
print(text.__hash__())

text2 = "Apples,BanNs,Oranges,Grapes"
print(text2.split(",")) # split() function is used to split a string into a list of substrings based on a specified delimiter. In this case, the delimiter is a comma (",
#"). The function returns a list of substrings that were separated by the delimiter.


print(",".join(text2.split(","))) # join() function is used to join a list of strings into a single string with a specified delimiter. In this case, we are joining the list of substrings back into a single string using a comma as the delimiter.

text3 = "HelloWorld12345"

print(text3.isalpha()) # isalpha() function is used to check if all characters in a string are alphabetic. It returns True if all characters are alphabetic and there is at least one character, otherwise it returns False.
print(text3.isdigit()) # isdigit() function is used to check if all characters in a string are digits. It returns True if all characters are digits and there is at least one character, otherwise it returns False.
print(text3.isalnum()) # isalnum() function is used to check if all characters in a string are alphanumeric (either alphabetic or digits). It returns True if all characters are alphanumeric and there is at least one character, otherwise it returns False.
print(text3.isspace()) # isspace() function is used to check if all characters in a string are whitespace characters. It returns True if all characters are whitespace and there is at least one character, otherwise it returns False. 