import shapefile
import matplotlib.pyplot as plt
import csv

def plot(sf):
	plt.figure()
	for shape in sf.shapeRecords():
		x = [i[0] for i in shape.shape.points[:]]
		y = [i[1] for i in shape.shape.points[:]]
		plt.plot(x,y)
	plt.show()

def fieldsnrecords(sf):
	print 0
	records = sf.records()
	print 1
	fields = sf.fields
	print 2
	shapes = sf.shapes()
	print 3
	for x in range(len(records)):
		print records[x][0], records[x][1], records[x][2]
		#if records[x][1] == 'PA':
		#	for y in range(len(records[x])):
		#		print fields[y+1], records[x][y]
		#	print shapes[x]

if __name__ == '__main__':
	sf = shapefile.Reader("State_2010Census_DP1/State_2010Census_DP1")
	plot(sf)
	fieldsnrecords(sf)
