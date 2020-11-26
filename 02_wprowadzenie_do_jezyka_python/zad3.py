def function(text, letter):
    return set(text).difference(letter)
# difference returns set of value difference , you can use counter function to count repeated values and substract them
# Task in question didnt specify which way it should be solved

print(function("Pizza man", "Dungeon dicer"))