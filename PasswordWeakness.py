
def NumCharLower(Password):
    count = 0
    for i in Password :
        if i.islower():
            count = count +1
    return count

def NumCharUpper(Password):
    count = 0
    for i in Password :
        if i.isupper():
            count = count +1
    return count

def NumCharNonalpaha(Password):
    count = 0
    for i in Password :
        if (i.isalpha()) ==False:
            count = count +1
    return count

def LongMaj(Password):
    for i in range(len(Password)):
        count = 0
        while i < len(Password) and Password[i].isupper():
            count = count+1
            i=i+1

        if (max<count):
            max = count
    return max

def LongMin(Password):
    for i in range(len(Password)):
        count = 0
        while i < len(Password) and Password[i].islower():
            count = count+1
            i=i+1

        if (max<count):
            max = count
    return max
def score(Password):
    b = len(Password) + (len(Password) - NumCharUpper(Password))*2 + (len(Password) - NumCharLower(Password))*2+ NumCharNonalpaha(Password)*5
    m = LongMaj(Password) * 2 + LongMin(Password)*2
    s = b+ m
    return score
