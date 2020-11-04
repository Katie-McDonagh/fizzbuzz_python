import unittest

from fizz_buzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
  def test_list(self):
    'returns 1 when given one'
    data = 1
    result = fizz_buzz(data)
    self.assertEqual(result, 1)

if __name__ == '__main__':
  unittest.main() 