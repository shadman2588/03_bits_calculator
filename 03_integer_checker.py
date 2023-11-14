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

# Main routine goes here
keep_going = ""
while keep_going == "":
    print()
    # ask the user for an integer (must be more than or equal to 0)
    var_integer = num_check("Enter an integer", 0)
    print()

    # ask for width and height of an image
    # (must be more than or equal to 1)
    image_width = num_check("Image width = ", 1)
    print()
    image_height = num_check("Image height = ", 1)
