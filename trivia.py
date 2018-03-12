#!/usr/bin/python
# Group 19
# CS361-400
# HW 6 User Story 3 Multi-level Game

class Question:
	

	
	def __init__(self, question, a0, a1, a2, a3, correct, level):
		self.question = question
		self.answers = ["", "", "", ""]
		self.answers[0] = a0
		self.answers[1] = a1
		self.answers[2] = a2
		self.answers[3] = a3
		self.correct = correct
		self.level = level
	
	def play(self, xp):
		valid = False
		while valid == False:
			self.printTrivia(xp)
			answer = raw_input("Answer: ")
			if(answer == "1" or answer == "2" or answer == "3" or answer == "4"):
				valid = True
		
		if(int(answer) == (self.correct + 1)):
			print("\nCorrect!\n")
			xp += (5 * self.level)
			return int(xp)
		else:
			print("\nThe correct answer is: " + self.answers[self.correct] +"\n")
			return int(xp)
			
	def printTrivia(self, xp):
		print("XP: " + str(xp) + "		Level " + str(self.level) + "\n\n")
		print(self.question + "\n")
		print("1. " + self.answers[0] + "\n")
		print("2. " + self.answers[1] + "\n")
		print("3. " + self.answers[2] + "\n")
		print("4. " + self.answers[3] + "\n\n")
			

if __name__ == '__main__':
	
	q11 = Question("A diversified portfolio consists of", "a single stock", "stocks in several different companies in a single industry", "stocks in a range of indexes over several markets", "buying 2 different cryptocurrencies", 2, 1)
	q12 = Question("When making investments for retirement it is best to consult with whom", "News channel talking heads", "your family", "a tarot deck", "a fiduciary", 3, 1)
	q13 = Question("IPO stands for", "Investor Payment Options", "Interest Payment Originator", "Initial Public Offering", "Investment Potential Outlook", 2, 1)
	q21 = Question("Short selling can be profitable when", "Stock prices are expected to fall", "Stock prices are expected to rise", "Stock prices are expected to remain the same", "No prediction on stock prices can be made", 0, 2)
	q22 = Question("Short term investments can be expected to be converted into cash within", "one month", "one year", "five years", "24 hours", 1, 2)
	level1 = [q11, q12, q13]
	level2 = [q21, q22]
	xp = 0
	for x in level1:
		xp = x.play(xp)
	print("===========================================")
	print("Level 2")
	print("===========================================")
	for x in level2:
		xp = x.play(xp)
	print("\n\n\nXP earned: " + str(xp))	
		
	


