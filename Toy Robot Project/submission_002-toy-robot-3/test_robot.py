import unittest
import robot


class testing_robot(unittest.TestCase):
    '''
    def test_keep_command(self):
        command = "forward 10"
        history_list = robot.keep_command(command)
        command = "forward 5"
        history_list = robot.keep_command(command)
        self.assertEqual(history_list[1],'forward 5')'''
    
    def test_do_replay(self):
        robot_name = "Vusi"
        history_list = ['forward 10','forward 10','forward 10']
        arg = ''
        (booli, message) = robot.do_replay(history_list, robot_name, arg)
        self.assertEqual(booli,True)
        self.assertEqual(message,' > '+robot_name+' replayed 3 commands.')

    def test_do_replay_silent(self):
        robot_name = "Vusi"
        history_list = ['forward 10','forward 10']
        arg = 'silent'
        (booli, message) = robot.do_replay_silent(history_list, robot_name, arg)
        self.assertEqual(booli,True)
        self.assertEqual(message,' > '+robot_name+' replayed 2 commands silently.')

    def test_do_replay_reversed(self):
        robot_name = "Vusi"
        history_list = ['forward 10','forward 10','forward 5', 'forward 3']
        arg = 'reversed'
        (booli, message) = robot.do_reverse(history_list, robot_name, arg)
        self.assertEqual(booli,True)
        self.assertEqual(message,' > '+robot_name+' replayed 4 commands in reverse.')

    def test_do_replay_reversed_silent(self):
        robot_name = "Vusi"
        history_list = ['forward 10','forward 10']
        arg = 'reversed'
        arg2 = 'silent'
        (booli, message) = robot.do_reverse_silent(history_list, robot_name, arg, arg2)
        self.assertEqual(booli,True)
        self.assertEqual(message,' > '+robot_name+' replayed 2 commands in reverse silently.')

    def test_split_arg(self):
        arg = '4-2'
        num_1, num_2 = robot.split_arg(arg)
        self.assertEqual(num_1,'4')
        self.assertEqual(num_2,'2')

    def test_convert_to_int(self):
        num_1 = '2'
        num_2 = '3'
        
        num1 , num2 = robot.convert_to_int(num_1, num_2)
        self.assertEqual(type(num1), int)
        self.assertEqual(num2, 3)
