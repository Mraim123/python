import re


output_a = 52.0
output_b = "{:g}" .format(output_a)
print(output_a)
print(output_b)
print()
print()
a = "Hellow Python"
a.upper()
print(a.upper())
a.lower()
print(a.lower())
print()
print()
input_a = """
      안녕하세요
문자열의 함수를 알아봅시다
"""
print(input_a.strip())
print()
print()
#print(input_a.isspace())

b = "10 20 30 40 50".split(" ")
print(b)
c = "10, 20, 30, 40, 50".split(",")
print(c)
print()
print()

a= input ("> 1번쨰 숫자: ")
b= input ("> 2번쨰 숫자: ")
print("{} + {} = {}".format(a,b,int(a)+int(b)))