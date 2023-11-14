# checks input is a number more than zero
def num_check(question, low):
    valid = False
    while not valid:

            error = "Please enter a number that is more than zero (or equal to) {}".format(low)

            try:

                 # ask the user to enter a number
                 response = int(input(question))

                 # check if the number is more than zero
                 if response >= low:
                      return response

                 # outputs error if input is invalid
                 else:
                     print(error)
                     print()

            except ValueError:
                print(error)

def int_bits():

    # get integer (must be => 0)
    var_integer = num_check("Please enter an integer: ", 0)

    var_binary = "{0:b}".format(var_integer)

    # calculate # of bits
    num_bits = len(var_binary)


    # output the answer with work
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))
    print()

    return ""

# main routine goes here
int_bits()
