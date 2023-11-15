__author__='Nick Jeong'
'''
November 5, 2023
BaseConversion
converts a number from one base to another
'''

def isValidBase(num, base, baseTo):
    '''
    check if number and base inputted are valid
    :param num: inputted number by user
    :param base: base which corresponds with num
    :return: true or false
    '''
    if base>10 or base<2 or baseTo>10 or baseTo<2:
        print("ERROR!! One of the base value is not accepted!!")
        return False
    else:
        while num>0:
            if num%10>=base:
                print("ERROR!! Base and number inputted does not match!!")
                return False
            else:
                num//=10
    return True

def baseToDecimal(num, base):
    '''
    returns base 10 number of number inputted
    :param num: a number inputted
    :param base: base of the number
    :return: base 10 number of the number inputted
    '''
    n=0
    i=0
    while num>0:
        n+=(num%10)*(base**i)
        i+=1
        num//=10
    return n

def decimalToBase(num, base):
    '''
    converts the number of a specified base that is equal to a base 10 number parameter
    :param num: number inputted
    :param base: base num will convert to
    :return: num value after converted to different base
    '''
    i=0
    n=0
    while num>0:
        n+=(num%base)*(10**i)
        num//=base
        i+=1
    return n
def base1ToBase2(num, base, baseTo):
    '''
    converts number into another base and prints out the number converted
    :param num: number inputted
    :param base: base of the number inputted
    :param baseTo: base which user wants to convert the number into
    :return: NULL
    '''
    if isValidBase(num,base,baseTo):
        print(num, "base", base, "converted into base", baseTo, "is"
        ,decimalToBase(baseToDecimal(num,base),baseTo))

# Main program
num = int(input("Enter a number: "))
base = int(input("Enter the base of the number: "))
baseTo = int(input("Enter the base to convert the number to: "))
base1ToBase2(num,base,baseTo)