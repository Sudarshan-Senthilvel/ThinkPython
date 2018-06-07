import time

# Recursion

# Countdown


def countdown(n):
    if n <= 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n-1)


countdown(10)

# Print string 'n' times


def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)


print_n("Apple", 3)
print_n("Hello", 0)
print_n("Hi", -5)

# Get the name and print it

# name = input("What is your name? \n")
# print(name)


# Exercise 5-1 #

time_since_epoch = time.time()
print(time_since_epoch)
no_of_days = time_since_epoch // (24*60*60)
print(no_of_days)
seconds_since_midnight = (time_since_epoch % (24*60*60))
no_of_hours = seconds_since_midnight // (60*60)
print(no_of_hours)
no_of_minutes = (seconds_since_midnight // 60) - (no_of_hours*60)
print(no_of_minutes)
no_of_seconds = int(seconds_since_midnight) \
                - (no_of_hours*60*60) \
                - (no_of_minutes*60)
print(no_of_seconds)
print("\n No of days since Epoch: ", no_of_days)
print("\n Time -> " + str(no_of_hours) + " : "
      + str(no_of_minutes) + " : "
      + str(no_of_seconds))


# Exercise 5-2 #

# Question 1 #

def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that does n’t work.")


# Question 2 #

def values_for_fermat():
    a = int(input("Value of a: "))
    b = int(input("Value of b: "))
    c = int(input("Value of c: "))
    n = int(input("Value of n: "))
    check_fermat(a, b, c, n)


values_for_fermat()


# Exercise 5-3 #

def is_triangle(a, b, c):
    if a + b < c or b + c < a or c + a < b:
        print("No!, you cannot form a triangle")
    else:
        print("Yes!, you can form a triangle")


def sides_of_triangle():
    a = int(input("Side a: "))
    b = int(input("Side b: "))
    c = int(input("Side c: "))
    is_triangle(a, b, c)


sides_of_triangle()


# Exercise 5-4 #

def recurse(n, s):
    """ A function that takes a value n and s
    calls recursively n times,
    decrementing value of n in each call and
    adding value of n to s
    :param n: number of recursive calls
    :param s: variable that tracks the sum
    """
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)


recurse(3, 0)
# recurse(-1, 0)

