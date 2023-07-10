#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#will print 5 

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#undefined because number of days in a week is not defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#Will print 5 because once it returns the 5 it exits the fucntion

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#Will print 5 for the return and exit the function the print 10 will not print to the console

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#Will print 5 for the print statement but will print none/null because there is no value for x when the function is called. 

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#Will print 3,5 line 37 will not print because there is no return values for line 36 it's just printing to the console. 

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#print 25 because they are turning the integers into strings so they won't add but concatenate

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
        return 7
print(number_of_oceans_or_fingers_or_continents())
#Will print 100, and 10 will be the held value

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#Will print 7,14, (7+14 fot lines 67) = 21 

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#Will print 8 runs line 72 and exits the function

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#Will print 500 (line79),500 (line83),300 (function gets called b turns to 300),500 (line 85 and b=500 from line 78)

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#Will print 500 (line 90), 500(print b again from line 89), 300 (line 93), 500 (line 89 again)

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#Will print 500 (from line 101), 500 (again from line 101), b becomes the function foobar print 300, 300 (b becomes 300 from the return and variable)

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#will print 1 from line 114, then bar gets called print 3 go back to line 116 and print 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#Will print 1 from line 124, print 3 from line 129, return 5 which prints to 5 as x, return 10 to variable y

























