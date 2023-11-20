# function goes here

# Puts series of symbols at start and end of text ( for emphasis )
def statement_generator(text, decoration):

    # make string with give characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}" .format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# displays instructions/ information
def instruction():

    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a data type (image / integer / text)")
    print()
    print("This program is assuming that pictures are being represented in 24 bit colour (ie: 24 bit per pixel). For text we assume that ascii encoding is being used (8 bits per character).")
    print()
    print("Complete as many calculation as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    print()
    return""

# check users choice is 'integer', 'text' or 'image'
def user_choice():

    # List of valid response
    text_ok = ["text", "txt", "t"]
    integer_ok = ["integer", "int", "number", "#"]
    image_ok = ["image", "img", "pic", "picture", "p", "pix"]


    valid = False
    while not valid:
        # Ask user for choice and change response to lowercase
        response = input("File type (integer / text / image): ").lower()

        # if they choose "t" or "text", return "text"
        if response in text_ok:
            return "text"

        elif response in integer_ok:
            return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("Press <enter> for an integer or any other key for an image.")
            if want_integer == "":
                return "integer"
            else:
                return "image"
        else:
            # if response is not valid, output an error
            print("Please choose a valid file type!")
            print()

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

# finds # of bits for 24 bit colour
def image_bits():
    # get width and hieght...
    image_hieght = num_check("Image height: ", 1)
    image_width = num_check("Image width: ", 1)

    # calculate # of pixels
    num_pixels = image_width * image_hieght

    # calculate # bits
    num_bits = 24 * num_pixels

    # output answer with work
    print()
    print("# of pixels = {} * {} = {}".format(image_hieght, image_width, num_pixels))
    print("# bits = {} * 24 = {}".format(num_pixels, num_bits))
    print()

    return""

# convert decimal to binary and states how many bits are needed to represent the orginal integer.
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



# Main routine goes here
# Heading
statement_generator("Bit Calculator for Integer, Text & Images", "-")

# Display instructions if the user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue.")

if first_time == "":
    instruction()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)


    # for integers, ask for integer
    if data_type == "integer":
        int_bits()

    # For images, ask for height and width
    # (must be integers more than / equal to 1)
    elif data_type == "image":
        image_bits()

    # for text, ask for string
    else:
        text_bits()

    print()
    keep_going = input(" Press <enter> to continue or any key to quit.")
    print()
