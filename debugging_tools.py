x = "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"

'''
Output
Traceback (most recent call last):
  File "demo_ref_keyword_assert.py", line 5, in <module>
AssertionError: x should be 'hello'
'''
