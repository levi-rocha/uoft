import sys
import copy

def readTwtFile(input):
    with open(input, 'rb') as twtfile:
        content = twtfile.readlines()
    tweets = []
    buf = []
    for line in content:
        if '< A = ' in line:
            tweets.append(copy.copy(buf))
            buf = []
        sp = line.split('\r')
        buf.append(sp[0])
    tweets.append(buf)
    tweets.pop(0)
    return tweets

def buildArffContentFromTweets(tweets, qty=-1):
    count0 = 0;
    count2 = 0;
    count4 = 0;
    content = []
    content.append('@relation tweets')
    content.append('')
    content.append('@attribute FPPcount numeric')
    content.append('@attribute SPPcount numeric')
    content.append('@attribute TPPcount numeric')
    content.append('@attribute CCcount numeric')
    content.append('@attribute PTVcount numeric')
    content.append('@attribute FTVcount numeric')
    content.append('@attribute Ccount numeric')
    content.append('@attribute CSCcount numeric')
    content.append('@attribute Dcount numeric')
    content.append('@attribute Pcount numeric')
    content.append('@attribute Ecount numeric')
    content.append('@attribute CNcount numeric')
    content.append('@attribute PNcount numeric')
    content.append('@attribute Acount numeric')
    content.append('@attribute WHWcount numeric')
    content.append('@attribute MSAcount numeric')
    content.append('@attribute UPPcount numeric')
    content.append('@attribute avgSlength numeric')
    content.append('@attribute avgTlength numeric')
    content.append('@attribute numsen numeric')
    content.append('@attribute class {0,2,4}')
    content.append('')
    content.append('@data')

    for tweet in tweets:
        if qty == -1:
            data = makeData(tweet)
            content.append(data)
        else:
            if count0 == qty and count2 == qty and count4 == qty:
                break
            cl = str(getClass(tweet))
            if cl == '0':
                if count0 < qty:
                    data = makeData(tweet)
                    content.append(data)
                    count0 += 1
            elif cl == '2':
                if count2 < qty:
                    data = makeData(tweet)
                    content.append(data)
                    count2 += 1
            elif cl == '4':
                if count4 < qty:
                    data = makeData(tweet)
                    content.append(data)
                    count4 += 1

    return content

def makeData(tweet):
        data = ''
        data += str(countFPP(tweet)) + ','
        data += str(countSPP(tweet)) + ','
        data += str(countTPP(tweet)) + ','
        data += str(countCC(tweet)) + ','
        data += str(countPTV(tweet)) + ','
        data += str(countFTV(tweet)) + ','
        data += str(countC(tweet)) + ','
        data += str(countCSC(tweet)) + ','
        data += str(countD(tweet)) + ','
        data += str(countP(tweet)) + ','
        data += str(countE(tweet)) + ','
        data += str(countCN(tweet)) + ','
        data += str(countPN(tweet)) + ','
        data += str(countA(tweet)) + ','
        data += str(countWHW(tweet)) + ','
        data += str(countMSA(tweet)) + ','
        data += str(countUPP(tweet)) + ','
        data += str(countAVGSL(tweet)) + ','
        data += str(countAVGTL(tweet)) + ','
        data += str(countNumSen(tweet)) + ','
        data += str(getClass(tweet))
        return data

def getClass(tweet):
    line = tweet[0]
    cl = line[6]
    return cl

def countFPP(tweet):
    count = 0
    words = ['i', 'me', 'my', 'mine', 'we', 'us', 'our', 'ours']
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            sp = token.split('/')
            word = sp[0].lower()
            if word in words:
                count += 1
    return count

def countSPP(tweet):
    count = 0
    words = ['you', 'your', 'yours', 'u', 'ur', 'urs']
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            sp = token.split('/')
            word = sp[0].lower()
            if word in words:
                count += 1
    return count

def countTPP(tweet):
    count = 0
    words = ['he', 'him', 'his', 'she', 'her', 'hers',
             'it', 'its', 'they', 'them', 'their', 'theirs']
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            sp = token.split('/')
            word = sp[0].lower()
            if word in words:
                count += 1
    return count

def countCC(tweet):
    count = 0
    tags = ['CC']
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            sp = token.split('/')
            tag = sp[1]
            if tag in tags:
                count += 1
    return count

