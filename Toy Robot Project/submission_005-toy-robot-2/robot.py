def check_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
def get_robot_name():
    robot_name = input("What do you want to name your robot? ")
    print(robot_name+": Hello kiddo!")
    return robot_name

def get_help_message():
    message = "I can understand these commands:\nOFF  - Shut down robot\nHELP - provide information about commands\nForward - Moves your robot forward\nBack - Moves your robot back\nSprint to sprint forward"
    return message

def forward_print(robot_name,y,inp): 
    print(" > "+robot_name+" moved forward by",inp,"steps.")

def back_print(robot_name,y,inp): 
    print(" > "+robot_name+" moved back by",inp,"steps.")

def forward(inp,y,x,pos):
    count = 0
    if pos == 0:
        y += inp
        if y > 200:
            y -= inp
            count += 1

    elif pos == 90 or pos == -270:
        x += inp
        if x > 100:
            x -= inp
            count += 1
            
    elif pos == 180 or pos == -180:
        y -= inp
        if y < -200:
            y += inp
            count += 1
    elif pos == 270 or pos == -90:
        x -= inp
        if x < -100:
            x += inp
            count += 1
    return y,x,count

def back(inp,y,x,pos):
    count = 0
    if pos == 0:
        y -= inp

    elif pos == 90 or pos == -270:
        x -= inp
 
    elif pos == 180 or pos == -180:
        y += inp

    elif pos == 270 or pos == -90:
        
        x += inp

    return y,x,count

def right(robot_name,pos):
    pos = pos + 90
    print(" > {} turned right.".format(robot_name))
    if pos == 360:
        pos = 0
    return pos

def left(robot_name,pos):
    pos = pos - 90
    print(" > {} turned left.".format(robot_name))
    if pos == -360:
        pos = 0
    return pos

def safe_zone(robot_name):
    print("{}: Sorry, I cannot go outside my safe zone.".format(robot_name))

def sprint(inp,y,x,pos,robot_name):
    if inp == 0:
        if pos == 0:
            return y
        elif pos == 90 or pos == -270:
            return x
        elif pos == 180 or pos == -180:

            return y
        elif pos == 270 or pos == -90:
            return x
    else:
        count = 0
        if pos == 0:
            y += inp
            forward_print(robot_name,y,inp)
            y = sprint(inp - 1,y,x,pos,robot_name)
            return y
        elif pos == 90 or pos == -270:
            x += inp
            forward_print(robot_name,y,inp)
            x = sprint(inp - 1,y,x,pos,robot_name)
            return x
        elif pos == 180 or pos == -180:
            y -= inp
            forward_print(robot_name,y,inp)
            y = sprint(inp - 1,y,x,pos,robot_name)
            return y
        elif pos == 270 or pos == -90:
            x -= inp
            forward_print(robot_name,y,inp)
            x = sprint(inp - 1,y,x,pos,robot_name)
            return x
        return y,x
def get_command_input(robot_name):
    
    x = 0
    y = 0
    pos = 0
    count = 0

    user_command = ''
    try:
        while user_command.lower() != 'off':
            user_input_command = input(robot_name+": What must I do next? ")

            user_command_list = user_input_command.split(' ')
            user_command = user_command_list[0]

            if len(user_command_list) > 1:  
                int_results = check_int(user_command_list[1])
                if int_results == True:
                    inp = int(user_command_list[1])
                    if user_command == "sprint":
                        if pos == 0:
                            y = sprint(inp,y,x,pos,robot_name)
                        elif pos == 90 or pos == -270:
                            x = sprint(inp,y,x,pos, robot_name)
                        elif pos == 180 or pos == -180:
                            y = sprint(inp,y,x,pos, robot_name)
                        elif pos == 270 or pos == -90:
                            x = sprint(inp,y,x,pos, robot_name)
                 
                    elif user_command == "forward":
                        y,x,count = forward(inp,y,x,pos)
                    
                    elif user_command == "back":               
                        y,x,count = back(inp,y,x,pos)
                else:
                    print(robot_name+": Sorry, I did not understand '"+user_input_command+"'.")
                    continue

            commands_list = ["off","help","forward", "back", "right", "left","sprint"]
            current_position = " > {} now at position ({},{}).".format(robot_name,x,y)

            if user_command.lower() not in commands_list:
                print(robot_name+": Sorry, I did not understand '"+user_input_command+"'.")

            elif user_command.lower() == "help":
                print(get_help_message()) 

            elif user_command.lower() == "forward":
                if count == 0:
                    forward_print(robot_name, y,inp)
                else:
                    safe_zone(robot_name)
                    count -= 1  
                print(current_position)

            elif user_command.lower() == "back": 
                if count == 0:
                    back_print(robot_name, y,inp)
                else:
                    safe_zone(robot_name)
                    count -= 1  
                print(current_position)

            elif user_command.lower() == "sprint":
                if count == 0:
                    pass
                else:
                    safe_zone(robot_name)
                    count -= 1  
                print(current_position)

            elif user_command.lower() == "right":
                pos = right(robot_name, pos)
                print(current_position)

            elif user_command.lower() == "left":
                pos = left(robot_name,pos)
                print(current_position)

        return(robot_name+": Shutting down..")
    except EOFError:
        pass

def robot_start():
    """This is the entry function, do not change"""
    robot_name = get_robot_name()
    print(get_command_input(robot_name))
    pass


if __name__ == "__main__":
    robot_start()