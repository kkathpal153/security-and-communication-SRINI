


#its the helper function to crc_division as its used to the xor operation at every iteration

def xorc(k,j):
    x=""
    zero_string= ""
    #making a zero string
    for i in range(0,len(j)):
        zero_string= zero_string + "0"
    if(k[0] == "0"):
        d=""
        for i in range(0,len(k)):
            d=d+"0"
        if(k==j):
            return zero_string
        else:   
            for p in range(0,len(k)):
                if(k[p] == d[p]):
                    x=x+"0"
                else:
                    x=x+"1"
            #print " the returning value is " + x
            return x
    else:
        if(k==j):
            return zero_string
        else:
            for p in range(0,len(k)):
                if(k[p] == j[p]):
                    x=x+"0"
                else:
                    x=x+"1"
            #print " the returning value is " + x
            return x



#THIS function is for division of the bit strings i. the g(x) and the m(x)
def crc_division(mx, gx):
    l= len(gx)
    k= mx [0:len(gx)]
    dd=mx[0:len(gx)-1]
    for i in range(0,len(mx)-len(gx)+1):
        if(i==0):
            None 
        else:
            k= k[1:len(gx)] + mx[i+len(gx)-1]
        #print "the k on the starting is " + k
        #print " the bits going for xor are " + k + " and " + gx 
        f=xorc(k,gx)
        #print " on the iteration " + str(i) + "the value of f is " + f
        dd=""
        k=""
        for a in range(0,len(gx)):
            k = k+ f[a]
        #print "k going to next iteration is " + k
        #print
        #print
        #print
    return f[1:len(gx)]


m="1101011"


gx="1101" 
dd=""
for i in range (0,len(gx)-1):
    dd= dd + "0"
    
mx = m + dd
print "PART A"
print " the divident ( message bits + no of zero bits in highest power of gx) is " + mx
print "the polynomial g(x) used is " + gx

remainder = crc_division(mx,gx)

print " the remainder is " + remainder
print "but we want to enter the last 3 significant bits "
mxx= m + remainder[0:len(remainder)-1]

print "the message to be transmitted is " + mxx



mxxx= "1101011010"
print
print 
print "Let the message received by the user is" + mxxx
print "To check if the message received is correct o r not we will divide it by " + gx + "  i.e the polynomial"
remainder2 = crc_division(mxxx,gx)



print "PART B"
#making a string of length len(gx) so as to compare the remainder 
check_string=""

for i in range(0, len(gx)-1):
    check_string=check_string + "0"

#now i will compare the strings
if(remainder2== check_string):
    print "the message received is correct because the reaminder of crc divison is  " + remainder2 
else:
    print "the message received is incorrect becasue the remainder of the crc division is " + remainder2


