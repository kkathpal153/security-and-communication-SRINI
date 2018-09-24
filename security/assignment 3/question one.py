
def ceaser_cipher():
    def encrypt_ceaseri( string, key ) :
        k = []
        print "the message sting is  is  " + string 
        for i in range(0, len(string)):
            d = ord (string [i])
            if ( d + key > 122 ) :
                d = 97 + ((d+key) % 122)-1
            else:
                d = d+key
            k.append ( chr(d))
        s=""
        for i in range ( 0 , len (k)):
            s=s+k[i]
        return s

    def decrypt_ceaser ( string , key ):
        k = []
        for i in range(0, len(string)):
            d = ord (string [i])
            if ( d - key < 97 ) :
                d = 122 - (key - (d -97)) +1
            else:
                d = d-key
            k.append ( chr(d))
        s=""
        for i in range ( 0 , len (k)):
            s=s+k[i]
        return s

    string = str(raw_input("enter the string for ceaser cipher : "))

    ceaser_key = int(raw_input("enter the key for ceaser cipher : "))
    ceasere = encrypt_ceaseri(string,ceaser_key)
    print "the encrypted ceaser message is : "+ ceasere
    ceaserd = decrypt_ceaser(ceasere , ceaser_key)
    print "the encrypted ceaser message is : "+ ceaserd
    print "\npress \n1. For Matrix Transposition \n2. Vigenere cipher \n3. Matrix Transposition \n 4. Exit"
    return int(raw_input("Enter your choice : "))


def vegenere_cipher():
    vengence_matrix =[[0 for x in range(0,26)] for y in range(0,26)]
    f=0
    def matrix_making():
        f=0
        for i in range (0,26):
            for j in range (0,26):
                if((j+97+f) > 122):
                    #print "if condition running at" + str(97 +j +f)
                    vengence_matrix[i][j] = chr ( (j+97+f)%122 + 96)
                else:
                    vengence_matrix [i][j]= chr(j+97+f)
            f=f+1
    #### to manipulate the secret key###
    def secretm (secret_key,vstring):
        secret_key2=''
        j=0
        for i in range(0,len(vstring)):
            if(j==len(secret_key)):
                j=0
            secret_key2=secret_key2+secret_key[j]
            j=j+1
        ##print secret_key2
        #print "above is the string" + str(len(vstring)) + str (len(vstring))
        return secret_key2
        
    ### function to decrypt vegenence###

    def vegee(vegemat , string ,key):
        d=''
        for i in range(0,len(key)):
            d = d+ vegemat[(ord(string[i]))-97][(ord(key[i]))-97]
        return d

    def veged(vegemat , estring , key):
        d=''
        for i in range(0,len(key)):
            ### first finding the position of i ###
            xval=0
            for j in range(0,26):
                if( key[i] == vegemat[0][j]):
                    xval=j
                    break
            yval = 0
            for j in range(0,26):
                if ( estring[i] == vegemat[xval][j]):
                    yval = j
            d=d + chr(yval + 97)
        return d
                

    vstring = str(raw_input("enter the string to be converted using vegenece cipher "))
    secret_key =str(raw_input( "enter the secret key"))


    matrix_making()
    for i in range(0,26):
        print vengence_matrix[i]

    ###manipulating the key string according to the user###
    secret_keym = secretm(secret_key,vstring)

    ### function to get the encrypted string ###
    vstringe = vegee(vengence_matrix, vstring, secret_keym)
    print "the encrypted string is " + vstringe

    print "now doing the decrypt function "
    vstringd = veged(vengence_matrix, vstringe, secret_keym)
    print " the decrypted string is " + vstringd
    
    print "\npress \n1. For Matrix Transposition \n2. Vigenere cipher \n3. Matrix Transposition \n 4. Exit"
    return int(raw_input("Enter your choice : "))

def matrix_trans():
    ### code for matrix transposition###

    s = str( raw_input("enter the string : "))
    string= ''
    for i in range(0,len(s)):
        if(s[i] == ' '):
            string = string + '%'
        else:
            string = string + s[i]
    print string

    k= str(raw_input( "enter the key  : "))
    key = []
    for i in range ( 0 ,len(k)):
        key.append( (ord(k[i])) - 48 )

    ########333
     ## diy
    if((len(string)%len(key)) != 0):
        e=(len(string) / len(key))+1
    else:
        #print "else is running"
        e = len(string) / len(key)
    ###########

    c=0
    ### function for encryption###
    mat =[[0 for x in range(0,len(key))] for y in range(0,e)]
    for i in range(0,e):
        for j in  range(0,len(key)):
            if(c<len(string)):
                mat[i][j]=string[c]
            else:
                mat[i][j]='%'
            c = c+1

    for i in range(0,e):
        print mat[i]
    print key
    encrypted = ''
    for i in range(0,len(key)):
        for j in range(0,e):
            #print " the x value is " + str(j) + " the value of y is " + str(key[i]) 
            encrypted = encrypted + mat[j][key[i]-1]
    print " the encrypted message is " 
    print encrypted


    print " the decrypted message is "

    if((len(encrypted)%len(key)) != 0):
        ss=(len(encrypted) / len(key))+1
    else:
        #print "else is running"
        ss= len(encrypted) / len(key)
    #print ss
    print
    matd =[[0 for x in range(0,len(key))] for y in range(0,ss)]
    c=0
    for i in range(0,len(key)):
        for j in  range(0,ss):
            matd[j][i]=encrypted[c]
            c = c+1
    for i in range(0,ss):
        print matd[i]
    decrypted = ' '
    
    for i in range(0,ss):
        for j in range(0,len(key)):
            #print " the x value is " + str(j) + " the value of y is " + str(key[i])
            decrypted = decrypted + matd[i][key[j]-1]

    print decrypted
    decrypted2=''
    for i in range(0,len(decrypted)):
        if(decrypted[i] == '%'):
            decrypted2 = decrypted2 + ' '
        else:
            decrypted2 = decrypted2 + decrypted[i]

    print " the decrypted message is " +str(decrypted2)
    
    print "\npress \n1. For Matrix Transposition \n2. Vigenere cipher \n3. Matrix Transposition \n4. Exit"
    return int(raw_input("Enter your choice"))


print "press \n1. For Ceaser Cipher \n2. Vigenere cipher \n3. Matrix Transposition \n4. Exit"
j = int(raw_input("Enter your choice in numeric form : "))


while(j != 4):
    if( j == 1):
        j = ceaser_cipher()        
    elif ( j== 2):
        j = vegenere_cipher()
    elif ( j == 3):
        j = matrix_trans()
    else:
        exit

        
        
### these functions are for matrix transposition ####



## naive solution ###



