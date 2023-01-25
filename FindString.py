def extractString():
    strValue = input('Enter your phrase :')
    strFind = input('Enter the string value to find :')

    if strFind in strValue:
        txt = strValue
        x = txt[txt.find(strFind):txt.find(strFind) + len(strFind) + 1]
        print(x)
    else:
        print('Given string is not present in the phrase')


extractString()