
def xo ( x , y):
    if( x == y):
        return 0
    else:
        return 1
    
def xorf( tap , seed ):
    x=seed[tap[0]]
    #print "for the xor the seed is " + str(seed) + " value of x is " + str(x)
    for i in range (1, len(tap)):
        #print "comparing x: " + str(x) + " the seed value " + str(seed[tap[i]])
        if(x == int(seed[tap[i]])):
            x=0
        else:
            x=1
        #print "the result is " + str(x)
    #print x,
    return x


def lfsr( tap_pos , seed_str ):
    #print seed_str[0]
    print str(seed_str[0])+ "  " ,
    result = xorf( tap_pos , seed_str )
    seed_str = seed_str[1:]
    seed_str.append(result)
    #print
    #print "the seed value is " + str(seed_str) + " result " + str(result)
    #print " the cipher random number is  " + str(d)
    #print
    #print seed_str
    return seed_str
    




print " The seed valuse should be exactly equal to the length of the shift register "
## for inputting the length ###
length = str ( raw_input( " enter the LENGTH OF THE SHIFT REGISTER "))
### for inputting the tap positions ###
tap = str ( raw_input(" enter the tap positions "))
### for inputing the seed value ####
seed = str (raw_input( "enter the seed value for the shift REGISTER " ) )
### for inputing the number of clock cycles ###
clock_pulse = int ( raw_input ("enter the number of clock pulses "))

tap_pos = []
for i in range (0, len(tap)):
    integer =  int (tap[i])
    tap_pos.append(integer)

seed_str = []
for i in range(0, len(seed)):
    integer = int (seed[i])
    seed_str.append(integer)

for i in range (0, clock_pulse):
    seed_str = lfsr( tap_pos , seed_str )
    #print seed_str
    #print

