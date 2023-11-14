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

def image_bits():
    # get width and hieght...
    image_hieght = num_check("Image hidght: ", 1)
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

#image routine goes here
image_bits()


