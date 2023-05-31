if x / 2 == 1:
        do_two(x)
else:
        do_other(x)



x = 9
if (x %
    2 == 0):
    if (x %
    3 == 0):'Divisible by 6'
    else:
        'Divisible by 2'
else:
    if (x %
        3 == 0):
        'Divisible by 3'
    else:
        'Not divisble by 2 or 3'
        'Divisible by 3'



if (x %
 2 == 0):
 if (x %
 3 == 0):
    'Divisible by 6'
 else:
    if (x %
        3 == 0):   
        'Divisible by 3'
else:
 'Not divisble by 2 or 3'

"Planck's constant:\n quantum of action:\t6.6e-34"
"Planck's constant:\n quantum of action:\t6.6e-34"
print("Planck's constant:\n quantum of action:\t6.6e-34")
Planck's constant:
quantum of action: 6.6e-34


def within(x, lo, hi): # Check if x is within the [lo, hi] range
 return lo <= x and x <= hi # Include hi in the range


 x = 2
 x
2
x = 2.71828
x
2.71828
x = 'two'
x
'two'


a = [1, 'a', False]
a
[1, 'a', False]
len(a)
3
a[2]
False
a[2] = True
a
[1, 'a', True]


s = 'π = 3.14159'
s
'π = 3.14159'
len(s)
11
π = 3.14159
π
3.14159


digits = '0123456789'
digits[3]
'3'
digits[-1]
'9'
digits[-2]
'8'
digits[3:6]
'345'
digits[:-2]
'01234567'


[1, 2, 3] + ['a', 'b']
[1, 2, 3, 'a', 'b']
'011' * 7
'011011011011011011011'
'011' * 0
''
3 in [1, 2, 3]
True
'elm' in ['Elm', 'Asp', 'Oak']
False


total = 0
for x in [5, 4, 3, 2, 1]:
    total += x

total
15

total = 0
for x in [5, 4, 3, 2, 1]:
    total += x
total
File "<stdin>", line 3
total

SyntaxError: invalid syntax


height = [5, 4, 7, 2, 3]
weightedsum = 0
for i in range(len(height)):
    weightedsum += i * height[i]

weightedsum
36
for i, h in enumerate(height):
    weightedsum += i * h

weightedsum

x, y, z = 3, 4, 5
y
4
(x, y, z) = [7, 8, 9]
y


i, h = (0, 5)
weightedsum += i * h
i, h = (1, 4)
weightedsum += i * h
i, h = (2, 7)
weightedsum += i * h
i, h = (3, 2)
weightedsum += i * h
i, h = (4, 3)
weightedsum += i * h

left, middle, right = 'Elm', 'Asp', 'Oak'
left, middle, right
('Elm', 'Asp', 'Oak')
left, middle, right = middle, right, left
left, middle, right
('Asp', 'Oak', 'Elm')

left = middle = right = 'Gum'
left, middle, right
('Gum', 'Gum', 'Gum')

import math
math.pi
3.141592653589793
import os
os.path.splitext('myfile.ext')
('myfile', '.ext')
filename, extension = os.path.splitext('myfile.ext')
extension
'.ext'

extension = os.path.splitext('myfile.ext')

def weightedsum(values, weights, missing=0):
    sum = 0
    for i, val in enumerate(values):
        sum += val * (weights[i] if i < len(weights) else
    missing)
    return sum

weightedsum([4, 9, 16, 25], [2, 2])
26
weightedsum([4, 9, 16, 25], [2, 2], 1)


expression if test_expression else expression


def print(*objects, sep=' ', end='\n', file=sys.stdout,
flush=False):


    import sys
print(print, 'is a', type(print), file=sys.stderr,
sep='\t')
<built-in function print> is a <class
'builtin_function_or_method'>




values = [7, 11, 13, 17, 19]
squares = []
for val in values:
    squares.append(val * val)

squares
[49, 121, 169, 289, 361]
[ x * x for x in values ]
[49, 121, 169, 289, 361]


[ x ** 3 for x in range(10, 21) ]
[1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000]

[ w.split('-') for w in ['ape', 'ape-man', 'hand-me-down'] ]
[['ape'], ['ape', 'man'], ['hand', 'me', 'down']]


[expression for variable in sequence if filter_expression]


[ x ** 3 for x in range(10, 21) if x % 3 != 0 ]
[1000, 1331, 2197, 2744, 4096, 4913, 6859, 8000]

[ c for c in 'We, the People...' if c.isalpha() ]
['W', 'e', 't', 'h', 'e', 'P', 'e', 'o', 'p', 'l', 'e']

try:
    <statements>
except:
    <statements>


try:
 long_running_function()
except KeyboardInterrupt:
 print('Keyboard interrupted long running function')
except IndexError:
 print('Index out of range during long running function')

 raise Exception('No more tickets')

 