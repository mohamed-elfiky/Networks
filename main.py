from helperfn import *
from generator import *
import sys

input_command = ''
while(input_command != 'exit'):
    input_command = input('Input file name->')
    if input_command == 'exit':
        break
    #read message
    lines = (line.rstrip() for line in open(input_command))
    lines = list(line for line in lines if line)
    message = lines[0]
    print(message)
    input_command = input('Alter?y/n->')
    if input_command == 'n':
        #convert string to binary
        data = (''.join(format(ord(x), 'b') for x in message)) 
        print ("Data binary: " + data) 
        key = "1001"
        encodedData = encode(data,key) 
        print("Decoded Data: " + encodedData) 

        verify(encodedData,key)

    else:
        input_command = input('Enter digit->')
        #convert string to binary
        data = (''.join(format(ord(x), 'b') for x in message)) 
        print ("Data binary: " + data) 
        key = "1001"
        encodedData = encode(data,key) 
        print("Decoded Data: " + encodedData) 
        alter(encodedData,int(input_command))
        verify(encodedData,key,1)

    






