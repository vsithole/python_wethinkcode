import unittest

import world.obstacles


class Obstacles_Case(unittest.TestCase):
    # def test_is_position_blocked(self):

    
    # def test_is_path_blocked(self):

    def test_get_obstacles(self):
        obst_list = world.obstacles.get_obstacles()
        self.assertEquals(type(obst_list),list)