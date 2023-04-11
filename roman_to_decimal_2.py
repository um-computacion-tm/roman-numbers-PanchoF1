import unittest

def romano_a_decimal(romano):
    

    lista= {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    decimal=0

    for i in range(len(romano)):
        if i > 0 and lista[romano[i]]>lista[romano[i-1]]:
            decimal += lista[romano[i]] - 2* lista[romano[i-1]]
        else:
            decimal += lista[romano[i]]

    return decimal


class TestDecimalToRoman(unittest.TestCase):

    
    def test_2(self):
        roman_number = romano_a_decimal('II')
        self.assertEqual(roman_number, 2)

        
    def test_12(self):
        roman_number = romano_a_decimal('XII')
        self.assertEqual(roman_number, 12)

        
    def test_18(self):
        roman_number = romano_a_decimal('XVIII')
        self.assertEqual(roman_number, 18)

        
    def test_50(self):
        roman_number = romano_a_decimal('L')
        self.assertEqual(roman_number, 50)

        
    def test_57(self):
        roman_number = romano_a_decimal('LVII')
        self.assertEqual(roman_number, 57)

        
    def test_82(self):
        roman_number = romano_a_decimal('LXXXII')
        self.assertEqual(roman_number, 82)

        
    def test_44(self):
        roman_number = romano_a_decimal('XLIV')
        self.assertEqual(roman_number, 44)

        
    def test_75(self):
        roman_number = romano_a_decimal('LXXV')
        self.assertEqual(roman_number, 75)

        
    def test_249(self):
        roman_number = romano_a_decimal('CCXLIX')
        self.assertEqual(roman_number, 249)

        
    def test_283(self):
        roman_number = romano_a_decimal('CCLXXXIII')
        self.assertEqual(roman_number, 283)

        
    def test_366(self):
        roman_number = romano_a_decimal('CCCLXVI')
        self.assertEqual(roman_number, 366)

        
    def test_500(self):
        roman_number = romano_a_decimal('D')
        self.assertEqual(roman_number, 500)

        
    def test_1366(self):
        roman_number = romano_a_decimal('MCCCLXVI')
        self.assertEqual(roman_number, 1366)
    
   


if __name__ == '__main__':
    unittest.main() 