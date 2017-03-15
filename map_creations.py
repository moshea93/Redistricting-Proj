import shapefile
from shapely.geometry import Polygon
from datetime import datetime

def create_neighbor_table(sf):

	shapeRecs = sf.shapeRecords()
	shape = Polygon(shapeRecs[0].shape.points)
	print datetime.now()
	for rec in shapeRecs:
		test = Polygon(rec.shape.points)
		if shape.touches(test):
			print rec.record[0]
	print datetime.now()

if __name__ == '__main__':
	sf = shapefile.Reader("state_zip_shapefiles/pennsylvania")
	create_neighbor_table(sf)
