import csv
import os
dirPath="E:\\MTSTraningmay2025\\day1\\reports"


for(dirPath,dirNames,fileNames) in os.walk(dirPath):
    print("Directory:", dirPath)
    print("Subdirectories:", dirNames)
    print("Files:", fileNames)
    for file in fileNames:
        (shortFileName, extension) = os.path.splitext(file)
        if(extension == ".csv"):
            print("Processing file:", file)
            
            with open(dirPath+"/"+file, mode='r', newline='', encoding='utf-8') as file:
             reader = csv.reader(file)
             header = next(reader)  # Read the header row
             print("Header:", header)
    
             for row in reader:
               print("Row:", row)
             
        

