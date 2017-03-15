import shapefile
import matplotlib.pyplot as plt

def get_zipcodes(state):
	zipcodes = {}
	with open('state_zips/'+state+'_zips.txt', 'r') as f:
		for row in f:
			zipcodes[(row[:5])] = 1
	return zipcodes

def plot(sf, state):
#	zipcodes = {}
#	with open('pa_zips.txt', 'r') as f:
#		for row in f:
#			zipcodes[(row[:5])] = 1
	zipcodes = get_zipcodes(state)
	plt.figure()
	for shape in sf.iterShapeRecords():
		if shape.record[0] in zipcodes:
			x = [i[0] for i in shape.shape.points[:]]
			y = [i[1] for i in shape.shape.points[:]]
			plt.plot(x,y)
	plt.show()

def justpa(sf, state):
	zipcodes = get_zipcodes(state)
	w = shapefile.Writer(shapeType=5)
	w.fields = list(sf.fields)
	for shape in sf.iterShapeRecords():
		if shape.record[0] in zipcodes:
			w.records.append(shape.record)
			w._shapes.append(shape.shape)
	w.save("pennsylvania")

def fieldsnrecords(sf):
	print 0
	shapes = sf.shapes()
	print 1
	records = sf.records()
	print 2
	fields = sf.fields
	print 3
	for y in range(len(records[0])):
		print fields[y+1], records[0][y]
	print len(records)

sf = shapefile.Reader("ZCTA_2010Census_DP1/ZCTA_2010Census_DP1")
#plot(sf, 'PA')
justpa(sf, 'PA')
#fieldsnrecords(sf)
