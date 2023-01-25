def getNaturalNumberSeries():
    inputValue = int(input('Please enter the range of natural numbers  to be printed: '))
    if(inputValue > 0):
        naturalNumber = list(x for x in range(1, inputValue + 1))
        print(naturalNumber)
    else:
        print('Given value is not valid')

getNaturalNumberSeries()