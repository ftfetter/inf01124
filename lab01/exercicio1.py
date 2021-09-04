SHELL = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]
KNUTH = [1,4,13,40,121,364,1093,3280,9841,29524,88573,265720,797161,2391484]
CIURA = [1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711]

def lineToList(line):
    return list(map(lambda x: int(x), line.split()))

def shellSort(originalArray, size, sequence, output):
    newArray = originalArray[:]
    steps = defineSteps(size, sequence)
    for step in range(steps, 0, -1):
        h = sequence[step - 1]
        for f in range(0, h):
            sort(newArray, size, h, f)
        
        output.write(str(newArray)[1:-1] + ' INCR=' + str(h) + '\n')

def defineSteps(size, sequence):
    steps = 0
    while size > sequence[steps]:
        steps = steps + 1
    return steps

def sort(array, size, h, f):
    for index in range(f + h, size, h):
        currentValue = array[index]
        currentPosition = index

        while currentPosition - h >= 0 and array[currentPosition - h] > currentValue:
            array[currentPosition] = array[currentPosition - h]
            currentPosition = currentPosition - h
        
        array[currentPosition] = currentValue

inputFile = 'entrada1.txt'
outputFile = 'saida1.txt'

output = open(outputFile, 'w+')

with open(inputFile, 'r') as input:
    lines = input.readlines()
    for line in lines:
        array = lineToList(line)
        size = array.pop(0)

        output.write(str(array)[1:-1] + ' SEQ=SHELL' + '\n')
        shellSort(array, size, SHELL, output)
        output.write(str(array)[1:-1] + ' SEQ=KNUTH' + '\n')
        shellSort(array, size, KNUTH, output)
        output.write(str(array)[1:-1] + ' SEQ=CIURA' + '\n')
        shellSort(array, size, CIURA, output)

output.close()
