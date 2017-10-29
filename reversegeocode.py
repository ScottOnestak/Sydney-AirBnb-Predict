import geocoder

def geos(lat,lon):
	g = geocoder.google([lat,lon], method='reverse')
	print(g)
	return(g.city)

with open('syd-2017-06-28.csv','w') as file:
	with open('chunk2.csv','r') as f:
		theheader = next(f)
		theheader = theheader.split(",")
		theheader = theheader[0] + "," + theheader[2] + "," + theheader[3] + "," + theheader[7] + "," +theheader[8] + "," +theheader[9] + "," +theheader[10] + "," +theheader[11] + "," +theheader[13] + "," +theheader[16] + "," +theheader[17] + ",suburb" + "\n"
		file.write(theheader)
		for x in f:
			x = x.replace("\n","")
			thearray = x.split(",")
			lat = thearray[16]
			lon = thearray[17]
			print(lat)
			print(lon)
			city = geos(lat,lon)
			if(city==None):
				city = "NA"
			newline = thearray[0] + "," + thearray[2] + "," + thearray[3] + "," + thearray[7] + "," +thearray[8] + "," +thearray[9] + "," +thearray[10] + "," +thearray[11] + "," +thearray[13] + "," +thearray[16] + "," +thearray[17] + "," + city + "\n"
			file.write(newline)
print("Done")
		
		
