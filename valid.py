# Function valid takes a string of 10 digits. The function returns True if the ID-numbers is a valid ID-number of 
# a person born between 1900 and 2099; False otherwise. To determine whether the ID-number is valid or not, you 
# have to use the checksum (english version) of the ID-number. Furthermore, the first six digits of the ID-number 
# must represent a valid date.
import datetime

def valid(digits):
    if len(digits) != 10:
        return False
    day = int(digits[:2])
    month = int(digits[2:4])
    year = int(digits[4:6])
    random = int(digits[6:8])
    # 1209972979
    # C = 11 - ((3xD1 + 2xD2 + 7xM1 + 6xM2 + 5xY1 + 4xY2 + 3xR1 + 2xR2) mod 11)
    checksum = 11 - (((3*int(digits[0:1])) + (2*int(digits[1:2])) + (7*int(digits[2:3])) + (6*int(digits[3:4])) + (5*int(digits[4:5])) + (4*int(digits[5:6])) + (3*int(digits[6:7])) + (2*int(digits[7:8]))) % 11)

    # if(datetime.datetime(year, month, day)):
    #     if(20 < random < 99):
    
    return checksum