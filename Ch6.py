import math
# Small Exercise 1 #


def compare_func(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1


print(compare_func(5, 1))
print(compare_func(5, 5))
print(compare_func(1, 5))


# Small Exercise 2 #


def hypotenuse(adj, opp):
    return math.sqrt(float(adj)**2 + float(opp)**2)


print(hypotenuse(3, 4))


# Area of a circle #


def area(xc, yc, xp, yp):
    radius = math.sqrt((xp - xc) ** 2 + (yp - yc) ** 2)
    return math.pi * radius ** 2


print(area(0, 0, 4, 4))


# Small Exercise 3 #

def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False


print(is_between(2, 4, 6))
print(is_between(6, 4, 2))
print(is_between(2, 6, 4))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))


def factorial(n):
    space = " " * (4 * n)
    print(space + "factorial " + str(n))
    if n == 0:
        print("returning 1")
        return 1
    else:
        result = n * factorial(n-1)
        print(space + "returning " + str(result))
        return result


print(factorial(4))


# Exercise 6-1 #


def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod


def a(x, y):
    x = x + 1
    return x * y


def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square


x1 = 1
y1 = x1 + 1
print(c(x1, y1+3, x1+y1))


# Exercise 6-2 #
# Ackermann function #


def ack(m, n):
    if m == 0:
        return n + 1
    elif n == 0 and m > 0:
        return ack(m-1, 1)
    elif n > 0 and m > 0:
        return ack(m - 1, ack(m, n-1))


print(ack(3, 4))
# print(ack(12, 15))
# maximum recursion depth exceeded in comparison


# Exercise 6-3 #


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


print(middle("hi"))
print(middle("h"))
print(middle(""))


def is_palindrome(word):
    length = len(word)
    if length == 1 or length == 0:
        print("The word is a Palindrome!")
    elif length == 2:
        if first(word) == last(word):
            print("The word is a Palindrome!")
        else:
            print("Not a Palindrome!")
    else:
        if first(word) == last(word):
            is_palindrome(middle(word))
        else:
            print("Not a Palindrome!")


is_palindrome("noon")
is_palindrome("madam")
is_palindrome("Apple")
is_palindrome('allen')
is_palindrome('bob')
is_palindrome('otto')
is_palindrome('redivider')


# Exercise 6-4 #

def is_power(a1, b1):
    if a1 % b1 == 0:
        if a1 == b1:
            print("Yes!")
        else:
            is_power(a1 / b1, b1)
    else:
        print("No!")


is_power(8.0, 2)
is_power(7, 2)
is_power(9, 3)


# Exercise 6-5 #

def gcd(a1, b1):
    if b1 == 0:
        return a1
    else:
        return gcd(b1, a1 % b1)


print(gcd(12, 3))
print(gcd(2, 10))
print(gcd(12, 2))
