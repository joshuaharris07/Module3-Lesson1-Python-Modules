# Mastering Python Modules and Aliases
# Objective: The aim of this assignment is to enhance your proficiency in using Python modules, 
# both standard and custom,with a specific focus on importing with aliases.

# Task 1: Custom Module with Aliases 

# Problem Statement: Create a custom module named `text_utils.py` with functions for string manipulation 
# (e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.

# Expected Outcome: Your main script should be able to use the functions from `text_utils.py` via an alias, 
# demonstrating an understanding of custom module creation and aliasing.

import text_utils as tu

action = input("Would you like to reverse a phrase, or capitalize it? (reverse/capitalize): ").lower()
s = input("Please enter the phrase: ")
if action == "reverse":
    print(tu.reverse_string(s))
elif action == "capitalize":
    print(tu.capitalize_string(s))