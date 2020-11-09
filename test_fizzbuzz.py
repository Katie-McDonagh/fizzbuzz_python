import pytest

from fizzbuzz_python import fizz_buzz

# class TestFizzBuzz(unittest.TestCase):
#   # def test_list(self):
#   #   'returns 1 when given 1'
#   #   data = 1
#   #   result = fizzbuzz(data)
#   #   self.assertEqual(result, 1)

#   def test_list(self):
#         self.assertEqual(fizzbuzz(1), 1)

# if __name__ == '__main__':
#   unittest.main() 

# def fizzbuzz(x):
#   return x

def test_function():
    assert fizzbuzz(1) == 1