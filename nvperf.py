#! /usr/bin/env python
# importing CSV module
import csv

# CSV file name
filename_1 = "./inputs/mmf-baseline.csv"
filename_2 = "./inputs/mmf-flopeff.csv"

# filename_1 = "C:\\Users\\sweth\\Desktop\\My Python\\csvs\\mmf-baseline.csv"
# filename_2 = "C:\\Users\\sweth\\Desktop\\My Python\\csvs\\mmf-flopeff.csv"
kpercent = {}
kflopeff = {}
with open(filename_1) as csvfile:
    next(csvfile, None) 
    
    reader = csv.DictReader(csvfile)

    #for row in reader:
         #print(row)
    for i, row in enumerate(reader): 
      # To Skip line  [('Type', ''), ('Time(%)', '%'), ('Time', 's'), ('Calls', ''), ('Avg', 'ms'), ('Min', 'ms'), ('Max', 'ms'), ('Name', '')] from file header
      if(i!=0):
      # Only including kernels greater than 1%
        if(float(row['Time(%)']) < 1.0):
          break
        kpercent[row['Name']] = float(row['Time(%)'])
      


with open(filename_2) as csvfile2:
    next(csvfile2, None) 
    next(csvfile2, None) 
    reader2 = csv.DictReader(csvfile2)
    for j, row in enumerate(reader2):
      if(row['Metric Name'] == 'flop_dp_efficiency'):
        kflopeff[row['Kernel']] = float(row['Max'].strip('%'))

#print (kpercent)
#print (kflopeff)
flopRate = 0.0
for key , value in kpercent.items() :
     for key1 , value1 in kflopeff.items() :
          if(key == key1) :
               # print (key , kpercent[key], kflopeff[key])
               flopRate += kpercent[key] * kflopeff[key]

# Flops percentage of peak
print("Flops (% peak): ", flopRate/100)
