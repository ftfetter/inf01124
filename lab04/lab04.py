def initHashTable(size):
    hashTable = []
    for i in range(0, size):
        hashTable.append([])
    return hashTable

def createHash(string, divider):
    value = 0
    factor = 53 # Primeiro número primo maior ou igual ao número total de caracteres possíveis (52)
    for i in range(0, len(string)):
        value = (factor * value + ord(string[i])) % divider
    return value

def insertKey(hashTable, size, key):
    pos = createHash(key, size)
    hashTable[pos].append(key)

def getTotalQueriesToFindKey(hashTable, size, key):
    pos = createHash(key, size)
    totalKeys = len(hashTable[pos])
    totalQueries = 1

    i = 0
    while (i < len(hashTable[pos]) and key != hashTable[pos][i]):
        totalQueries += 1
        i += 1
    
    return totalQueries

fileKeys = "nomes_10000.txt"
fileQueries = "consultas.txt"

outputFiles = ["experimento503.txt", "experimento2503.txt", "experimento5003.txt", "experimento7507.txt"]
hashDividers = [503, 2503, 5003, 7507]

with open(fileKeys, "r") as input:
    keys = input.read()
    keys = keys.split('\n')

with open(fileQueries, "r") as input:
    keysToFetch = input.read()
    keysToFetch = keysToFetch.split('\n')

for i in range(0, len(hashDividers)):
    hashTable = initHashTable(hashDividers[i])
    for key in keys:
        insertKey(hashTable, hashDividers[i], key)

    output = open(outputFiles[i], "w+")
    maxQueries = 0
    greatestTotalQueriesValue = 0

    for key in keysToFetch:
        totalQueriesToFetch = getTotalQueriesToFindKey(hashTable, hashDividers[i], key)
        maxQueries += totalQueriesToFetch
        if totalQueriesToFetch > greatestTotalQueriesValue:
            greatestTotalQueriesValue = totalQueriesToFetch
        output.write("{} {}\n".format(key, totalQueriesToFetch))

    averageTotalQueriesValues = maxQueries / len(keysToFetch)
    
    output.write("MEDIA {}\n".format(averageTotalQueriesValues))
    output.write("MAXIMO {}".format(greatestTotalQueriesValue))
    
    output.close