


def to_usd(my_price):
    """
    This is a docstring. It tells us what this function is about. 
    What its responsibilites are
    What the params are about
    What datatypes the params are
    What this funciton will return
    Example of invoking the function

    Invoke like this: to_usd(9.999)
    """
    return '${:,.2f}'.format(my_price)

if __name__ == "__main__":
    # nesting code in the main conditional allows other scripts to cleanly import fucntions from this file
    
    price = input("please choose a price like 4.9999:")
    print(to_usd(float(price)))

