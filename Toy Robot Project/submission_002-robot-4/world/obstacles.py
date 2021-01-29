import random

#rand_obstacles = [] 

def is_position_blocked(x,y):
    for v in rand_obstacles:
        if x in range(v[0],v[0]+5) and y in range(v[1],v[1]+5):
            return True
    return False 


def is_path_blocked(x1,y1, x2, y2):
    for a in rand_obstacles:
        if (x1 == x2) and (a[0] < x1 < a[0] + 4) and (y1 < a[1] < y2) or ((a[0] + 4 > x1 > a[0]) and y1 > a[1] > y2):
            return True
        if (y1 == y2) and (a[1] < y1 < a[1] + 4) and (x1 < a[0] < x2) or ((a[1] + 4 > y1 > a[1]) and x1 > a[0] > x2):
            return True
    return False


def get_obstacles():
    global rand_obstacles
    rand_obstacles = []
    num = random.randint(1,10)
    for i in range (num):
        x1 = random.randint(-100,100)
        y1 = random.randint(-200,200)

        rand_obstacles.append((x1,y1))
    return rand_obstacles

def reset_obst():
    global rand_obstacles
    rand_obstacles = []