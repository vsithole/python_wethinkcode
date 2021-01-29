import world.text.world
import unittest


class MyTestCase(unittest.TestCase):
    def test_is_position_allowed(self):

        '''
        area limit vars
        min_y, max_y = -200, 200
        min_x, max_x = -100, 100
        '''
        val_x = 100
        val_y = 200
        
        output = world.text.world.is_position_allowed(val_x,val_y)
        self.assertEqual(output,True)

        val_x = 101
    
        output = world.text.world.is_position_allowed(val_x,val_y)
        self.assertEqual(output,False)

    def test_update_position(self):

        output = world.text.world.update_position(202)
        self.assertEqual(output,False)

        output = world.text.world.update_position(67)
        self.assertEqual(output,True)