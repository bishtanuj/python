# Program to reverse a number

def reverseNumber(num: int) -> int:
  reverse = 0
  while num:
    remainder = num % 10
    reverse = reverse * 10 + remainder
    num = num // 10
  return reverse
  
