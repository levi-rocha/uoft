import NLPlib
import csv
import sys

def replaceCharCodes(str):
    new = str.replace('&#38','&')
    new = new.replace('&#32',' ')
    new = new.replace('&#33','!')
    new = new.replace('&#34','"')
    new = new.replace('&#35','#')
    new = new.replace('&#36','$')
    new = new.replace('&#37','%')
    new = new.replace('&#39',"'")
    new = new.replace('&#40','(')
    new = new.replace('&#41',')')
    new = new.replace('&#42','*')
    new = new.replace('&#43','+')
    new = new.replace('&#44',',')
    new = new.replace('&#45','-')
    new = new.replace('&#46','.')
    new = new.replace('&#47','/')
    new = new.replace('&#48','0')
    new = new.replace('&#49','1')
    new = new.replace('&#50','2')
    new = new.replace('&#51','3')
    new = new.replace('&#52','4')
    new = new.replace('&#53','5')
    new = new.replace('&#54','6')
    new = new.replace('&#55','7')
    new = new.replace('&#56','8')
    new = new.replace('&#57','9')
    new = new.replace('&#58',':')
    new = new.replace('&#59',';')
    new = new.replace('&#60','<')
    new = new.replace('&#61','=')
    new = new.replace('&#62','>')
    new = new.replace('&#63','?')
    new = new.replace('&#64','@')
    new = new.replace('&#91','[')
    new = new.replace('&#92',"\\")
    new = new.replace('&#93',']')
    new = new.replace('&#94','^')
    new = new.replace('&#95','_')
    new = new.replace('&#96','`')
    new = new.replace('&#123','{')
    new = new.replace('&#124','|')
    new = new.replace('&#125','}')
    new = new.replace('&#126','~')
    return new.replace('&#127','DEL')

def removeURL(words):
    for word in words:
        if "http" in word or "www" in word:
            words.remove(word)
    return words

def removeAtAndHashTags(str):
    noat = str.replace('@','')
    noht = noat.replace('#','')
    return noht

def checkIfEndOfSentenceAndSeparatePunctuation(str):
    if '.' in str:
        if str.count('.') > 1:
            sp = str.split('.')
            if sp.count('') > 1:
                #elipses
                new = str.replace('.',' .',1)
                lis = new.rsplit('.', 1)
                new = '****EOSP'.join(lis)
                return new
            else:
                #abbrev
                return str
        else:
            if len(str) < 3:
                #abbrev
                return str
            else:
                if len(str) == 3 and str[0].isupper():
                    #abbrev
                    return str
                else:
                    return str.replace('.',' ****EOSP')
    if '?' in str:
        sp = str.split('?')
        if sp.count('')>1:
            new = str.replace('?',' ?',1)
            lis = new.rsplit('?', 1)
            new = '****EOSQ'.join(lis)
            return new
        return str.replace('?',' ****EOSQ')
    if '!' in str:
        sp = str.split('!')
        if sp.count('')>1:
            new = str.replace('!',' !',1)
            lis = new.rsplit('!', 1)
            new = '****EOSE'.join(lis)
            return new
        return str.replace('!',' ****EOSE')
    return str

def separateCliticsAndOtherPunctuation(str):
    new = str.replace("'", " ' ")
    new = new.replace(",", " , ")
    new = new.replace(":", " : ")
    new = new.replace("(", " ( ")
    new = new.replace(")", " ) ")
    new = new.replace('"', ' " ')
    return new.strip()

def separateSentences(text):
    sentences = text.split("****EOSP")
    if "" in sentences:
        sentences.remove("")
    for i in range(0,len(sentences)-1):
        sentences[i] += "."
    stcs2 = []
    for sentence in sentences:
        if "****EOSQ" in sentence:
            spl = sentence.split("****EOSQ")
            if "" in spl:
                spl.remove("")
            for i in range(0,len(spl)-1):
                spl[i] += "?"
            for item in spl:
                stcs2.append(item)
        else:
            stcs2.append(sentence)
    stcs3 = []
    for sentence in stcs2:
        if "****EOSE" in sentence:
            spl = sentence.split("****EOSE")
            if "" in spl:
                spl.remove("")
            for i in range(0,len(spl)-1):
                spl[i] += "!"
            for item in spl:
                stcs3.append(item)
        else:
            stcs3.append(sentence)
    stripped = []
    for sentence in stcs3:
        sentence = sentence.strip()
        stripped.append(sentence)
    return stripped

filename = sys.argv[1]
outputfile = sys.argv[2]

tweets = []
with open(filename, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        tweet = []
        for item in row:
            tweet.append(item)
        tweets.append(tweet)
tagger = NLPlib.NLPlib()
parsed = []
for tweet in tweets:
    text = tweet[5]
    words = text.split()
    words = removeURL(words)
    nwords = []
    for word in words:
        word = replaceCharCodes(word)
        word = removeAtAndHashTags(word)
        word = checkIfEndOfSentenceAndSeparatePunctuation(word)
        word = separateCliticsAndOtherPunctuation(word)
        nwords.append(word)
    text = " ".join(nwords)
    sentences = separateSentences(text)
    header = "< A = " + tweet[0] + " >"
    pt = header + "\n"
    for stc in sentences:
        words = stc.split(" ")
        tags = tagger.tag(words)
        tagged = []
        for i in range(0,len(words)):
            tagged.append(words[i]+"/"+tags[i])
        stc = " ".join(tagged)
        pt += (stc + "\n")
    parsed.append(pt)

text = ""
for tweet in parsed:
    text += tweet

if (len(sys.argv)>3 and sys.argv[3] == 'overwrite'):
    f = open(outputfile, 'w')
else:
    f = open(outputfile, 'a')

f.write(text)

# elipses: end of sentence?

# html tags?

# html to ascii codes?






