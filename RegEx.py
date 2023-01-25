import re

def getOnlyNumbers():
    strValue = input('Enter your string phrase : ')

    pattern = '\d'
    result = re.findall(pattern, strValue)
    return print(result)


getOnlyNumbers()
