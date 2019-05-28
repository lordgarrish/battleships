#battleships game 

import random


field = [[], [], [], [], [], [], []] 
DX = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
num_of_tries = 15
num_of_hits = 0
win = False

#adding three small(one-point) ships to the field
field[random.randint(0, 1)].append(random.randint(1, 7))
field[random.randint(2, 3)].append(random.randint(1, 7))
field[random.randint(4, 6)].append(random.randint(1, 7))

#adding two medium(two-point) ships to the field
counter = 2
for f in field:
	if len(f) == 0:
		r = random.randint(1, 6)
		f.append(r)
		f.append(r + 1)
		counter -= 1
	if counter == 0:
		break

#adding one big(three-point) ship to the field
for f in field:
	if len(f) == 0:
		r = random.randint(1, 5)
		f.append(r)
		f.append(r + 1)
		f.append(r + 2)
		break

def shoot(letter, y):
	global num_of_hits
	
	if letter in DX:
		x = DX.index(letter)
	else:
		print('Invalid input...')
		return
	
	if y not in range(1, 8):
		print('Invalid input...')
		return
	else:
		if y in field[x]:
			num_of_hits += 1
			field[x].remove(y)
			if len(field[x]) == 0:
				print('Kill!')
			else:
				print('Hit!')
		else:
			print('Missed!')


print('Welcome to Battleships Game!')
print()
while num_of_tries > 0:
	l = input('Please, input a letter from A to G: ')
	n = int(input('Please, input a number from 1 to 7: '))
	print()
	
	shoot(l, n)
	num_of_tries -= 1
	print('You have {0} rocket(s) left!'.format(num_of_tries))
	print()
	
	if num_of_hits >= 10:
		print('You win!')
		win = True
		break

if not win:
	print('You lose...')

