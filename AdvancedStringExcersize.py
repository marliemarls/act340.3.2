#Problem 1:
stringy = "You can learn more from failure than from success."
print(stringy[0 : 3], stringy[-1])

#Problem 2:
print(stringy.replace(".", "!"))

#Problem 3:
new_str= "“WHEN YOU Change your thougHts, remember to ALSO change your world.”"
str_lower = new_str[1: -2].lower()
print(str_lower)

#Problem 4:
str_capital = new_str[1: -2].capitalize()

#Problem 5: 
new_str_5= "There are no traffic jams along the extra mile."
print(new_str_5.startswith("Z"))
print(new_str_5.startswith("t"))

#Problem 6: 
# index_of = new_str.index('j')
# print(index_of)

#Problem 7: 
a = new_str.count("t")
b = new_str.count("o")
print("The letter 't' appears {} times and the letter 'o' appears {} times.".format(a,b))

print(f"The letter 't' appears {a} times and the letter 'o' appears {b} times.")

#Problem 8: 
greeting= "Good Morning!"
print(len(greeting))

#Problem 9:
alphabet= "abcdefghijklmnopqrstuvwxyz"
print(alphabet.isalpha())

#Problem 10:
learning = "Learning is fun!"
print(learning.find("y"))
print(learning.index("y"))
#Both methods are used to look up values in a sequence type in Python. The difference between the find method is that it will return -1 as an output if it cannot find the substring and can be used in conditional statements. Index throws a valueerror exception and cannot be used in conditional statements because it will render an error. 

#Problem 11:
count_string= "Twinkle twinkle little star, how I wonder what you are"

print(count_string.count())

