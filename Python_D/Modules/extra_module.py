'''
__doc__ 
__file__
__name__
__loader
__package__

'''
import os
print(__doc__) # Print whatever we have added at the top which we added for documentation 

print("File Name ",__file__) # File Name  /Users/kaliprasad/Documents/PythonCourse/Python_D/Modules/extra_module.py

print("Absolute Module ", os.path.abspath(__file__)) # /Users/kaliprasad/Documents/PythonCourse/Python_D/Modules/extra_module.py

print("Directory Path ", os.path.dirname(__file__)) # Directory Path  /Users/kaliprasad/Documents/PythonCourse/Python_D/Modules

print(__name__)