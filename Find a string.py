#You are given a string . 
#Your task is to find out if the string  contains: alphanumeric characters,
#alphabetical characters, digits, lowercase and uppercase characters

def count_substring(string, sub_string):
    subslen  = len(sub_string)
    count =0 
    for i in range (len(string)):
        if string[i:subslen+i] == sub_string:
            count = count +1    
    return count 
