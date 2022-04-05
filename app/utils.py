


def to_usd(my_price):
    """
    takes in an float number value,
    returns a string with an appended $ sign 
    and number formatted to 2 decimal places
    Invoke like this: to_usd(9.999)
    """
    return '${:,.2f}'.format(my_price)

if __name__ == "__main__":
    # nesting code in the main conditional allows other scripts to cleanly import fucntions from this file
    
    price = input("please choose a price like 4.9999:")
    print(to_usd(float(price)))

