

rtr = open("rou.txt", "r")
read_rtr = rtr.readlines()[1:]


packets = open("pac.txt", "r")
repa = packets.readlines()

# this function is used for displaying tthe output
def display():
	print "\nPacket with " + epa + " will be forwarded to " + destination + " out on interface " + interface + " (" + flags+ ")"



for epa in repa:
	
	epa = epa.replace("\n","")
	cut = epa.split(".")
	#this functions read the ip address fromt the pac file and takes
	#takes the routing table form the menu and dsiplay everything
	for ere in read_rtr:
		ere = ere.split(" ")
		mask = ere[0]
		destination = ere[1]
		flags = ere[3]
		interface = ere[4]
		desti = ere[1]
		#i have made 4 conditions for each class A,B,C,D
		if mask == "255.255.255.255":
			air = epa
			if air == desti:
				display()
				break
		if mask == "255.255.255.0":
			air = cut[0]+ "." + cut[1]+ "." + cut[2] + ".0"
			if air == desti:
				display()
				break
		if mask == "255.255.0.0":
			air = cut[0]+ "." + cut[1]+ "." + "0.0"
			if air == desti:
				display()
				break
		if mask == "255.0.0.0":
			air = cut[0]+ "." + cut[1]+ "." + "0.0"
			if air == desti:
				display()
				break



