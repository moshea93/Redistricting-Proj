import shapefile
import matplotlib.pyplot as plt

def plot(sf):
	plt.figure()
	for shape in sf.shapeRecords():
		x = [i[0] for i in shape.shape.points[:]]
		y = [i[1] for i in shape.shape.points[:]]
		plt.plot(x,y)
	plt.show()

if __name__ == '__main__':
	sf = shapefile.Reader('state_zip_shapefiles/pennsylvania')
	plot(sf)
