''' Input Format
The first line contains the first name, and the second line contains the last name.
Constraints
The length of the first and last name = .
Output Format
Print the output as mentioned above.
Sample Input 0
Ross
Taylor
Sample Output 0
Hello Ross Taylor! You just delved into python.
'''

def print_full_name(a, b):
    name = a + ' ' + b + '!'

    print ("Hello %s You just delved into python." % (name))
