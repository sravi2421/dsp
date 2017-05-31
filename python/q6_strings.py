# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if count > 9:
        return 'Number of donuts: many'
    else:
        return 'Number of donuts: {0}'.format(count)
    raise NotImplementedError


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s)>1:
        y = s[0:2]+s[len(s)-2] +s[len(s)-1]
        return y
    else:
        return ''
    raise NotImplementedError


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    str_copy = '' + s[0]
    for n in range(1, len(s)):
        if s[n]==s[0]:
            str_copy = str_copy+'*'
        else:
            str_copy = str_copy + s[n]
    return str_copy
    raise NotImplementedError


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    a_copy = "" + b[0] + b[1]
    b_copy = "" + a[0] + a[1]
    for n in range(2, len(a)):
        a_copy = a_copy+a[n]
    for n in range(2, len(b)):
        b_copy = b_copy+b[n]
    return (a_copy + " " + b_copy)
    raise NotImplementedError


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s) > 2:
        if s[(len(s)-3):(len(s))] == "ing":
            return s + "ly"
        else:
            return s + "ing"
    else:
        return s
    raise NotImplementedError


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    bad_index = -5
    not_index = -5
    for n in range(3, len(s)+1):
        if s[(n-3):n] == "bad":
            bad_index = n-3
        elif s[(n-3):n] == "not":
            not_index = n-3
    if not_index < bad_index:
        str_copy = ""
        for n in range(not_index):
            str_copy = str_copy + s[n]
        return str_copy + "good"
    else:
        return s

    raise NotImplementedError


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    str_copy = ""
    for n in range (len(a)/2 + len(a)%2):
        str_copy = str_copy + a[n]
    for n in range (len(b)/2 + len(b)%2):
        str_copy = str_copy + b[n]
    for n in range (len(a)/2 + len(a)%2, len(a)):
        str_copy = str_copy +a[n]
    for n in range (len(b)/2 + len(b)%2, len(b)):
        str_copy = str_copy + b[n]
    return str_copy
    raise NotImplementedError
