import math
import myModule
import requests

'''
 Two types of modules:
 1. Built-in modules: These are modules that come pre-installed with Python. They provide a wide range of functionalities, such as math, random, datetime, etc. You can import and use these modules without any additional installation.
 2. User-defined modules: These are modules that you create yourself. You can define your own functions, classes, and variables in a user-defined module and then import it into other Python scripts to reuse the code. To create a user-defined module, you simply need to save your Python code
'''

print(math.sqrt(16))
myModule.hello()
r = requests.get('https://www.google.com')
print(r.status_code)



