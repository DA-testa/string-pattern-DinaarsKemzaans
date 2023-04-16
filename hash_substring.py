#Dinārs Kemzāns 17. grupa 221RDB321

def read_input():
    typeOption = str(input())
    patternData = ""
    lookTextData = ""
    if("I" in typeOption):
        patternData = str(input()).rstrip()
        lookTextData = str(input()).rstrip()
    else:
        fileName = str(input())
        fileName = "tests/" + fileName
        with open(fileName, "r") as dataPlace:
            patternData = str(dataPlace.readline()).rstrip()
            lookTextData = str(dataPlace.readline()).rstrip()
    
    return (patternData, lookTextData)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(patternData, lookTextData):
    qData = 101
    bData = 256
    result = []
    patternHash = 0
    textHash = 0
    
    for m in range(int(len(patternData))):
        patternHash = (patternHash * bData + ord(patternData[m])) % qData
        textHash = (textHash * bData + ord(lookTextData[m])) % qData

    for u in range(int(len(lookTextData) - len(patternData) + 1)):
        if patternHash == textHash and lookTextData[u:u+len(patternData)] == patternData:
            result.append(u)
        if u < (len(lookTextData) - len(patternData)):
            textHash = ((textHash - ord(lookTextData[u]) * pow(bData, len(patternData) - 1, qData)) * bData + ord(lookTextData[u + len(patternData)])) % qData
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

