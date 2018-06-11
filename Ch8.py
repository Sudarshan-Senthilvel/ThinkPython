
fruit = "Apple"
print(len(fruit))
print(fruit[0] + fruit[1] + fruit[-1])


# Small Exercise 1 #


def disp_back(word):
    index = len(word) - 1
    while index >= 0:
        print(word[index])
        index = index - 1


disp_back("Sudarshan")
disp_back(" ")
disp_back("S")

print("\n\n")

# Small Exercise 2 #

prefixes = "JKLMNOPQ"
suffix1 = "ack"
suffix2 = "uack"

for i in prefixes:
    if i == "O" or i == "Q":
        print(i + suffix2)
    else:
        print(i + suffix1)


# Small Exercise 3 #

def find(word, letter, after):
    index = after
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


print(find("Sudarshan", "a", 2))


def count_letter(word, letter):
    counter = 0
    for a in word:
        if a == letter:
            counter = counter + 1
    return counter


print(count_letter("Sudarshan", "a"))


# Small Exercise 4 #

def count(word, letter):
    counter = 0
    after = 0
    while True:
        val = find(word, letter, after)
        if val == -1:
            return counter
        else:
            counter = counter + 1
            after = val + 1


print(count("abababaa", "b"))


def in_both(word1, word2):
    for l in word1:
        if l in word2:
            print(l)


in_both("apples", "oranges")


def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    index = 0
    j = len(word2) - 1
    while j >= 0:
        print(index, j)
        if word1[index] != word2[j]:
            return False
        index = index + 1
        j = j - 1
    return True


print(is_reverse('pots', 'stop'))


# Exercise 8-2 #

check_word = "banana"
print(check_word.count("a"))


# Exercise 8-3 #

fruit = "banana"
print(fruit[::-1])


def is_palindrome(word):
    return word[::-1] == word


print(is_palindrome("madam"))
print(is_palindrome("noon"))
print(is_palindrome("apple"))


# Exercise 8-4 #


def any_lowercase1(s):  # Wrong One #
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):  # Wrong One #
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):  # Wrong One #
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):  # Correct Solution #
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):  # Wrong One #
    for c in s:
        if not c.islower():
            return False
    return True


print("\n\n")
print(any_lowercase1("HELLO"))
print(any_lowercase2("HELLO"))
print(any_lowercase3("HELLO"))
print(any_lowercase4("HELLO"))
print(any_lowercase5("HELLO"))
print("\n\n")
print(any_lowercase1("HElLO"))
print(any_lowercase2("HElLO"))
print(any_lowercase3("HElLO"))
print(any_lowercase4("HElLO"))
print(any_lowercase5("HElLO"))


# Exercise 8-5 #


def rotate_word(rword, n):
    new_word = ""
    rword = rword.lower()
    for letter in rword:
        new_word = new_word + chr(ord(letter) + n)
    return new_word


print(rotate_word("abc", 2))
