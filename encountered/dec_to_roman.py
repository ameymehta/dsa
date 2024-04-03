# I = 1, V = 5, X = 10, L = 50, C = 100, D = 500 M = 1000
# XVI
# XIV
# 166 => 100 + 60 + 6 => 
# 40 = XL
# 50 = L
# 60 = LX

# conver_digit(number, I, V, X)
# conver_digit(number, X, L, C)
# conver_digit(number, C, D, M)
def conver_digit(number, ones, fives, tens):
  if number < 4:
    return ones * number
  elif number == 4:
    return ones + fives
  elif number == 9:
    return ones + tens
  else:
    return fives + (ones * (number-5))

def convert_dec_to_roman_number(num):
  result = ""

  if num < 1 and num > 999:
    return result

  hundreds = num//100
  tens = (num%100)//10
  decimals = (num%100)%10
  result += conver_digit(hundreds, 'C', 'D', 'M')
  result += conver_digit(tens, 'X', 'L', 'C')
  result += conver_digit(decimals, 'I', 'V', 'X')

  return result

def main():
  print('start')
  print(convert_dec_to_roman_number(99) == "XCIX")
  print(convert_dec_to_roman_number(899) == "DCCCXCIX")
  print(convert_dec_to_roman_number(3) == "III")
  print(convert_dec_to_roman_number(55) == "LV")
  print(convert_dec_to_roman_number(44) == "XLIV")
  print(convert_dec_to_roman_number(0) == "")

main()
