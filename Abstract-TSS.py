"""
20200423---Abstraction in OOP by TSS
------------------------------------
Abstraction is the mechanism for declaration methods but not possible
for instantiate. These declared methods can be possible to implement in
sub (child classes) classes with in it's abstract class.
"""

from abc import ABC, abstractclassmethod

class google(ABC):
    def developer(self):
        pass

class jr_developer(google):
    def developer(self):
        return "Mr. Veera will be a Junior developer @ Google"

class sr_developer(google):
    def developer(self):
        return "Mr Veera will be promoted as a Senior Developer @ Google"

#com = google()
j1 = jr_developer()
s1 = sr_developer()
print(j1.developer())
print(s1.developer())

