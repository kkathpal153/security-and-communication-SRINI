

import binascii
#### Script created by kunal Kathpal B00765934 ####

#### from string i mean the whole text that was preent in the file i.e .TXT file### 
##### function to convert the ascii value of the character to binary 8 bit srting###
def chartobinary( i):
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


### transition jump in NRZ###

def nrz (binary_string):
    count=0
    transition_count = 0
    for i in range(1,len(binary_string)):
        if(binary_string[i] == "1"):
            if(binary_string[i-1] == "0"):
                #print "value of i is" + str(i) + " increase count when current bit " + str(binary_string[i]) + " increasing count when the previous bit is" + str(binary_string[i-1])
                transition_count= transition_count + 1
        if(binary_string[i] == "0"):
            if(binary_string[i-1] == "1"):
                #print "value of i is" + str(i) + " increase count when current bit " + str(binary_string[i]) + " increasing count when the previous bit is" + str(binary_string[i-1])
                transition_count = transition_count + 1
    if(binary_string[len(binary_string)-1] == "1"):
        return transition_count + 1
    return transition_count



###calculating the transition count during menchester encoding ###
def menchester (binary_string):
    transition_count = 0
    for i in range(0, len(binary_string)):

        if(binary_string[i] == binary_string[i-1] and i > 0):
            transition_count = transition_count + 1
        transition_count= transition_count + 1
    return transition_count
        
                   
### reading the file contaning random jibbersh data ###
### convert every element of that jibbersh file to ascii values then into binary form###
### after converting the file to binary form bit stuffing is done from the above function####




l="101101"

def nrz_wave(binary_string1):
    k = ("¯ ¯","_ _")
    for i in binary_string1:
        if(i=="1"):
            print k[0],
        else:
            print k[1],
    #if(binary_string1[len(binary_string1)-1] == "1"):
        #print k[1],
    print

def menchester_wave(binary_string):
    k=("_","¯")
    
    #if(binary_string[0] == "0"):
       # print k[0],
    #else:
        #print k[1],
    print "i am assuming that the signal is low at default"
    for i in range(1,len(binary_string)):
        if(i=="1"):
            print k[0] + k[1],
        else:
            print k[1] + k[0],
    print

                   
#### PART A ####
###object for openning the file###

with open('queston2.txt', 'r') as myfile:   
    data=myfile.read()

binary_string1 =""
print "PART A"
print "reading the file"
print "  the file contains the data."
print data
print
print
# the loop will convert the file containing text to a long string of ascii codes

##### PART B ####
print "PART B"
for i in data:
    jj= chartobinary(i)
    binary_string1 = binary_string1 + jj
print "Printing the binary code file "
print binary_string1

print
print


### PART C ####
#calling the  nrz transition function
print "PART C"
print "number of transition in nrz is",
print nrz(binary_string1)
print
print
#calling the menchester transition count function
print "number of transition in menchester ",
print menchester(binary_string1)
print
print

##### PART D #####
#nrz_binary_string = asciitobinary(binary_string2)
print "PART D"
binary_string2= ""

#print "the nrz waveform is "
print
print 
print" the NRZ wave form for string i.e my intials 'K.K'"

string2 = "K.K"
#converting my initials to the binarycode!!
for i in string2 :
    jj= chartobinary(i)
    binary_string2 = binary_string2 + jj
bitcode=(binary_string2)

print "prititng the nrz wave"
nrz_wave(bitcode)



print " printitng the Menchester wave "
menchester_wave(bitcode)
