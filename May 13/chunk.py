#Import libraries
import fitz
#Function to extract text
def extract():
    pdf=fitz.open('chunks.pdf')
    text=[] #initialize empty list to store text
    #Loop through all pages
    for pages in pdf:
        texts = pages.get_text() #Extract text
        text.append(texts) #Appent it
    pdf.close() #Close file
    return text
#Fuction for chunking
def chunk_txt():
    all_text = " ".join(text) #join all text to single string
    words = all_text.split() #split string into individual words
    chunks = [] #initialize list to store
    size =35
    #create chunks of words
    for i in range(0,len(words),size):
        ch=words[i:i + size]
        chunks.append(ch)
    return chunks
text=extract()
chunks=chunk_txt()
#print each chunk with index
for idx,ch in enumerate(chunks):
    print(f"Chunk {idx+1}")
    print(ch[:300])
    print()
