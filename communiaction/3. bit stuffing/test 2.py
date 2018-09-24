


def binay_to_bitstuff( binary_string ):
    j=""
    jump = 1
    for i in range(0,len(binary_string),jump):
        s= binary_string[i:i+5]
        print "copie string" + s
        if( s == "11111"):
            j= j + binary_string[i: i+5] + "0"
            
            print j + "on iteration i" + str(i)
            
            print "for running"
            i = i+5
            jump = 5
        else:
            j=j+binary_string[i]
            print str(jump)
            jump = 1
    return j


def binary_to_bitstuff( binary_string ):
    j=""
    i=0
    k=""
    while i< len(binary_string):
        s = binary_string[i:i+5]
        print " the ith value is" + str(i)
        print "copied string is " + s
        if( s == "11111"):
            k = k +  binary_string[i: i+5] + "0"
            print " the element k is " + k
            i=i+5
        else:
            k=k+binary_string[i]
            print " k on else is" + k
            i=i+1
    return k

            
        

s="11111011111"
k="1011111001111"


f= binary_to_bitstuff(k)
print f
