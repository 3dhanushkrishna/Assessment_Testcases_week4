import unittest

import Operations

class testforarmstrong(unittest.TestCase):
    def setUp(self):
        self.a = 245

    def tearDown(self):
        self.a = 0

    def test_armstrong(self):
        c = Operations.armstrongnumber(self.a)
        self.assertFalse(c)

class testfordivisible(unittest.TestCase):

    def setUp(self):
        self.b = 75

    def tearDown(self):
        self.b = 0

    def test_divby5(self):
        c = Operations.divisibleby5(self.b)
        self.assertTrue(c)

class testforlargest(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 15
        self.c = 20

    def tearDown(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def test_largest(self):
        c = Operations.largest3(self.a,self.b,self.c)
        self.assertEqual(self.c,c)

class testforevenorodd(unittest.TestCase):

    def setUp(self):
        self.a = 16
        self.b = 11

    def tearDown(self):
        self.a = 0
        self.b = 0

    def test_evenorodd1(self):
        c = Operations.check_EvenorOdd(self.a)
        self.assertTrue(c)

    def test_evenorodd2(self):
        c = Operations.check_EvenorOdd(self.b)
        self.assertFalse(c)



if __name__ == "__main__":
    unittest.main()