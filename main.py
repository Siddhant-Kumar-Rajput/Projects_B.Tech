import pyttsx3
import pdfplumber
import PyPDF2

file = 'C:/Users/Siddhant/PycharmProjects/audiobook/oop.pdf'

#Creating a PDF File Object
pdfFileObj = open(file, 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#Get the number of pages
pages = pdfReader.numPages
print(pages)

#Jump to page
page=int(input("which page number"))
number=pdfReader.getPage(page)

with pdfplumber.open(file) as pdf:
 #Loop through the number of pages
    for j in range(page, pages):
      look = pdf.pages[i]
      text = look.extract_text()
      print(text)
      speaker = pyttsx3.init()
      speaker.say(text)
      speaker.runAndWait()
      j=j+1