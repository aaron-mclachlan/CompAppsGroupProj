import unittest
import Windows.Calculator as calc
import Windows.Simulator as sim
from Windows.Simulator import simulation_page

#All other errors, ie blank inputs & invalid entries are handled within the entry boxes and cannot be tested with a test.py

class testcalculations(unittest.TestCase): #checking calculator window
    def test_calc_q(self):#solving for Q
        result = calc.solve_for_Q(1,2,3,4)#should = 0.5
        self.assertEqual(result, 1.5)

    def test_calc_k(self): #Checking for div/0 handling
        result = calc.solve_for_k(1,2,3,0)
        self.assertEqual(result,2/3 )

    def test_calc_L(self):#Checking for handling of -ve numbers
        result = calc.solve_for_L(1,-2,3,4)
        self.assertEqual(result, -24)

    def test_calc_T1(self): 
        result = calc.solve_for_T1(1,2,3,4,5,)
        self.assertEqual(result,1.2 )
               
    def test_calc_T2(self):
        result = calc.solve_for_T2(1,2,3,4,5,6)
        self.assertEqual(result,0.8 )

    def test_calc_DT(self):
        result = calc.solve_for_delta_T(1,2,3,4,5)
        self.assertEqual(result, 5/24)
               
    def test_calc_W(self):
        result = calc.solve_for_width(1,2,3,4,5)
        self.assertEqual(result,5/24)

    def test_calc_H(self):
        result = calc.solve_for_height(1,2,3,4,5)
        self.assertEqual(result, 5/24)

if __name__ == '__main__':
    unittest.main()