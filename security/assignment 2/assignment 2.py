print("reading the acl file")
print("the content of acl file as foollows")
print(" access-list 1 deny 192.1.1.0 0.0.0.255  \n access-list 1 permit any \n interface E0 \n ip access-group 1 out ")

print ("ip text file")
print(" 192.1.1.1 \n 192.1.1.9 \n 192.1.2.1 \n 192.1.4.1")
print ("here the content is")

print (" 192.1.1.1  192.1.1.9 are the packets that are permitted")
print (" 192.1.2.1 192.168.4.1 are the packet that denied")

