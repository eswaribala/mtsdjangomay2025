import fitz
import os
dirPath="E:\\MTSTraningmay2025\\day1\\documents\\images"


for(dirPath,dirNames,fileNames) in os.walk(dirPath):
    print("Directory:", dirPath)
    print("Subdirectories:", dirNames)
    print("Files:", fileNames)
    for file in fileNames:
        (shortFileName, extension) = os.path.splitext(file)
        if(extension == ".pdf"):
            print("Processing file:", file)
            
            with fitz.open(dirPath+"/"+file) as pdfFile:
                print("Number of pages:", len(pdfFile))
                
                for page_num in range(len(pdfFile)):
                    page = pdfFile[page_num]
                    images = page.get_images(full=True)
                    if images:
                        print(f"Page {page_num + 1} has {len(images)} images.")
                        for img_index, img in enumerate(images):
                            xref = img[0]
                            base_image = pdfFile.extract_image(xref)
                            image_bytes = base_image["image"]
                            image_filename = f"{shortFileName}_page{page_num + 1}_img{img_index + 1}.png"
                            
                            with open(os.path.join(dirPath, image_filename), "wb") as image_file:
                                image_file.write(image_bytes)
                            print(f"Extracted image saved as: {image_filename}")
                    else:
                        print(f"Page {page_num + 1} has no images.")
                        