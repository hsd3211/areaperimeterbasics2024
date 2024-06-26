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

# Main routine goes here

keep_going = ""
while keep_going == "":

    # get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")

    # calculate area / perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # display output
    print()
    print(f"perimeter: {perimeter} units")
    print(f"area: {area} square units")

    # ask if the user wants to keep going
    keep_going = input("press enter to restart the program or any key to quit")
    print()

print("Thank you for using the area / perimeter calculator")