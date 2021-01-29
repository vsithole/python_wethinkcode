
def move_square(size, degrees):
    print("Moving in a square of size "+str(size))
    for i in range(4):
       
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")


def move_cicle():
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")


def move_rectangle(length, width, degrees):
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")


def dancing_square(size, length, degrees):
    size = 20
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        print("* Move Forward "+str(length))
        print("Moving in a square of size "+str(size))
        for j in range(4):
            print("* Move Forward " + str(size))
            print("* Turn Right " + str(degrees) + " degrees")


def crop_circle(size, length, degrees):
    length = 20
    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward "+str(length))
        move_cicle()


def move():
    size = 10
    length = 20
    width = 10
    degrees = 90

    move_square(size, degrees)
    move_rectangle(length, width, degrees)
    move_cicle()
    dancing_square(size, length, degrees)
    crop_circle(size, length, degrees)


def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
