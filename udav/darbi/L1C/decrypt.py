fmeta = open("meta.bin", "rb")                      
fmeta.seek(0)                                       

fdata = open("data.bin", "rb")                      
fdata.seek(0)                                        

poz = 0                                                 
odd = bool(True)                                      

while 1:                                              
	b = fmeta.read(1)                            
	if not b:                                    
		break                                  
	if odd:                                      
		poz = poz + ord(b)                     
		fdata.seek(poz)                       
		x = fdata.read(1)                    
		odd= not odd                         
	else:
						
		print chr(ord(b)^ord(x))                   
		odd= not odd                         
		                                       
fmeta.close()                                        
fdata.close()					     
