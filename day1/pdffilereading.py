import PyPDF2
import os
dirPath="E:\\MTSTraningmay2025\\day1\\documents"


for(dirPath,dirNames,fileNames) in os.walk(dirPath):
    print("Directory:", dirPath)
    print("Subdirectories:", dirNames)
    print("Files:", fileNames)
    for file in fileNames:
        (shortFileName, extension) = os.path.splitext(file)
        if(extension == ".pdf"):
            print("Processing file:", file)
            
            with open(dirPath+"/"+file, mode='rb') as pdfFile:
                reader = PyPDF2.PdfReader(pdfFile)
                print("Number of pages:", len(reader.pages))
                
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        print("Page Text:", text)
                    else:
                        print("No text found on this page.")    
                        