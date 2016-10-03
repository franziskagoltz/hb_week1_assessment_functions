# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%


# Setting the tax parameter to a default value of 5%
def item_cost(price, state, tax=0.05):
    """ calculates the total price based on the state's tax rate.

    >>> item_cost(5, "CA")
    5.35

    >>> item_cost(5, "AL")
    5.25

    """

    # Checking the state, and if it's CA we set the tax to 7% inside the function.
    # Then we calculate the total cost
    if state == "CA":
        tax = 0.07
        return price + price * tax
    else:
        return price + price * tax



#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.


def is_berry(fruit):
    """ checks if the passed fruit is a strawberry, cherry, or blackberry.

    >>> is_berry("strawberry")
    True

    >>> is_berry("raspberry")
    False

    """
    berries = ["strawberry", "cherry", "blackberry"]
    # returns true if the passed argument is found in the berries list
    return fruit in berries


def shipping_cost(fruit):
    """ calculates the shipping cost of a fruit by checking the is_fruit function.
    if is_fruit is true, the berry ships for free (returns 0), else it return 5

    >>> shipping_cost("strawberry")
    0

    >>> shipping_cost("raspberry")
    5

    """
    if is_berry(fruit):
        return 0
    else:
        return 5


def is_hometown(city):
    """ evaluates the town and return `True` if it is my hometown (Berlin), and `False` otherwise

    >>> is_hometown("Berlin")
    True

    >>> is_hometown("San Francisco")
    False

    """

    if city == "Berlin":
        return True
    else:
        return False


def full_name(first, last):
    """ takes first and last name as arguments, returns the full name.

    >>> full_name("Jane", "Balloon")
    'Jane Balloon'

    >>> full_name("Grace", "Hopper")
    'Grace Hopper'

    """

    # Using the join method
    return " ".join([first, last])


def hometown_greeting(city, first_name, last_name):
    """ greets a person with the full name, based on what hometown they are from.

    >>> hometown_greeting("Berlin", "Jane", "Balloon")
    Hi, Jane Balloon, we're from the same place!

    >>> hometown_greeting("San Francisco", "Grace", "Hopper")
    Hi, Grace Hopper, where are you from?

    """

    # checks if the hometown matches the hometown passed in the is_hometown function
    # uses the join method to create the response
    if is_hometown(city):
        print "".join(["Hi, ", full_name(first_name, last_name), ", we're from the same place!"])
    else:
        print "".join(["Hi, ", full_name(first_name, last_name), ", where are you from?"])

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#####################################################################


def increment(x):
    """ uses a nested function (add) to add two integers together

    """
    def add(y):
        """
        addfive = increment(x=5)

        >>> addfive(y=5)
        10

        >>> addfive(y=20)
        25
        """
        return x + y
    return add

# calling the increment function with named argument set to 5 and storing the result in the addfive variable, 
# turning addfive into a function (to access it's nested function)
addfive = increment(x=5)

# calling the addfive function twice with different parameters
addfive(y=5)
addfive(y=20)


def append_list(num, list_of_nums):
    """ appends a number to a list of numbers

    >>> append_list(5, [1, 2, 3, 4])
    [1, 2, 3, 4, 5]

    >>> append_list(100, [10, 20, 30, 40, 50])
    [10, 20, 30, 40, 50, 100]

    """

    # appending the passed number to the passed list
    list_of_nums.append(num)

    # returning that list
    return list_of_nums


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
