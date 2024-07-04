# Ask user for width until they enter a number larger than zero

def num_check(question):

    error = "please input a number larger than zero\n"

    while True :

        try:
            # ask user for a number
            response = float(input(question))

            # check that number is more than zero
            if response > 0:
                return response
            else:
                print (error)
        # checks that number is valid
        except ValueError:
            print(error)


def dollar_check(question):

    error = "please input a number larger than zero\n"

    while True :

        try:
            # ask user for a number
            response = str(input(question))
            floatr = float(response.replace("$", ""))

            # check that number is more than zero
            if floatr > 0:
                return floatr
            else:
                print (error)
        # checks that number is valid
        except ValueError:
            print(error)


# Main routine goes here

keep_going = ""
while keep_going == "":

    # get width and height
    width = num_check("Width: ")
    height = num_check("Length: ")
    price_per_unit = dollar_check("Cost / m: ")

    # calculate  perimeter and cost
    perimeter = 2 * (width + height)
    cost = perimeter * price_per_unit

    # display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Cost: ${cost:.2f}")

    # ask if the user wants to keep going
    keep_going = input("press enter to restart the program or any key to quit ")
    print()

print("Thank you for using the fence calculator")