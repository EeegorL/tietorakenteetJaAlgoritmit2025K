import math;

def check_number(number):
    if(number[0] != "0" or len(number) != 9):
        return False;
    
    multArr = "37137137";
    numbersWithoutLast = number[:-1];

    numSum = 0;
    i = 0;
    for x in numbersWithoutLast:
        numSum += int(x) * int(multArr[i]);
        i+=1;
    
    distToTen = (math.ceil(numSum / 10) * 10) - numSum;
    
    return int(number[8]) == int(distToTen);

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False
