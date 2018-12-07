# Function valid takes a string of 10 id. The function returns True if the ID-numbers is a valid ID-number of 
# a person born between 1900 and 2099; False otherwise. To determine whether the ID-number is valid or not, you 
# have to use the checksum (english version) of the ID-number. Furthermore, the first six id of the ID-number 
# must represent a valid date.
import datetime

def valid(id):
    if len(id) != 10: return False

    d = int(id[:2])
    m = int(id[2:4])
    if int(id[9]) == 0: century = 100 
    else: century = 0
    y = 1900 + int(id[4:6]) + century

    try:
        datetime.date(y,m,d)
    except ValueError:
        return False

    birthday = datetime.date(y,m,d)
    lowerBound = datetime.date(1899,12,31)
    upperBound = datetime.date(2100,1,1)

    random = int(id[6:8])
    # c = 11 - ((3xD1 + 2xD2 + 7xM1 + 6xM2 + 5xY1 + 4xY2 + 3xR1 + 2xR2) mod 11)
    c = 11 - (((3*int(id[0:1])) + (2*int(id[1:2])) + (7*int(id[2:3])) + (6*int(id[3:4])) + (5*int(id[4:5])) + (4*int(id[5:6])) + (3*int(id[6:7])) + (2*int(id[7:8]))) % 11)
    if ((lowerBound < birthday < upperBound) and (c == int(id[8])) and (19 < random < 100) and ((int(id[9]) == 9) or (int(id[9]) == 0))):
        return True
    else:
        return False