# Ask user for width until they enter a number larger than zero

error = "please input a number larger than zero\n   "

while True :

    try:
        # ask user for a number
        width = float(input("Width: "))

        # check that number is more than zero
        if width > 0:
            break
        else:
            print (error)
    # checks that number is valid
    except ValueError:
        print(error)
