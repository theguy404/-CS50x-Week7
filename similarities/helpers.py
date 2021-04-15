from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    lineA = a.split("\n")
    lineB = b.split("\n")

    return compare(lineA, lineB)


def sentences(a, b):
    """Return sentences in both a and b"""
    sentA = sent_tokenize(a)
    sentB = sent_tokenize(b)

    return compare(sentA, sentB)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    subsA = split(a, n)
    subsB = split(b, n)
    
    return compare(subsA, subsB)

def compare(a, b):
    result = []
    
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                found = False
                for n in range(len(result)):
                    if a[i] == result[n]:
                        found = True
                if not found:
                    result.append(a[i])
    
    return result
    
def split(a, n):
    result = []
    for i in range(len(a) - n):
        result.append(a[i:i+n+1])
        
    return result