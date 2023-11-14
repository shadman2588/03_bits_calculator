
# Puts series of symbols at start and end of text ( for emphasis )
def statement_generator(text, decoration):

    # make string wtih give characters
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

# Main routine goes here
instruction()