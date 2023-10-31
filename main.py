# Anastasia Lobanov
# Encode function

def encode(password):
    new = ""
    for element in password:
        new_element = int(element) + 3
        new_element = str(new_element)
        new += new_element[-1]
    return new
