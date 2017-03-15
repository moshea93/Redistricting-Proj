import shapefile
import csv

def get_state_references(state_shapefile):
	records = state_shapefile.records()
	with open('state_references.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(['Number', 'Abbreviation', 'State'])
		for record in records:
			writer.writerow([record[0], record[1], record[2]])

def single_state_zips(number, abbreviation):
	target = {}
	with open('zip_to_state.txt', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			if row[1] == number:
				target[row[0]] = 1
	with open('state_zips/'+abbreviation+'_zips.txt', 'w') as g:
		writer = csv.writer(g)
		for zipcode in target:
			writer.writerow([zipcode])

def get_state_zips(state_refs):
	abbreviations = []
	numbers = []
	with open(state_refs, 'r') as f:
		reader = csv.reader(f)
		reader.next()
		for row in reader:
			abbreviations.append(row[1])
			numbers.append(row[0])
	for x in range(len(numbers)):
		single_state_zips(numbers[x], abbreviations[x])

if __name__ == '__main__':
	sf = shapefile.Reader("State_2010Census_DP1/State_2010Census_DP1")
	get_state_references(sf)
	get_state_zips('state_references.csv')
