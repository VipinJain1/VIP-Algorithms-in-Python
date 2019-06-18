# compress of string, compression should be in place and  compressed string should be lesser than the original string.

def compress (st):
    stl = list (st)
    stlen = len(stl)
    count =1
    charcount =0

    if  (stlen  ==0 or stlen ==1):
        return stl

    if (len(set(stl)) == stlen):
        return stl

    for i in range(stlen-1):
        if stl[i] == stl[i+1]:
            count = count +1
            if  (i != (stlen -2)):
                continue
        if count >1:
            stl[charcount] = str(stl[i])
            charcount = charcount+1
            stl[charcount] = str(count)
            charcount = charcount+1
            count =1
            if (i == (stlen - 2)):
                return stl[0:charcount]
            i = i+1
        else:
            stl[charcount] = str(stl[i])
            charcount = charcount + 1
            i =i+1
            count =1
            return stl

print (compress(st = "aabd"))
print (compress(st = "a"))
print (compress(st = "aabbbccc"))
print (compress(st = "abc"))
print (compress(st = "aaaa"))
print (compress(st = "abbaaa"))
