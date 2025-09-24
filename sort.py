# sort package
def sort(width, height, length, mass):
    # validate input values
    if width < 0 or height < 0 or length < 0 or mass < 0:
        raise ValueError("Dimensions and mass must be non-negative")

    # check bulky
    volume = width * height * length
    bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150

    # check heavy
    heavy = mass >= 20

    # decision tree
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# test cases for the sort function
print(sort(10,10,10,5))     # STANDARD
print(sort(200,10,10,5))    # SPECIAL BULKY
print(sort(10,10,10,25))    # SPECIAL HEAVY
print(sort(200,10,10,25))   # REJECTED BULKY HEAVY
print(sort(100,100,100,10)) # SPECIAL BULKY
print(sort(-1,-1,-1,-1))    # ERROR
