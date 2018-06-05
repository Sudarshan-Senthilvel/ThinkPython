import math

# Exercise 2-1 #

# We’ve seen that n = 42 is legal. What about 42 = n?
# Answer: compile error

# How about x = y = 1?
x = y = 1  # Answer: Works!

# In some languages every statement ends with a semicolon, ;.
# What happens if you put a semicolon
# at the end of a Python statement?
# Answer: Gives a warning message, but compiles and runs.

# What if you put a period at the end of a statement?
# Answer: compile error

# In math notation you can multiply x and y
# like this: xy. What happens if you try that in Python?
xy = 1  # Answer: 'xy' is taken as a variable name.


# Exercise 2-2 #

# ----- Question 1 ----- #
# The volume of a sphere with radius r is (4/3)πr^3.
# What is the volume of a sphere with radius 5?
# ----- Solution Q1 ------ #
volume = (4/3)*math.pi*(5**3)
print(volume)
# Volume: 523.5987755982989

# ----- Question 2 ----- #
# Suppose the cover price of a book is $24.95,
# but bookstores get a 40% discount.
# Shipping costs $3 for the first copy
# and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?
# ----- Solution Q2 ----- #
cover_price = 24.95
discounted_price = cover_price - (0.4*cover_price)
wholesale_cost = 60*discounted_price + 3 + 0.75*59
print(wholesale_cost)
# Wholesale cost: 945.4499999999999

# ----- Question 3 ----- #
# If I leave my house at 6:52 am and
# run 1 mile at an easy pace (8:15 per mile),
# then 3 miles at tempo (7:12 per mile) and
# 1 mile at an easy pace again,
# what time do I get home for breakfast?
# ----- Solution Q3 ----- #
time_elapsed_seconds = 1*((8*60)+15) + 3*((7*60)+12) + 1*((8*60)+15)
time_elapsed_minutes = time_elapsed_seconds / 60
print(time_elapsed_minutes)
start_time = 6*60 + 52
end_time_hrs = int((start_time + time_elapsed_minutes) / 60)
end_time_min = int((start_time + time_elapsed_minutes) % 60)
print(str(end_time_hrs) + ":" + str(end_time_min))
# End time -> 7:30 am

