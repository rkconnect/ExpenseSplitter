i = 0
flag = True
item = 1
expenditure = []
paid = []
balance = []
payer = ''

#Input number of participant
while flag:
	try:
		numOfParticipant = int(input('Please Enter Number of Participant:'))
		if (numOfParticipant <= 0):
			raise ValueError('Add some participant')
		else:
			flag = False
	except TypeError:
		print ('Add some participant')
	except ValueError:
		print ('Add some participant')

#Input names of all the participant
participant = list(range(numOfParticipant))
print(participant)
while i < numOfParticipant:
	participant[i] = input('Participant#' + str(i + 1) + ':')
	i += 1
print(participant)

balance = list(range(numOfParticipant))

#Add expenditure
print("Please add all the expenditures one by one.\nIf there is nothing else to add, please input 0 to see the output.")

while True:
	try:
		expenditure.append(float(input('Please input Expenditure#' + str(item) + 'Amount:')))
		payer = input('Expenditure#' + str(item) + 'Amount was paid by:')
		item += 1

		if payer not in participant:
			raise ValueError('Enter valid payer')

	except ValueError:
		print('Please enter a valid payer')

	except TypeError:
		print('Please enter a valid payer')






















