# calculate the # of bits for text (# for character * 8)
def text_bits():

    print()
    # ask user for a string...
    var_text = input("Enter some text: ")

    # Calculate # of bits (length of string * 8)
    var_length = len(var_text)
    num_bits = 8 * var_length

    # output the answer with working
    print()
    print("\'{}\' has {} characters...".format(var_text, var_length))
    print("# of bits is {} * 8...".format(var_length))
    print("we need {} bits to represent {}".format(num_bits, var_text))
    print()

    return ""

# Main routine goes here
text_bits()
