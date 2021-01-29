import unittest
import robot
from unittest.mock import patch
from io import StringIO

class testing_robot(unittest.TestCase):
    @patch("sys.stdin", StringIO("off\noff\n"))
    def test_get_command_input_off(self):
        robot_name = "Vee"
        output = robot.get_command_input(robot_name)
        
        self.assertEqual(output,robot_name+": Shutting down..") 

    @patch("sys.stdin", StringIO("Vee\nVee\n"))
    def test_get_robot_name(self):
        name = robot.get_robot_name()
        self.assertEqual(name,"Vee")
        self.assertEqual(type(name), str)
    
    def test_get_help_message(self):
        message = "I can understand these commands:\nOFF  - Shut down robot\nHELP - provide information about commands\nForward - Moves your robot forward\nBack - Moves your robot back\nSprint to sprint forward"
        self.assertEqual(robot.get_help_message(), message)
    
    def test_user_input_if_contains_integers(self):
        s = "10"
        result = robot.check_int(s)
        self.assertEqual(result,True)
        v = "forward"
        result = robot.check_int(v)
        self.assertEqual(result,False)
    
    def test_moving_forward_x_and_y_variables(self):
        inp = 10
        y = 0
        x = 0
        pos = 0
        '''
        Testing y variable if it updates up position
        '''
        y,x,count = robot.forward(inp,y,x,pos)
        self.assertEqual(y,10)
        y,x,count = robot.forward(inp,y,x,pos)
        self.assertEqual(y,20)

    def test_moving_back_x_and_y_variables(self):
        inp = 10
        y = 0
        x = 0
        pos = 0
        '''
        Testing y variable if it updates up position
        '''
        y,x,count = robot.back(inp,y,x,pos)
        self.assertEqual(y,-10)
        y,x,count = robot.back(inp,y,x,pos)
        self.assertEqual(y,-20)

    def test_moving_back_x_and_y_different_position(self):
        inp = 10
        y = 0
        x = 0
        pos = 0
        '''
        Testing x variable if it updates right position
        '''
        pos = -90
        y,x,count = robot.back(inp,y,x,pos)
        self.assertEqual(x,10)
        '''
        Testing y variable if it updates down position
        '''
        pos = -180
        y = 0
        y,x,count = robot.back(inp,y,x,pos)
        self.assertEqual(y,10)
        '''
        Testing y variable if it updates left position
        '''
        pos = -270
        x = 0
        y,x,count = robot.back(inp,y,x,pos)
        self.assertEqual(x,-10)

    def test_moving_forward_x_and_y_different_position(self):
        inp = 10
        y = 0
        x = 0
        pos = 0
        '''
        Testing x variable if it updates right position
        '''
        pos = 90
        y,x,count = robot.forward(inp,y,x,pos)
        self.assertEqual(x,10)
        '''
        Testing y variable if it updates down position
        '''
        pos = 180
        y = 0
        y,x,count = robot.forward(inp,y,x,pos)
        self.assertEqual(y,-10)
        '''
        Testing y variable if it updates left position
        '''
        pos = 270
        x = 0
        y,x,count = robot.forward(inp,y,x,pos)
        self.assertEqual(x,-10)