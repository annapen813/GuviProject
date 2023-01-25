def getPrimeNumberSeries():
    inputValue = int(input('Please enter the rage of prime numbers to be printed: '))
    lst = []
    if(inputValue > 1):
        for x in range(2, inputValue):
            if(x == 2 or x == 3 or x == 5 or x == 7 or x == 11):
                lst.append(x)
            if(x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0 and x % 11 != 0):
                lst.append(x)
        print(lst)
    else:
        print('Given value is not valid')  

getPrimeNumberSeries()