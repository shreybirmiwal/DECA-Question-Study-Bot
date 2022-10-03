count = 0
over100 = False
questionAnswer = []
AnswersOnly = []
AnswersOnly.append("NO ASNWER FOR THIS QUESTION MY B GANG U KEEP STUDYING HARD DOE FAM")

def playGame(questionAnswer):
	questionCount = 0
	for element in questionAnswer:
		for item in element:
			print(item)
		print(AnswersOnly[questionCount])
		questionCount+=1

def addQuestions(page):
	global count
	global over100
	#find question COUNT in PDF
	completed = False;

	while(not completed):

		if(count == 101):
			completed = True
			break

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
		#print(QSet)
		#for each question + question choice set, add to answer choices
		answerChoices = []

		if(count <= 100):
			questionEnd = QSet.find('A.')
			question = QSet[0:questionEnd]

			answerChoices.append(question)

			#print(QSet)

			if(QSet.find('C.') < QSet.find('B.')):

				start1 = questionEnd
				end1 = QSet.find('C.')
				answerChoices.append(QSet[start1:end1])

				start1 = end1
				end1 = QSet.find('B.')
				answerChoices.append(QSet[start1:end1])

				start1 = end1
				end1 = QSet.find('D.')
				answerChoices.append(QSet[start1:end1])

				start1 = end1
				end1 = len(QSet)
				answerChoices.append(QSet[start1:end1])

			if(QSet.find('C.') > QSet.find('B.')):
				start1 = questionEnd
				end1 = QSet.find('B.')
				answerChoices.append(QSet[start1:end1])

				start1 = end1
				end1 = QSet.find('C.')
				answerChoices.append(QSet[start1:end1])

				start1 = end1
				end1 = QSet.find('D.')
				answerChoices.append(QSet[start1:end1])

				start1 = end1
				end1 = len(QSet)
				answerChoices.append(QSet[start1:end1])

			#print(answerChoices)
			questionAnswer.append(answerChoices)
		
		else:
			AnswersOnly.append(QSet)

import PyPDF2
pdfFileObj = open('2022.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
# creating a page object

for i in range(1,pdfReader.numPages):
	pageObj = pdfReader.getPage(i) 
	recieved = (pageObj.extractText())
	addQuestions(recieved)
	count+=1

AnswersOnly.append("")
playGame(questionAnswer)

pdfFileObj.close()
