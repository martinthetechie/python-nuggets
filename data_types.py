"""
List, Tuples and Dictionaries

Lists and tuples are ordered collections, while dictionaries are unordered.
Lists are mutable, tuples are immutable, and dictionaries are mutable.
Lists and tuples can contain any type of data, while dictionaries require keys to be hashable (typically strings or numbers).
Lists and tuples are accessed by index, while dictionaries are accessed by key.
"""

from enum import Enum
class Food(Enum):
    BAN_MIAN = "Ban Mian"
    CHICKEN_RICE = "Chicken Rice"
    LAKSA = "Laksa"
    TOAST = "Toast"
    ROTI_PRATA = "Roti Prata"

"""
Operators on each data structures differ due to the fundamental differences of mutability and as well as data structure.
"""

# Function to operate on a list of foods
def operate_on_list():
    foods_list = [food.value for food in Food]
    print("List of foods:", foods_list)
    
    # Modify a list element
    foods_list[0] = "Noodle Soup"
    print("Modified list:", foods_list)

# Function to operate on a tuple of foods
def operate_on_tuple():
    foods_tuple = tuple(food.value for food in Food)
    print("Tuple of foods:", foods_tuple)
    
    # Try to modify a tuple element (this will raise an error)
    try:
        foods_tuple[0] = "Noodle Soup"
    except TypeError as e:
        print("Error:", e)

# Function to operate on a dictionary of foods
def operate_on_dictionary():
    foods_dict = {food.name: food.value for food in Food}
    print("Dictionary of foods:", foods_dict)
    
    # Add a new key-value pair
    foods_dict["RAMEN"] = "Ramen"
    print("Dictionary after adding a new key-value pair:", foods_dict)
    
    # Remove a key-value pair
    del foods_dict["TOAST"]
    print("Dictionary after removing a key-value pair:", foods_dict)

# Call the functions
operate_on_list()
print("\n---------------------------------\n")
operate_on_tuple()
print("\n---------------------------------\n")
operate_on_dictionary()
