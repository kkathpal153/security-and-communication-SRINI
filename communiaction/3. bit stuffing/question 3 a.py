

import binascii
#### Script created by kunal Kathpal B00765934 ####

#### from string i mean the whole text that was preent in the file i.e .TXT file### 
##### function to convert the ascii value of the character to binary 8 bit srting###
def asciitobinary( i):
    #print " the character coming is " + i
    s=(bin(ord(i))) #its a binary tring with soemthing like 0b0000000
    #print "its binary conversion is" + s
    s= s[2:len(s)]#converted the binary string to a 8 bit binart string
    if(len(s)!= 8):
        k= 8 -len(s)
        for i in range (0,k):
            s= "0" + s
    #print s
    return s

### to convert the binary string to bit stuffed binary string###
### will return a string with bit stuffing ###

def binary_to_bitstuff( binary_string ):
    j=""
    i=0
    k=""
    while i< len(binary_string):
        s = binary_string[i:i+5]
        if( s == "11111"):
            k = k +  binary_string[i: i+5] + "0"
            i=i+5
        else:
            k=k+binary_string[i]
            i=i+1
    return k


### THIS function is just as opposite to binary to bitstuff ###
### it takes the binary stuffed string and outputs the binary string ###

def bitstuff_to_binary( binary_string ):
    j=""
    i=0
    k=""
    while i< len(binary_string):
        s = binary_string[i:i+5]
        if( s == "11111"):
            k = k +  binary_string[i: i+5] 
            i=i+6
        else:
            k=k+binary_string[i]
            i=i+1
    return k



### a funtion to convert the binary sting to the original text ####
def binary_to_original(bit_stuffed):
    final_string=""
    for i in range(0,len(bit_stuffed),8):
        character = bit_stuffed[i:i+8]
        ascii = int ( character , 2)
        #print str(ascii) + "  " +character + "  " + chr(ascii)
        final_string = final_string + chr(ascii)
    return final_string
    

#### the main segment of the script ###

### reading the file contaning random jibbersh data ###
### convert every element of that jibbersh file to ascii values then into binary form###
### after converting the file to binary form bit stuffing is done from the above function####



###object for openning the file###

with open('question3.txt', 'r') as myfile:   
    data=myfile.read()

binary_string1 =""

for i in data:
    jj= asciitobinary(i)
    binary_string1 = binary_string1 + jj


### we will send J to function binary to bitstuff ###
    
final_bitstuffed_string= binary_to_bitstuff(binary_string1)

### the string variable ""final_bitstuffed_string""" contains the bitstuddef string



print final_bitstuffed_string
##### PART A #####
print " now writing the buffed string to text file "
buff = open("buff.txt", "w")

buff.write("Purchase Amount: " 'TotalAmount')

buff.close()
print "the file is created " + "buff.txt" 
### part b of the question ###
### converting the previously obtained bitstuffed string to binary sttring and then to original paragraph###
binary_string2 = bitstuff_to_binary(final_bitstuffed_string)


    

original_text = binary_to_original(binary_string2)

print original_text
buffr = open("original.txt", "w")

buffr.write("Purchase Amount: " 'TotalAmount')

buff.close()
print "the file is created " + "buff.txt" 
