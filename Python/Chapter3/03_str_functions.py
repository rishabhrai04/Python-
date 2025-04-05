name = " Harry "

print (len(name))
print(name.endswith("y")) 
print(name.startswith("H")) 
print(name.find("rr")) # returns the index of the first occurrence of the substring
print(name.count("r")) # returns the number of occurrences of the substring
print(name.isalpha()) # returns True if all characters are alphabetic
print(name.isalnum()) # returns True if all characters are alphanumeric
print(name.isdigit()) # returns True if all characters are digits
print(name.islower()) # returns True if all characters are lowercase
print(name.isupper()) # returns True if all characters are uppercase
print(name.upper()) # returns the string in uppercase
print(name.lower()) # returns the string in lowercase
print(name.title()) # returns the string in title case
print(name.capitalize()) # returns the string in capitalized case
print(name.swapcase()) # returns the string with uppercase and lowercase swapped    
print(name.replace("r", "R")) # replaces all occurrences of the substring with the new substring
print(name.split("r")) # splits the string into a list of substrings
print(name.split(" ")) # splits the string into a list of substrings
print(name.splitlines()) # splits the string into a list of substrings  
print(name.strip()) # removes leading and trailing whitespace
print(name.lstrip()) # removes leading whitespace
print(name.rstrip()) # removes trailing whitespace
print(name.strip("r")) # removes leading and trailing occurrences of the substring
print(name.lstrip("r")) # removes leading occurrences of the substring
print(name.rstrip("r")) # removes trailing occurrences of the substring 
print(name.zfill(10)) # pads the string with zeros on the left to fill the specified width
print(name.center(10)) # pads the string with spaces on both sides to fill the specified width
print(name.ljust(10)) # pads the string with spaces on the left to fill the specified width
print(name.rjust(10)) # pads the string with spaces on the right to fill the specified width    
print(name.expandtabs(4)) # replaces tabs with spaces
print(name.split(" ")) # splits the string into a list of substrings
print(name.join(["Hello", "World"])) # joins the list of strings with the specified string as a separator
print(name.format("Hello", "World")) # formats the string with the specified values
print(name.format_map({"name": "Harry"})) # formats the string with the specified values
print(name.partition("r")) # splits the string into a tuple of three parts: the part before the substring, the substring, and the part after the substring
print(name.rpartition("r")) # splits the string into a tuple of three parts: the part before the substring, the substring, and the part after the substring
print(name.rsplit("r")) # splits the string into a list of substrings
print(name.rsplit(" ")) # splits the string into a list of substrings