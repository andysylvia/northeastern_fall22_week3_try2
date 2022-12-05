Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> 
>>> def first(word):
...     return word[0]
... 
>>> def last(word):
...     return word[-1]
... 
>>> def middle(word):
...     return word [1:-1]
... 
>>> def is_palindrome(word):
...     if len(word) <=2 and word[0] == word[-1]:
...         print ('True')
...     elif word[0] == word[-1]:
...         is_palindrome(middle(word))
...     else:
...         print ('False')
... 
>>> middle('boat')
'oa'
>>> middle('bot')
'o'
>>> middle('bt')
''
>>> middle('b')
''
>>> middle('')
''
>>> is_palindrome('racecar')
True
>>> is_palindrome('raceecar')
True
>>> is_palindrome('raceca')
False
>>> ^D
$ 