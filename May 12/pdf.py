#import library
import fitz

#Define function for extracting
def extract():
    pdf = fitz.open("llm.pdf")
    text=[] #initialize empty list to store text
    #Loop through all pages
    for pages in pdf:
        texts = pages.get_text() #Extract text
        text.append(texts) #Appent it
    pdf.close() #Close file
    all="".join(text) #Combine all page text to single string
    print( "Extracted text\n ",all)
extract()
