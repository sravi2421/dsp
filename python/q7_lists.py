# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    count = 0
    new_words=[]
    for n in range (len(words)):
        if len(words[n]) >1:
            if words[n][0] == words[n][len(words[n])-1]:
                count += 1
                new_words.append(words[n])
    return count
    raise NotImplementedError


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    new_list = sorted(words)
    x_list=[]
    for n in range(len(new_list)):
        if new_list[n][0] == "x":
            x_list.append(new_list[n])

    for m in range(len(x_list)-1,-1,-1):
        new_list.insert(0, new_list.pop(new_list.index(x_list[m])))

    return new_list
    raise NotImplementedError


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    new_tuples = []
    sorting_list = []
    for n in range(len(tuples)):
        ##sorting_list is a list of tuples with two elements each, below is the encoding
        ## (last element in original tuple, index of tuple within original list of tuples)
        sorting_list.append([tuples[n][len(tuples[n])-1], n])
    sorting_list = sorted(sorting_list)
    for n in range (len(sorting_list)):
        new_tuples.append(tuples[sorting_list[n][1]])
    return new_tuples
    raise NotImplementedError


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    new_nums = []
    to_include = [True]
    ##  iterate through existing list to check if each element is similar to
    ## the element left of it
    for n in range(1, len(nums)):
        if nums[n] == nums[n-1]:
            to_include.append(False)
        else:
            to_include.append(True)

    for m in range(len(nums)):
        if to_include[m]:
            new_nums.append(nums[m])
    return new_nums
    raise NotImplementedError


def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    new_list = list1
    for n in range(0, len(list2)):
        if list2[n]<=new_list[0]:
            new_list.insert(0,list2[n])
        elif list2[n] >= new_list[len(new_list)-1]:
            new_list.append(list2[n])
        else:
            for m in range(len(new_list)):
                if list2[n]>new_list[m] and list2[n] < new_list[m+1]:
                    new_list.insert(m+1, list2[n])
    return new_list
    raise NotImplementedError
