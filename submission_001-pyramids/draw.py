

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    try:
        shape = input("Shape?: ")
        shape = shape.lower()
        if shape == "pyramid" or shape == "triangle" or shape == "square" or shape == "parallelogram" or shape == "trapeziod" or shape == "rectangle":         
            return shape
        else:
            return get_shape()
    except (ValueError):
        return get_shape()

# TODO: Step 1 - get height (it must be int!)
def get_height():
    try:
        height = int(input("Height?: "))
        if height <= 80 and height > 0:
            return height
        else:
            print ("Height max is 80")

    except (ValueError):
        return get_height()


# TODO: Step 2
def draw_pyramid(height, outline):
    inp = height
    inb = 1
    if outline == True:
        x = inp
        while inp > 0:
            y = 0
            while y < x:
                if y == x-1 or inp == 1 or y == inp-1:
                    print("*",end="")
                else:
                    print(" ",end="")
                y += 1
            print("")
            x += 1
            inp -= 1
    else:
        for z in range(inp):
            inp -= 1
            print(" "*inp+ "*"*inb + ""*inp,end="")
            print("")
            inb += 2 


# TODO: Step 3
def draw_square(height, outline):
    for i in range(height):
        for x in range(height):
            if outline == True:
                if i == 0 or x == 0 or i == height-1 or x == height-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            else:    
                print("*",end="")
        print("")


# TODO: Step 4
def draw_triangle(height, outline):
    for row in range(height):
        for col in range(row+1):
            if outline == True:
                if row == col or col == 0 or row == height-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                print("*",end="")
        print("")

#Extra shapes code starts here--------------
def parallelogram(height, outline):

    inb = 2 + height
    if outline == False:
        for z in range(height):
            height -= 1
            print(" "*height+ "*"*inb + " "*height,end="")
            print("")
    else:
        for row in range (height):
            for col in range (height+2):
                if (row == 0 and col == ((height - 1) + height)) or row == height -1 or (col + row) == (height - 1) or (col - row) == (height - 1):
                    print("*",end="")
                else:
                    print(end=" ")
            print("")   

def trapeziod(height, outline):

    inb = height - 2
    if outline == False:
        for z in range(height):
            height -= 1
            print(" "*height+ "*"*inb + " "*height,end="")
            print("")
            inb += 2 
 
def rectangle(height, outline):
    if outline == False:
        for i in range(height):
            for x in range(height * 4):
                print("*",end="")
            print("")
    else:
        for i in range(height):
            for x in range(height* 4):
                if i == 0 or x == 0 or i == height-1 or x == (height*4)-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print("")

#Extra shapes code ends here--------------

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height, outline)
    elif shape == "square":
        draw_square(height, outline)
    elif shape == "triangle":
        draw_triangle(height, outline)      
    elif shape == "parallelogram":
        parallelogram(height, outline)
    elif shape == "trapeziod":
        trapeziod(height, outline)
    elif shape == "rectangle":
        rectangle(height, outline)
    else:
        print("Enter the correct shape")

# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input("Outline only? (y/N): ")
    outline = outline.lower()
    if outline == "y":
        return True
    if outline == "n" or outline == "":
        return False
    

if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

