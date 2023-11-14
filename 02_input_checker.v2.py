# Function goes here

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


# Main routine goes here
keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("you chose", data_type)

    print()
