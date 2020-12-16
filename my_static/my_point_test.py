import unittest
from my_point import Point

class testPoint(unittest.TestCase): # we need the TestCase class from unittest
    # set up the tests (this is run BEFORE each test)
    def setUp(self):
        self.point = Point(3, 5)
        self.pointDefault = Point() # default to 0, 0

    # declare our suite of tests
    def testMoveBy(self):
        """testing the moveby method"""
        self.point.move_by(5, 2)
        # make an assertion
        self.assertEqual(self.point.__str__(), 'Point is at x:8 y:7')

    def testMoveByAgain(self):
        """testing the moveby method again"""
        self.point.move_by(-5, -2)
        # make an assertion
        self.assertEqual(self.point.__str__(), 'Point is at x:-2 y:3')

    def testDefault(self):
        self.assertEqual(self.pointDefault.__str__(), 'Point is at x:0 y:0')

if __name__ == '__main__':
    # invoke the tests
    unittest.main()
