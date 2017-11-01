
from new_cards import *
import random
#def printcard(card):
	#if card == "trap":
		#print(card)
	#trap 175 0 134
	
#while True:
firstcard=random.sample(cards,5)
for card in firstcard:
	if card[0:1] == "1": #trap
		print("\033[1;35;40m %s \033[0;35;40m \n" % (card[1:]))
	elif card[0:1] == '2': #spell
		print("\033[1;36;40m %s \033[0;36;40m \n"% (card[1:]))
	elif card[0:1] == '3': #monster
		print("\033[1;33;40m %s \033[0;33;40m \n"% (card[1:]))
	
	
#print(firstcard)
	#printcard(secondcard)
	#printcard(thirdcard)
	#printcard(fourthcard)
	#printcard(fithcard)
	#break

#secondcard=random.sample(list(cards),1)
	#thirdcard=random.sample(list(cards,1)
	#fourthcard=random.sample(list(cards,1)
	#ithcard=random.sample(list(cards),1)
	#if secondcard != firstcard: and thirdcard != secondcard and  thirdcard != firstcard and fourthcard != thirdcard and fourthcard != secondcard and fourthcard != firstcard and fithcard != fourthcard and fithcard != thirdcard and fithcard != secondcard and fithcard != firstcard:

#print("\033[0;37;40m Normal text\n")
#print("\033[2;37;40m Underlined text\033[0;37;40m \n")
#print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
#print("\033[3;37;40m Negative Colour\033[0;37;40m \n")
#print("\033[5;37;40m Negative Colour\033[0;37;40m\n")
 
#print("\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
#print("\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
#print("\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
#print("\033[1;32;40m Bright Green   \033[0m 1;32;40m  clea          \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
#print("\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
#print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
#print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
#print("\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
#print("\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")
