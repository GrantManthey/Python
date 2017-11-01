
from new_cards import *
import random
#draws your starting hand of five cards
firstcard=random.sample(cards,5)
#checks the type of card and colors it accordingly
def drawhand():
	for card in firstcard:
		if card[0:1] == "1": #trap
			print("\033[1;35;40m %s \033[0;35;40m \n" % (card[1:]))
		elif card[0:1] == '2': #spell
			print("\033[1;36;40m %s \033[0;36;40m \n"% (card[1:]))
		elif card[0:1] == '3': #monster
			print("\033[1;33;40m %s \033[0;33;40m \n"% (card[1:]))
		else:
			print('whoops')
			
drawhand()
			

