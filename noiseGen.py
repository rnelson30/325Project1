from random import randint
import csv

with  open('logFile.csv', 'r') as datafile:
   datareader = csv.reader(datafile, delimiter='~')
   data = []
   noiseData = []
   for row in datareader:
      data.append(row) 

   rows = len(data)      # get number of rows
   cols = len(data[0])   # get number of cols
  
   for row in range(rows):
      if(randint(0, 1) == 0):    # flip a coin
         noiseData.append(data[row])   # 0: add original row to new dataset 
      else:
         noiseRow = []           # 1: add noise row
         for i in range(cols):            # loop through column index
            if(randint(0,1) == 0):        # flip coin again
               noiseRow.append(data[row][i]) # 0: add initial column value
            else:                             # 1: 
               r = randint(0,rows-2)         # get random row in initial dataset
               noiseRow.append(data[r][i])   # append row,col combination to noise row
         noiseData.append(noiseRow)       # add noise row to new dataset

   with open('noiseLogFile.csv', 'w') as writeFile:  # make new csv
      writer = csv.writer(writeFile)
      writer.writerows(noiseData)       

   datafile.close()
   writeFile.close()

