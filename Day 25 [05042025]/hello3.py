#import [ hello4]

import hello4
import hello4 as hello5
hello4.palindrome("hello")
hello5.palindrome("racecar")
print(hello5.pangram("qwertyuiopasdfghjklzxcvbnm"))
print(hello5.pangram("hello"))

#o/p
'''
NO
YES
True
False
'''
