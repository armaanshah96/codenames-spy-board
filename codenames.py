import random

OKBLUE = '\033[1;94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
BOLD = '\033[1m'
ENDC = '\033[0m'
RED = "\033[1;31m"  


def gameBoard( list ):
	"blue is the number of blue cards"
	array = [];
	for b in range(list[0]):
		array.append(OKBLUE + "blu" + ENDC);
	for r in range(list[1]):
		array.append(RED + "red" + ENDC);
	for n in range(7):
		array.append("neu");
	array.append(BOLD + "ass" + ENDC)

	random.shuffle(array);

	row = 0;
	s = " | ";
	for i in range(0,len(array),5):
		print("|----------------------------|");
		print("|" + s.join(array[i:i+5]) + " |");
	
	print("------------------------------");
	return;

gameBoard([9,8]);
