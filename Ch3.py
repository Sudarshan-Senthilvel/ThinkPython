def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()

# Exercise 3-1 #

# Write a function named right_justify
# that takes a string named s as a parameter
# and prints the string with enough leading spaces
# so that the last letter of the string is
# in column 70 of the display
# Answer:


def right_justify(s):
    print(" "*(70-len(s)) + s)


right_justify("Apple")


# Exercise 3-2 #

# 1. Type this example into a script and test it.
def do_twice_orig(f):
    f()
    f()


def do_four_orig(f):
    do_twice_orig(f)
    do_twice_orig(f)


def print_spam():
    print('spam')


do_twice_orig(print_spam)
print(" ")

# 2. Modify do_twice so that it takes two arguments,
# a function object and a value,
# and calls the function twice, passing the value as an argument.


def do_twice(f, v):
    f(v)
    f(v)

# 3. Copy the definition of print_twice
# from earlier in this chapter to your script.


def print_twice(bruce):
    print(bruce)
    print(bruce)


# 4. Use the modified version of do_twice
# to call print_twice twice,
# passing 'spam' as an argument.


do_twice(print_twice, "spam")
print(" ")


# 5. Define a new function called do_four
# that takes a function object and a value
# and calls the function four times,
# passing the value as a parameter.
# There should be only two statements in the body
# of this function, not four.

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)


do_four(print_twice, 'spam')


# Exercise 3-3 #

# 1. Write a function that draws a grid

def print_column():
    print("+ - - - -", end=" ")


def print_row():
    print("|        ", end=" ")


def two_rows():
    do_twice_orig(print_row)
    print("|")


def cell_2colls():
    do_twice_orig(print_column)
    print("+")
    do_four_orig(two_rows)


def grid():
    do_twice_orig(cell_2colls)
    do_twice_orig(print_column)
    print("+")


grid()
print(" ")
print(" ")

# 2. Write a function that draws a similar grid
# with four rows and four columns.


def four_rows():
    do_four_orig(print_row)
    print("|")


def cell_4colls():
    do_four_orig(print_column)
    print("+")
    do_four_orig(four_rows)


def new_grid():
    do_four_orig(cell_4colls)
    do_four_orig(print_column)
    print("+")


new_grid()
