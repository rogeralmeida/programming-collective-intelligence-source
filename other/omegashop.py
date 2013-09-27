import csv

def readCSV():
	dataset={}
	with open('vendasOmegaShop.csv') as csvFile:
		lineReader=csv.reader(csvFile,delimiter=';')
		for row in lineReader:
			if row[0] not in dataset:
				dataset[row[0]]={}
			dataset[row[0]][row[1]]=int(row[2])
			print row
	return dataset