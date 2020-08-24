'''
judge if the elements are duplicated
'''
def all_unique(lst):
    return len(lst) == len(set(lst))
x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
y = [1, 2, 3, 4, 5]
print("Case 1:")
print(all_unique(x))
print(all_unique(y))

'''
judge if the elements make up the list or string
'''
from collections import Counter
def anagram(first, second):
    return Counter(first) == Counter(second)
print()
print("Case 2:")
print(anagram("abcd3", "3acdb"))
print(anagram([1, 2, 3, 4], [2, 3, 4, 1, 3]))
print(Counter([1, 2, 3, 4, 2]))

'''
get the memory space the variable takes
'''
import sys
variable = 30
print()
print("Case 3:")
print(sys.getsizeof(variable))

'''
get the bytes takes for a string
'''
def byte_size(string):
    return (len(string.encode('utf-8')))
print()
print("Case 4:")
print(byte_size(''))
print(byte_size('Hello World'))

'''
print repeated string
'''
n = 2
s = "Programming"
print()
print("Case 5:")
print(s * n)

'''
Capital the initials of a word
'''
s = "programming is awesome"
print()
print("Case 6:")
print(s.title())

'''
cut a list into pieces of fixed size
'''
from math import ceil
def chunk(lst, size):
    return list(
        map(lambda x: lst[x * size: x * size + size],
        list(range(0, ceil(len(lst) / size))))
    )
print()
print("Case 7:")
print(chunk([1, 3, 4, 5, 6, 7, 8], 2))

'''
filter boolean var, e.g. False, None, 0, ""
'''
def compact(lst):
    return list(filter(bool, lst))
print()
print("Case 8:")
print(compact([0, 1, False, 2, '', 3, 'a', 's', 34]))

'''
zip
'''
array = [['a', 'b'], ['c','d'], ['e', 'f']]
transposed = zip(*array)
print()
print("Case 9:")
transposed
print(transposed)
print(array[0][1])

'''
chain compare
'''
a = 3
print()
print("Case 10:")
print(2 < a < 8)
print(1 == a < 3)

'''
, operator
'''
hobbies = ["basketball", "football", "swimming"]
print()
print("Case 11:")
print("My hobbies are: " + ", ".join(hobbies))

'''
vowel counter
'''
import re
def count_vowels(str):
    return (len(re.findall(r'[aeiou]', str, re.IGNORECASE)))
print()
print("Case 12:")
print(count_vowels('foobar'))
print(count_vowels('gym'))

'''
lower initials
'''
def decapitalize(str):
    return str[:1].lower() + str[1:]
print()
print("Case 13:")
print(decapitalize('FooBar'))
print(decapitalize('Yezi'))

'''
expand list
'''
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret
def deep_flatten(lst):
    result = []
    result.extend(
        spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst)))
    )
    return result
print()
print("Case 14:")
print(deep_flatten([1, [2], [[3], 4], 5]))

'''
listA - listB
'''
def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)
print()
print("Case 15:")
print(difference([1, 2, 3], [1, 2, 4]))

'''
function to realize listA - listB
'''
def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]
from math import floor
print()
print("Case 16:")
print(difference_by([2.1, 1.2], [2.3, 3.4], floor))
print(difference_by([{'x': 2}, {'x': 1}], [{'x': 1}], lambda v: v['x']))

'''
chain function call
'''
def add(a, b):
    return a + b
def substract(a, b):
    return a - b
print()
print("Case 17:")
a, b = 4, 5
print((substract if a > b else add)(a, b))

'''
check if the list has duplicates
'''
def has_duplicates(lst):
    return len(lst) != len(set(lst))
x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
print()
print("Case 18:")
print(has_duplicates(x))
print(has_duplicates(y))

'''
combine two dicts
'''
def merge_two_dicts(a: dict, b: dict):
    c = a.copy()
    c.update(b)
    return c

a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print()
print("Case 19:")
print(merge_two_dicts(a, b))

'''
convert two lists to dict
'''
def to_dictionary(keys: list, values: list):
    return dict(zip(keys, values))
keys = ["a", "b", "c"]
values = [2, 3, 4]
print()
print("Case 20:")
print(to_dictionary(keys, values))

'''
enumerator
'''
lst = ['a', 'b', 'c']
print()
print("Case 21:")
for index, element in enumerate(lst):
    print('Value', element, 'Index', index)

'''
execute time
'''
import time
start_time = time.time()
a = 1
b = 2
c = a + b
print(c)
end_time = time.time()
total_time = end_time - start_time
print()
print("Case 22:")
print('Time: ', total_time)

'''
Try ... except ... else ...
'''
print()
print("Case 23:")
try:
    2 * 3
except TypeError:
    print("An exception was raised")
else:
    print("Thank God, no exceptions were raised.")

'''
return the most frequent element
'''
def most_frequent(list):
    return max(set(list), key = list.count)
lst = [1, 2, 1, 2, 3, 2, 1, 4, 2]
print()
print("Case 24:")
print(most_frequent(lst))

'''
palindrome
eliminate all non-letter characters
'''
def palindrome(str: list):
    from re import sub
    s = sub('[\W_]', '', str.lower())
    return s == s[::-1]
print()
print("Case 25:")
print(palindrome('taco \/.cat'))

'''
'''
import operator
action = {
    '+' : operator.add,
    '-' : operator.sub,
    '/' : operator.truediv,
    '*' : operator.mul,
    '**' : pow
}
print()
print("Case 26:")
print(action['-'](50, 25))

'''
shuffle
'''
from copy import deepcopy
from random import randint

def shuffle(lst):
    temp_lst = deepcopy(lst)
    m = len(temp_lst)
    while (m):
        m -= 1
        i = randint(0, m)
        temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
    return temp_lst

foo = [1,2,3]
print()
print("Case 27")
print(shuffle(foo))

'''
expend list
'''
def spread1(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret
print()
print("Case 28")
print(spread1([1,[4,5,6],[7],8,9]))

'''
swap
'''
def swap(a, b):
    return b, a
a, b = -1, 14
print()
print("Case 29")
print(swap(a, b))

'''
dict default value
'''
d = {'a': 1, 'b': 2}
print()
print("Case 30")
print(d.get('c', 4))