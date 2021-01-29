print ('Module Turtle loaded')
import turtle
import random
from world import obstacles

blocker = False

robo = turtle.Turtle()
robo.color('red','black')
robo.pensize(3)
robo.speed(0)

# Drawing a canvas

robo.up()
robo.goto(-100, -200)
robo.down()
robo.goto(-100, 200)
robo.goto(100, 200)
robo.goto(100, -200)
robo.goto(-100, -200)

robo.color('black')
robo.up()
robo.home()
robo.setheading(90)
robo.right(90)


#Drawing obstacles in to the interface
def print_obstacles():
    
    robo.pensize(1)
    rand_list = obstacles.get_obstacles()
    robo.fillcolor('red')
    for z in rand_list:

        robo.begin_fill()
        robo.pu()
        robo.goto(z[0],z[1])
        robo.pd()
        robo.goto(z[0]+4,z[1])
        robo.goto(z[0]+4,z[1]+4)
        robo.goto(z[0],z[1]+4)
        robo.goto(z[0],z[1])
        robo.end_fill()

print_obstacles()

robo.color('black','red')
robo.up()
robo.home()
robo.setheading(90)

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    position_blocked = obstacles.is_position_blocked(new_x,new_y) 
    path_blocked =obstacles.is_path_blocked(position_x,position_y,new_x,new_y)
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y and not position_blocked and not path_blocked


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """
    global blocker
    blocker = False

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if obstacles.is_path_blocked(position_x,position_y,new_x,new_y) or obstacles.is_position_blocked(new_x,new_y):
        blocker = True
        return False
    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False

def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        robo.forward(steps)
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    elif blocker is True:
        return True, ''+robot_name+': Sorry, there is an obstacle in the way.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        robo.backward(steps)
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    elif blocker is True:
        return True, ''+robot_name+': Sorry, there is an obstacle in the way.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    robo.right(90)
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    robo.left(90)
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        robo.forward(1)
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        robo.forward(steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)