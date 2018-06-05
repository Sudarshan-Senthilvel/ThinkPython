print(type(2))


# Exercise 1-1 #

# ----- Question 1 ----- #
# In a print statement,
# what happens if you leave out one of the parentheses,
# or both?
# ----- Solution Q1 ------ #
# -> results in a compile error


# ----- Question 2 ----- #
# If you are trying to print a string,
# what happens if you leave out
# one of the quotation marks, or both?
# ----- Solution Q2 ----- #
# -> results in a compile error


# ----- Question 3 ----- #
# You can use a minus sign to make
# a negative number like -2.
# What happens if you put a plus sign before a number?
# What about 2++2?
# ----- Solution Q3 ------ #
print(2++2)
# -> Executes without any error


# ----- Question 4 ----- #
# In math notation, leading zeros are okay, as in 02.
# What happens if you try this in Python?
# ----- Solution Q4 ----- #
# -> results in a compile error


# ----- Question 5 ----- #
# What happens if you have two values
# with no operator between them?
# ----- Solution Q5 ----- #
# -> results in a compile error


# Exercise 1-2 #

# ----- Question 1 ----- #
# How many seconds are there in 42 minutes 42 seconds?
# ----- Solution Q1 ----- #
print(42*60 + 42)
# No. of seconds = 2562


# ----- Question 2 ----- #
# How many miles are there in 10 kilometers?
# Hint: there are 1.61 kilometers in a mile.
# ----- Solution Q2 ----- #
one_mile_in_km = 1.61
one_km_in_mile = 1 / one_mile_in_km
ten_km_in_mile = 10 * one_km_in_mile
print(ten_km_in_mile)
# Answer = 6.211180124223602


# ----- Question 3 ----- #
# If you run a 10 kilometer race in 42 minutes 42 seconds,
# what is your average pace
# (time per mile in minutes and seconds)?
# What is your average speed in miles per hour?
# ----- Solution Q3 ----- #
time_ten_km = 42*60 + 42
time_per_mile_in_sec = time_ten_km / ten_km_in_mile
time_per_mile_in_min = time_per_mile_in_sec / 60
print("Time: " + str(time_per_mile_in_min) + " Minutes or "
      + str(time_per_mile_in_sec) + " Seconds")
print("Average speed: " + str(60/time_per_mile_in_min)
      + " Miles per hour")
# Answer
# -> Time per mile in seconds = 412.5
# -> Time per mile in minutes = 6.9
# -> Average Speed = 8.7 miles per hour
