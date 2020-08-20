import main
import unittest

class TestPemdas(unittest.TestCase):

    def testSolveExpresssion(self):
        self.assertEqual(main.solveExpression("(22/2-2*5)^2+(4-6/6)^2"), "10.0")
        self.assertEqual(main.solveExpression("(1^4*2^2+3^3)-2^5/4"), "23.0")
        self.assertEqual(main.solveExpression("(3*5^2/15)-(5-2^2)"), "4.0")
        self.assertEqual(main.solveExpression("-1*((3-4*7)/5)-2*24/6"), "-3.0")
        self.assertEqual(main.solveExpression("-2(1*4-2/2)+(6+2-3)"), "-1.0")
        self.assertEqual(main.solveExpression("(17-6/2)+4*3"), "26.0")
        self.assertEqual(main.solveExpression("6*4/12+72/8-9"), "2.0")
        self.assertEqual(main.solveExpression("18/3-7+2*5"), "9.0")
        self.assertEqual(main.solveExpression("7-24/8*4+6"), "1.0")
