
import fitz

def extract():
    pdf = fitz.open("llm.pdf")
    text=[]

    for pages in pdf:
        texts = pages.get_text()
        text.append(texts)
    pdf.close()
    all="".join(text)
    print( "Extracted text\n ",all)
extract()