def countPTV(tweet):
    count = 0
    tags = ['VBD']
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            sp = token.split('/')
            tag = sp[1]
            if tag in tags:
                count += 1
    return count

def countC(tweet):
    count = 0
    tags = [',']
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            sp = token.split('/')
            tag = sp[1]
            if tag in tags:
                count += 1
    return count

def countCSC(tweet):
    count = 0
    tags = [':']
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            sp = token.split('/')
            tag = sp[1]
            if tag in tags:
                count += 1
    return count

def countD(tweet):
    count = 0
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            if '-' in token:
                count += 1
    return count

def countP(tweet):
    count = 0
    tags = ['(', ')']
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            sp = token.split('/')
            tag = sp[1]
            if tag in tags:
                count += 1
    return count

def countE(tweet):
    count = 0
    words = ['..', '...', '....']
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            sp = token.split('/')
            word = sp[0].lower()
            if word in words:
                count += 1
    return count

def countFTV(tweet):
    count = 0
    special = 0
    words = ["'ll", 'will', 'gonna']
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            sc = 0
            sp = token.split('/')
            word = sp[0].lower()
            if word in words:
                count += 1
            if word == 'going':
                special = 1
                sc = 1
            if special == 1:
                if word == 'to':
                    special = 2
                    sc = 1
            if special == 2:
                if sp[1] == 'VB':
                    special = 0
                    count += 1
            if not sc:
                special = 0
    return count

def countCN(tweet):
    count = 0
    tags = ['NN', 'NNS']
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            sp = token.split('/')
            tag = sp[1]
            if tag in tags:
                count += 1
    return count

def countPN(tweet):
    count = 0
    tags = ['NNP', 'NNPS']
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            sp = token.split('/')
            tag = sp[1]
            if tag in tags:
                count += 1
    return count

def countA(tweet):
    count = 0
    tags = ['RB', 'RBR', 'RBS']
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            sp = token.split('/')
            tag = sp[1]
            if tag in tags:
                count += 1
    return count

def countWHW(tweet):
    count = 0
    tags = ['WDT', 'WP', 'WP$', 'WRB']
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            sp = token.split('/')
            tag = sp[1]
            if tag in tags:
                count += 1
    return count

def countMSA(tweet):
    count = 0
    words = ['smh', 'fwb', 'lmfao', 'lmao', 'tbh', 'rofl',
             'wtf', 'bff', 'wyd', 'lylc', 'brb', 'atm',
             'imao', 'sml', 'btw', 'bw', 'imho', 'fyi', 'u',
             'ppl', 'sob', 'ttyl', 'imo', 'ltr', 'thx', 'sol',
             'kk', 'omg', 'ttys', 'afn', 'bbs', 'cya', 'ez',
             'f2f', 'gtr', 'ic', 'jk', 'k', 'ly', 'ya', 'nm',
             'np', 'plz', 'ru', 'so', 'tc', 'tmi', 'ym', 'ur']
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            sp = token.split('/')
            word = sp[0].lower()
            if word in words:
                count += 1
    return count

def countUPP(tweet):
    count = 0
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            sp = token.split('/')
            if len(sp[0]) > 1:
                if sp[0] == sp[0].upper():
                    count += 1
    return count

def countAVGSL(tweet):
    num = 0
    sum = 0
    for i in range(1,len(tweet)):
        num += 1
        for token in tweet[i].split(' '):
            sum += 1
    if num > 0:
        avg = sum/num
    else:
        avg = 0
    return avg

def countAVGTL(tweet):
    num = 0
    sum = 0
    for i in range(1,len(tweet)):
        for token in tweet[i].split(' '):
            num += 1
            sp = token.split('/')
            sum += len(sp[0])
    if num > 0:
        avg = sum/num
    else:
        avg = 0
    return avg

def countNumSen(tweet):
    num = 0
    for i in range(1,len(tweet)):
        num += 1
    return num

def writeContentToFile(content,file):
    f = open(file, 'a')
    for line in content:
        f.write(line + '\n')

input = sys.argv[1]
tweets = readTwtFile(input)
content = []
if len(sys.argv)>3:
    content = buildArffContentFromTweets(tweets, int(sys.argv[3]))
else:
    content = buildArffContentFromTweets(tweets)
writeContentToFile(content, sys.argv[2])




