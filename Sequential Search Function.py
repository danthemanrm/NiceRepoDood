'''
sequential search function
licensed under GNU General Public License 3.0

created--------2/2/16
last updated---2/2/16

changelog:
	v1.0 - program created
	v1.1 - code commented, falling for the meme
	v1.2 - strings moved about, ya boi efficiency
	v1.3 - extra validation added
'''

Scores = ['MIK','JIM','SUZ','JIM','MAN','JIM','REE','REE','RIP','SUZ'] #array containing ten predetermined items

def sequentialSearch():
	
	userInput = input('What name are you searching for? ').upper() #upper used for validation
	
	if userInput in Scores: #if the user's input is found in the Scores array it displays so to user
		print('ya boi on the table. they appear',Scores.count(userInput),'time(s) in the scoreboard\n') #displays how many positions the user's input holds)
		
		print('ya boi in position(s):')
		for i in range(len(Scores)): #repeated same number of times as there are spaces in array to check all positions
			if Scores[i]==userInput: #if the user's input = current position in Scores array, it displays it
				print ('   ',i+1) #prints the position +1, (counting starts at 1)
				
	else:
		print('no nig nog of this name be on here fam') #validates user's input, item not in array
		
	restart = input('\nWould you like to restart? (y/N) ').lower() #N default action if null
	print('\n') #shitty workarounds for a free space my doods
	if restart == "y":
		sequentialSearch() #restarts function at user's command
	else:
		return
			
		
sequentialSearch()
exit
