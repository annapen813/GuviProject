import math
class Helper:
    def __init__(self):
        pass

    def simpleEquation(self):
        a = int(input('please enter the first parameter value : '))
        b = int(input('please enter the second parameter value : '))
        c = int(input('please enter the third parameter value : '))
        if(a != None and b != None and c != None):
            return (a + b + c) * (a - b - c) * (a * b) + a**2 + b**2 + (a * b * c)**3
        else:
            return('Please enter the valid input')

    def simpleSquareRootEquation(self):
        x1 = int(input('please enter the X1 value : '))
        x2 = int(input('please enter the X2 value : '))
        y1 = int(input('please enter the Y1 value : '))
        y2 = int(input('please enter the Y2 value : '))
        if(x1 != None and x2 != None and y1 != None and y2 != None):
            try:
                return  math.sqrt(x1 - x2) ** 2 + math.sqrt(y1 - y2) ** 2
            except ValueError:
                print("x1 and y1 should be greater than x2 and y2")
            except:
                print("Something else went wrong")

    def checkPalindrome(self):
        strValue = input('Enter the string value to check : ')
        reverseValue = strValue.lower()[::-1]

        if(strValue.lower() == reverseValue):
            print('Yes, given string is a Palindrome.')
        else:
            print('No, given string is not a Palindrome.')

    

objHelper = Helper()
print(objHelper.simpleEquation())
print(objHelper.simpleSquareRootEquation())
objHelper.checkPalindrome()

