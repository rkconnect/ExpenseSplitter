i = 0
flag = True
noErrorFlag = False
item = 1
expenditure = []
paid = []
balance = []
payer = ''
lastExpense = 0

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


def addExpenditure(lastExpense, numOfParticipant):
	expenditurePerHead = lastExpense/numOfParticipant
	for x in range(numOfParticipant):
		balance[x] += expenditurePerHead
	return 0

def addPayment(lastExpense, payer):
 	payerIndex = participant.index(payer)
 	balance[payerIndex] -= lastExpense
 	return 0


#Add expenditure
print("Please add all the expenditures one by one.\nIf there is nothing else to add, please input 0 to see the output.")

while True:
	try:
		lastExpense = float(input('Please input Expenditure#' + str(item) + ' Amount:'))
		if lastExpense == 0:
			break
		expenditure.append(lastExpense)
		payer = input('Expenditure#' + str(item) + ' Amount was paid by:')

		if payer not in participant:
			raise ValueError('Enter valid payer')
		noErrorFlag = True

	except ValueError:
		print('Please enter a valid payer')

	except TypeError:
		print('Please enter a valid payer')

	if noErrorFlag:
		addExpenditure(lastExpense, numOfParticipant)
		addPayment(lastExpense, payer)
		item += 1
		noErrorFlag = False

print(balance)
for people in range(numOfParticipant):
	if balance[people] == 0:
		print(participant[people] + ' doesn\'t need tp pay anyone.\nHe will not get anything from anyone.' )
	elif balance[people] < 0:
		print(participant[people] + ' will get back Rs' + str(0 - balance[people]))
	else:
		print(participant[people] + ' will pay Rs' + str(balance[people]))