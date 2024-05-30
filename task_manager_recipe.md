

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string `#TODO`.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def task_manager(text):
    """

    Parameters: 
    string: i.e This is #Todo
       

    Returns: 
        boolean: True or False

    Side effects: 
        None
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

'''
# Takes a string that contains #TODO 
'''
#  Returns True

'''
Takes a string that doesn't contain #TODO 
Returns False
'''

'''
Takes an empty string
Returns False
'''

'''
Takes a None value 
Returns False
'''

'''
A integer instead of a string
Returns False
'''

python
# EXAMPLE


Given a None value
It throws an error

extract_uppercase(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE


Ensure all test function names are unique, otherwise pytest will ignore them!
