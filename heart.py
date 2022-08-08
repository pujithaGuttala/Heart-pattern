i=0
while i<6:
	j=0
	while j<7:
		if (i==0 and j%3!=0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
			print ("*",end=" ")
		else:
			print (" ", end=" ")
		j=j+1
	print ( )
	i=i+1