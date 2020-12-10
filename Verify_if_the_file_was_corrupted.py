#!/usr/bin/python3.6
import hashlib
import os

#main
md5_hash=hashlib.md5()
g=open("verifyout.txt","w")
block_size=2**4
with open("dateout.txt","rb") as file:
	while True:
		linie=file.readlines(block_size)
	
		if not linie:
			break
		sir=str(linie)
		sir=sir[:len(sir)-4]
		sir=sir[3:]
		i=0
		for caracter in sir:
			if caracter==',':
				known_hash=sir[i+1:]
				sir=sir[:i]
				break
			i=i+1
				
		md5_hash.update(repr(sir).encode('utf-8'))
		digest=md5_hash.hexdigest()
		g.write(sir)
		g.write(",")
		if known_hash==digest:
			g.write("Same hash")
		else:
			g.write("Different hash")
		g.write("\n")
		g.flush()
g.close()
		
		
