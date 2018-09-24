## readinfg file contaning existing fdb""




def evaluation( l ):
    source = l[0]
    destination = l[1]
    port= l[2]
    print source + "\t" + destination  + "\t" + port +"\t" ,
    if(fd.has_key(source) != True ):
        fd[source] = port
        print message[1],
        if(fd.has_key(destination) == True):
            if( str(fd[source]) == str(fd[destination])):
                print "; " + message[0],
            else:
                print "; " + message[2] + "  " + str(fd[destination]) ,
        else:
            print "; " + message[3],
    else:
        if(fd.has_key(destination)== True):
            if( str(fd[source]) == str(fd[destination]) ):
                print message[0],
            else:
                print message[2] + " " + str( fd[destination]),
        else:
            print message[3],
    print


### list of messages that i have to print ###
message = ["Frame Discarded " ,
           "Fdb Updated ",
           "Frame Sent on Port" ,
           "Frame Broadcast on all out ports "]

fdb_file= open("fdb.txt","r")
sor_dest_file = open ("sd.txt", "r")
c=0
fd={}
sd={}


for i in fdb_file:
    l = i.split()
    if(c!=0):
        fd[l[0]] = l[1]
    c=c+1
c=0




print "FDB INTITIALLY "
print fd,
print "\n \n"
for i in sor_dest_file:
    l = i.split()
    sd[c] = l
    evaluation(l)
    c=c+1

print "\n\nFDB UPDATED"
print fd

    



## made a dictionary of the given forwarded data ###

