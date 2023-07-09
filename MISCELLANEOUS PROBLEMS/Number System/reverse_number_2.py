# Program to reverse a number


def reverseNumber(num: int) -> int:
  K = [int(i) i for i in str(num)]
  reverse_K = K[::-1]
  str_num = ""
  for i in reverse_K:
    str_num += i
  return int(str_num)


