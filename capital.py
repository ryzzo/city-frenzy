from create_array import CreateArray
from fetch_data import getCapital



def arrayFormation(capital):
    """Create the required array from the size of the words
    return array and size of capital"""

    size_capital = len(capital)

    # empty array full of dashes
    display_array = CreateArray(size_capital)
    for i in range(size_capital):
        display_array[i] = "_"

    # letters of the capital in an array
    capital_array = CreateArray(size_capital)
    for i in range(size_capital):
        capital_array[i] = capital[i]

    return display_array, capital_array


def checkLetter(capital_array, letter):
    """Check if the letter is available in the array"""
    index = []
    idx = 0
    for element in capital_array:
        if element == letter:
            index.append(idx)
        idx += 1

    if len(index) == 0:
        return None
    return index

def addLetter(display_array, index, letter):
    for i in index:
        display_array[i] = letter
    
    return display_array

def main():
    country_data = getCapital()
    country = country_data[1]
    capital = country_data[2]

    display_array, capital_array = arrayFormation(capital)

    for value in display_array:
        print(value)

capital = "kenya"
display_array, capital_array = arrayFormation(capital)

message = ''.join(capital[i] for i in range(len(capital)))
print(message)

