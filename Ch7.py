import sys
import math
# Small Exercise 1 #


def print_n(s, n):
    while n > 0:
        print(s)
        n = n - 1


print_n("Apple", 5)
print_n("Apple", 0)
print_n("Apple", -3)

# Square Roots #


def sq_root(a, x):
    y = x
    while True:
        x = y
        y = (x + a / x) / 2
        if abs(x - y) < sys.float_info.epsilon:
            break
    return y


print(sq_root(25, 3))


# Exercise 7-1 #


def mysqrt(a):
    y = a / 2
    while True:
        x = y
        y = (x + a / x) / 2
        if abs(x - y) < sys.float_info.epsilon:
            break
    return y


def test_square_root():
    print("a       mysqrt(a)    math.sqrt(a)   diff")
    print("-       ---------    ------------   ----")
    a = 1.0
    while a < 10.0:
        print(a, "\t", round(mysqrt(a), 1),
              "\t\t", round(math.sqrt(a), 1),
              "\t\t\t", round(mysqrt(a) - math.sqrt(a), 1))
        a = a + 1.0


test_square_root()


# Exercise 7-2 #


def eval_loop():
    while True:
        val = input("Enter the value: ")
        if val == "done":
            break
        else:
            print(val)
            result = eval(val)
            print(result)


eval_loop()


# Exercise 7-3 #


def estimate_pi():
    val = 0
    k = 0
    while True:
        term = (math.factorial(4 * k) * (1103 + 26390 * k)) \
              / ((math.factorial(k) ** 4) * (396 ** (4*k)))
        if term < 1e-15:
            break
        val = val + term
        k = k + 1
    val2 = 2 * math.sqrt(2) / 9801
    val3 = val2 * val
    result = 1 / val3
    print(result)


estimate_pi()
print(math.pi)
