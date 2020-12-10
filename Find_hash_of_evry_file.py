#!/usr/bin/python3.6
import hashlib
import os


def director(cale_director):
	for (root,dirs,files) in os.walk(cale_director,topdown=True):
		for dire in dirs:
			dname=os.path.join(root,dire)
			md5_hash.update(repr(dname).encode('utf-8'))
			digest=md5_hash.hexdigest()
			sir=str(dire)
			g.write(dname)
			g.write(",")
			g.write(digest)
			g.write("\n")
		for filename in files:
			fname=os.path.join(root,filename)			
			md5_hash.update(repr(fname).encode('utf-8'))
			digest=md5_hash.hexdigest()
			g.write(fname)
			g.write(",")
			g.write(digest)
			g.write("\n")



#main
md5_hash=hashlib.md5()
g=open("dateout.txt","w")
block_size=2**4
with open("datein.txt","rb") as file:
	while True:
		linie=file.readlines(block_size)
	
		if not linie:
			break
		
		sir=str(linie)
		sir=sir[:len(sir)-4]
		sir=sir[3:]
		
		isdir=os.path.isdir(sir)
		if isdir==True:
			md5_hash.update(repr(sir).encode('utf-8'))
			digest=md5_hash.hexdigest()
			directory=str(sir)
			g.write(directory)
			g.write(",")
			g.write(digest)
			g.write("\n")
			director(directory)
		else:
			md5_hash.update(repr(sir).encode('utf-8'))
			digest=md5_hash.hexdigest()
			sir=str(linie)
			sir=sir[:len(sir)-4]
			sir=sir[3:]
			g.write(sir)
			g.write(",")
			g.write(digest)
			g.write("\n")
			g.flush()
g.close()



	
