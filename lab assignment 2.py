# 1. For a given input string “Python is a case sensitive language”. Write python
# code for the following:
string1 = "Python is a case sensitive language"
x = len(string1)
y = string1[::-1]
print(x)
print(y)
s1 = slice(10, 26)
print(string1[s1])
print(string1.replace("a case sensitive", "object oriented"))
print(string1.find('a'))
z = string1.replace(' ', '')
print(z)


# 2. Store your name, SID, department name and CGPA into different variables.
# With the help of String formatting print the following output:
# Hey, ABC Here!
# My SID is 2110XXXX
# I am from XYZ department and my CGPA is 9.9
name = 'Tushar yadavendu'
SID = 21102027
department = 'Civil'
cg = 9.9
print("Hey, %s Here!\n My SID is %s \n I am from %s department and my CGPA is %s" % (name, SID, department, cg))
     

print("Hey, {} Here!\nMy SID is {} \nI am from {} department and my CGPA is {}".format(name, SID, department, cg))

# 3. For a=56 and b=10 with the help of bitwise operators calculate the following:
# a. a&b
# b. a|b
# c. a^b
# d. Left shift both a and b with 2 bits.
# e. Right shift a with 2 bits and b with 4 bits.
a= 56
b = 10
print(a & b, a | b, a ^ b, a << 2, b << 2, a >> 2, b >> 4)

# 4. Write a python program to check if the word “name” is present in the string
# entered by the user (Print : “Yes” or “No”).
string2 = input("enter any sentence: ")
if "name" in string2:
    print('Yes')
else:
    print('No')

# 6. Given two numbers ‘a’ and b’. Write a program to count number of bits
# needed to be flipped to convert ‘a’ to ‘b’.
a = 10
b = 20
x = a ^ b
count = 0
while x:
    count += x & 1
    x >>= 1
print(count)


# 5. For any three lengths, there is a simple test to see if it is possible to form a
# triangle. If any of the three lengths is greater than the sum of the other two,
# then you cannot form a triangle. Otherwise, Enter three sides of a triangle,
# converts them to integers, and to check whether the given input lengths can
# form a triangle or not (Print : “Yes” or “No”).
n1 = int(input('enter the side of triangle: '))
n2 = int(input('enter the side of triangle:'))
n3 = int(input('enter the side of triangle: '))
if n1 + n2 > n3 and n1+n3 > n2 and n2+n3 > n1:
    print('yes')
else:
    print('NO')
