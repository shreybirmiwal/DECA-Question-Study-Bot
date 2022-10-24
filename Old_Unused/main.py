count = 1
over100 = False
questionAnswer = []
AnswersOnly = []

import colorama
from colorama import Fore, Back, Style
colorama.init()


def playGame(questionAnswer):
	questionCount = 0
	for element in questionAnswer:
		for item in element:
			print(item.strip())

		UserAnswer = input("what is your answer? ").upper()
		correctAnswer = AnswersOnly[questionCount]
		if(UserAnswer == correctAnswer[3:4] or UserAnswer == correctAnswer[4:5]):
			print(Fore.GREEN + "CORRECT!")
			print(correctAnswer.strip())
			print()
			print(Style.RESET_ALL)

		else:
			print(Fore.RED + "WRONGGGG!")
			print(correctAnswer)
			print()
			print(Style.RESET_ALL)
			
		questionCount+=1

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

AnswersOnly.append("")
#print(questionAnswer)
playGame(questionAnswer)

pdfFileObj.close()
