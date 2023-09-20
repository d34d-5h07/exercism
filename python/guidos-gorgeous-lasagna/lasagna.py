"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.
#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
EXPECTED_BAKE_TIME = 40
def bake_time_remaining(time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time

    

#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.

PREPARATION_TIME = 2
def preparation_time_in_minutes(layer):
    """Calculate the preparation time in minutes.
    :param layer: int - number of layers
    :return: int - remaining bake time (in minutes) derived from 'PREPARATION_TIME'.
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return layer * PREPARATION_TIME

#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)

def elapsed_time_in_minutes(layer,time):
    """Calculate total number of minutes the lasagna hass been baking
    :param layer: int - number of lyaer
    :param time: int - elapsed bake time
    :return the total number of minutes you've been cooking, or the sum of your preparation time and the time the lasagna has already spent baking in the oven.
    """
    return layer * PREPARATION_TIME + time
    