count = 1
over100 = False
Question1 = []
AnswerA = []
AnswerB = []
AnswerC = []
AnswerD = []
Answer = []

import re

def addQuestions(page):
	global count
	global over100
	#find question COUNT in PDF
	completed = False;

	while(not completed):

		if(count > 100):
			start = page.index(str(count-100)+".")

			if(page.find(str(count-100+1)+".") == -1):
				end = len(page)+1
				completed = True
				
			else:
				end = page.index(str(count-100+1)+".")
				count+=1
		else:
			start = page.index(str(count)+".")

			if(page.find(str(count+1)+".") == -1):
				end = len(page)+1
				completed = True
				
			else:
				end = page.index(str(count+1)+".")
				count+=1

		QSet = page[start:end]

		if(count <= 100):
			questionEnd = QSet.find('A.')
			question = QSet[0:questionEnd]
			Question1.append(question)

			if(QSet.find('C.') < QSet.find('B.')):

				start1 = questionEnd
				end1 = QSet.find('C.')
				AnswerA.append(QSet[start1:end1].strip())

				start1 = end1
				end1 = QSet.find('B.')
				AnswerC.append(QSet[start1:end1].strip())

				start1 = end1
				end1 = QSet.find('D.')
				AnswerB.append(QSet[start1:end1].strip())

				start1 = end1
				end1 = len(QSet)
				AnswerD.append(QSet[start1:end1].strip())

			if(QSet.find('C.') > QSet.find('B.')):
				start1 = questionEnd
				end1 = QSet.find('B.')
				AnswerA.append(QSet[start1:end1].strip())

				start1 = end1
				end1 = QSet.find('C.')
				AnswerB.append(QSet[start1:end1].strip())

				start1 = end1
				end1 = QSet.find('D.')
				AnswerC.append(QSet[start1:end1].strip())

				start1 = end1
				end1 = len(QSet)
				AnswerD.append(QSet[start1:end1].strip())

		else:
			a = re.search(r'\b(SOURCE)\b', QSet.strip())
			Answer.append(QSet.strip()[0:a.start()])

import PyPDF2
file = "Tests/"+input("What PDF do you want to practice? eg: Business.pdf, Entrepreneurship.pdf, Finance.pdf, Hopitality.pdf, Marketing.pdf, PFL1.pdf, PFL2.pdf, PFL3.pdf, PFL4.pdf ")
print()
pdfFileObj = open(file, 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
# creating a page object

for i in range(1,pdfReader.numPages):
	pageObj = pdfReader.getPage(i) 
	recieved = (pageObj.extractText())
	addQuestions(recieved)
	count+=1

print(AnswerA)

pdfFileObj.close()
