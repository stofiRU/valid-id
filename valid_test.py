# tests for valid.py
from valid import valid

print("T:", valid('1209972979'))
print("F:", valid('1209972977'))
print("F:", valid('1209972975'))


# test for c for 1209972979:
# print("(1) 3xD1: 1*3: 3:", (3*int(digits[0:1])))
# print("(2) 2xD2: 2*2: 4:", (2*int(digits[1:2])))
# print("(0) 7xM1: 7*0: 0:", (7*int(digits[2:3])))
# print("(9) 6xM2: 6*9: 54:", (6*int(digits[3:4])))
# print("(9) 5xY1: 5*9: 45:", (5*int(digits[4:5])))
# print("(7) 4xY2: 4*7: 28:", (4*int(digits[5:6])))
# print("(2) 3xR1: 3*2: 6:", (2*int(digits[7:8])))
# print("(9) 2xR2: 2*9: 18:", (2*int(digits[8:9])))
# print("1",(int(digits[0:1])))
# print("2",(int(digits[1:2])))
# print("0",(int(digits[2:3])))
# print("9",(int(digits[3:4])))
# print("9",(int(digits[4:5])))
# print("7",(int(digits[5:6])))
# print("2",(int(digits[6:7])))
# print("9",(int(digits[7:8])))