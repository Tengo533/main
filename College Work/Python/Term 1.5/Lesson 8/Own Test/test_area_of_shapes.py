import unittest
from area_of_shapes import AreaOfShapes

class TestArea(unittest.TestCase):

    def setUp(self):
        print("startUp")
        self.shape = AreaOfShapes(5,3,5,3)
        self.shape2 = AreaOfShapes(10,6,10,6)
    
    def tearDown(self):
        print("tearDown\n")


    def test_square_area(self):
        print("test_square_area")
        result = self.shape.square_area(), self.shape2.square_area()
        self.assertEqual(result[0], 25)
        self.assertEqual(result[1], 100)

    def test_circle_area(self):
        print("test_circle_area")
        result = self.shape.circle_area(), self.shape2.circle_area()
        self.assertEqual(result[0], 28.27431)
        self.assertEqual(result[1],  113.09724)

    def test_rectangle_area(self):
        print("test_rectangle_area")
        result = self.shape.rectangle_area(), self.shape2.rectangle_area()
        self.assertEqual(result[0], 15)
        self.assertEqual(result[1], 60)
    
    def test_triange_area(self):
        print("test_triange_area")
        result = self.shape.triangle_area(), self.shape2.triangle_area()
        self.assertEqual(result[0], 7.5)
        self.assertEqual(result[1], 30)


if __name__ == '__main__':
    unittest.main()