from main import *

## Feel free to add your own tests here.
def test_multiply():
  result = subquadratic_multiply(BinaryNumber(2), BinaryNumber(2))
  expected_result = BinaryNumber(2 * 2)
  assert result.decimal_val == expected_result.decimal_val