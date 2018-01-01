# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


"""
Given an int count of a number of donuts, return a string of the
form 'Number of donuts: <count>', where <count> is the number
passed in. However, if the count is 10 or more, then use the word
'many' instead of the actual count.
"""
def donuts(count):
    if count < 10:
        return f"Number of donuts: {count}"
    else:
        return "Number of donuts: many"

"""
Given a string s, return a string made of the first 2 and the last
2 chars of the original string, so 'spring' yields 'spng'.
However, if the string length is less than 2, return instead the
empty string.
"""
def both_ends(s):
    if len(s) < 2: return ""
    return s[:2] + s[-2:]


"""
Given a string s, return a string where all occurences of its
first char have been changed to '*', except do not change the
first char itself. e.g. 'babble' yields 'ba**le' Assume that the
string is length 1 or more.
"""
def fix_start(string):
    first_char = string[0]
    result = first_char

    for letter in string[1:]:
        if letter == first_char:
            result += "*"
        else:
            result += letter

    return result


"""
Given strings a and b, return a single string with a and b
separated by a space '<a> <b>', except swap the first 2 chars of
each string. Assume a and b are length 2 or more.
"""
def mix_up(a, b):
    first = b[0:2] + a[2:]
    second = a[0:2] + b[2:]
    return f"{first} {second}"


"""
Given a string, if its length is at least 3, add 'ing' to its end.
Unless it already ends in 'ing', in which case add 'ly' instead.
If the string length is less than 3, leave it unchanged. Return
the resulting string.
"""
def verbing(string):
    if len(string) >= 3:
        if string[-3:] == "ing":
            return string + "ly"
        else:
            return string + "ing"
    else:
        return string


"""
Given a string, find the first appearance of the substring 'not'
and 'bad'. If the 'bad' follows the 'not', replace the whole
'not'...'bad' substring with 'good'. Return the resulting string.
So 'This dinner is not that bad!' yields: 'This dinner is
good!'
"""
def not_bad(string):
    not_index = string.find("not")
    bad_index = string.find("bad")
    if not_index > -1 and bad_index > -1 and bad_index > not_index:
        return string[:not_index] + "good" + string[(bad_index + 3):]
    else:
        return string


"""
Consider dividing a string into two halves. If the length is even,
the front and back halves are the same length. If the length is
odd, we'll say that the extra char goes in the front half. e.g.
'abcde', the front half is 'abc', the back half 'de'. Given 2
strings, a and b, return a string of the form a-front + b-front +
a-back + b-back
"""
import math
def front_back(a, b):
    a_middle_index = math.ceil(len(a) / 2)
    b_middle_index = math.ceil(len(b) / 2)
    a_front = a[:a_middle_index]
    b_front = b[:b_middle_index]
    a_back = a[a_middle_index:]
    b_back = b[b_middle_index:]
    return a_front + b_front + a_back + b_back

# TESTS

# donuts()
print("donuts(4) == 'Number of donuts: 4'", donuts(4) == 'Number of donuts: 4')
print("donuts(9) == 'Number of donuts: 9'", donuts(9) == 'Number of donuts: 9')
print("donuts(10) == 'Number of donuts: many'", donuts(10) == 'Number of donuts: many')
print("donuts(99) == 'Number of donuts: many'", donuts(99) == 'Number of donuts: many')
print()

# both_ends()
print("both_ends('spring') == 'spng'", both_ends('spring') == 'spng')
print("both_ends('Hello') == 'Helo'", both_ends('Hello') == 'Helo')
print("both_ends('a') == ''", both_ends('a') == '')
print("both_ends('xyz') == 'xyyz'", both_ends('xyz') == 'xyyz')
print()

# fix_start()
print("fix_start('babble') == 'ba**le'", fix_start('babble') == 'ba**le')
print("fix_start('aardvark') == 'a*rdv*rk'", fix_start('aardvark') == 'a*rdv*rk')
print("fix_start('google') == 'goo*le'", fix_start('google') == 'goo*le')
print("fix_start('donut') == 'donut'", fix_start('donut') == 'donut')
print()

# mix_up()
print("mix_up('mix', 'pod') == 'pox mid'", mix_up('mix', 'pod') == 'pox mid')
print("mix_up('dog', 'dinner') == 'dig donner'", mix_up('dog', 'dinner') == 'dig donner')
print("mix_up('gnash', 'sport') == 'spash gnort'", mix_up('gnash', 'sport') == 'spash gnort')
print("mix_up('pezzy', 'firm') == 'fizzy perm'", mix_up('pezzy', 'firm') == 'fizzy perm')
print()

# verbing()
print("verbing('hail') == 'hailing'", verbing('hail') == 'hailing')
print("verbing('swiming') == 'swimingly'", verbing('swiming') == 'swimingly')
print("verbing('do') == 'do'", verbing('do') == 'do')
print()

# not_bad()
print(
    "not_bad('This movie is not so bad') == 'This movie is good'",
    not_bad('This movie is not so bad') == 'This movie is good'
)
print(
    "not_bad('This dinner is not that bad!') == 'This dinner is good!'",
    not_bad('This dinner is not that bad!') == 'This dinner is good!'
)
print(
    "not_bad('This tea is not hot') == 'This tea is not hot'",
    not_bad('This tea is not hot') == 'This tea is not hot'
)
print(
    'not_bad("It\'s bad yet not") == "It\'s bad yet not"',
    not_bad("It's bad yet not") == "It's bad yet not"
)
print()


# front_back()
print("front_back('abcd', 'xy') == 'abxcdy'", front_back('abcd', 'xy') == 'abxcdy')
print("front_back('abcde', 'xyz') == 'abcxydez'", front_back('abcde', 'xyz') == 'abcxydez')
print("front_back('Kitten', 'Donut') == 'KitDontenut'", front_back('Kitten', 'Donut') == 'KitDontenut')
print()
