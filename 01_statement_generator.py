# function goes here

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

# Main rotuine goes here
statement_generator("Look - stars", "*")