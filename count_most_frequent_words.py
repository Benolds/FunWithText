import operator
import string
from collections import defaultdict
from datetime import datetime

def getMostFrequentWords(inputString, numStringsToReturn):
    print "Returning the top " + str(numStringsToReturn) + " most frequent words in a length " + str(len(inputString)) + " string..."

    stripped = inputString.translate(string.maketrans("",""), string.punctuation)

    wordCounts = defaultdict(int)
    for word in stripped.split():
        wordCounts[word] += 1

    sortedWords = sorted(wordCounts.iteritems(), key=operator.itemgetter(1), reverse=True)

    return [x[0] for x in sortedWords[:(min(numStringsToReturn, len(sortedWords)-1))]]


#Use to test on a 100,000 word sample text:

fileHandle = open('lorem-ipsum-test.txt', 'r')
testString = fileHandle.read()
fileHandle.close()

startTime = datetime.now()
words = getMostFrequentWords(testString, 100)
print("Time Taken = " + str(datetime.now()-startTime))

print words

print "\n CHECKING FOR ERRORS... \n"
numErrors = 0
for word in words:
    if len(word) == 0:
        numErrors += 1
        print "\n ERROR \n"

if numErrors == 0:
    print "No word-length errors! :) \n"

