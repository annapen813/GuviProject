def writeSimpleTextOnFile():
    strValue = input('Enter the text which you want to write on the file: ')
    try:
        with open('helloWorld.txt', 'w') as f:
            f.write(strValue)
        
        print('Given text is added in the helloWorld.txt')
    except:
        print('Something went wrong.')


writeSimpleTextOnFile()