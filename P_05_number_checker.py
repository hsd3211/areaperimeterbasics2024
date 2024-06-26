# Ask user for width until they enter a number larger than zero

def numcheck(question):

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


for item in range(0, 2):
    width = numcheck("Width: ")
    print(width)

print()

for item in range(0, 2):
    height = numcheck("Height: ")
    print(height)