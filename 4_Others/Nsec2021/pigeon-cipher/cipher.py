#!/usr/bin/env python3

from hashlib import sha256
from base64 import b64encode, b64decode
from pathlib import Path

txt_folder = Path('messages').rglob('*')
files = [x for x in txt_folder]

# # extraction de tous les bytes de tous les message 
# tabl=[]
# for name in files:
#     f = open(name, 'r')  
#     content = f.readlines()
#     tabl.append(list(bytes(b64decode(content[0]))))
#     f.close()

#print(tabl)

# # classer tous les character a la meme position dans une meme liste
# tablOrd = []
# for x in range(83):
# 	y = []
# 	for message in tabl:
# 		y.append(message[x])
# 	tablOrd.append(y)

#print(tablOrd)

# # comparer ceux qui sont present le plus souvent
# countf=0
# countl=0
# counta=0
# countg=0
# countt=0
# for index,ligne in enumerate(tablOrd):

# 	if index == 0:
# 		for ele in ligne:
# 			if (ele == 70):
# 				countf = countf + 1
# 	if index == 1:
# 		for ele in ligne:
# 			if (ele == 76):
# 				countl = countl + 1
# 	if index == 2:
# 		for ele in ligne:
# 			if (ele == 65):
# 				counta = counta + 1
# 	if index == 3:
# 		for ele in ligne:
# 			if (ele == 71):
# 				countg = countg + 1
# 	if index == 4:
# 		for ele in ligne:
# 			if (ele == 45):
# 				countt = countt + 1
# print('F')
# print(countf)
# print('L')
# print(countl)
# print('A')
# print(counta)
# print('G')
# print(countg)
# print('-')
# print(countt)

print("miniscules")
tabl=[]

for name in files:
	with open (name, 'rt') as f: 
		count=0
		content = f.readlines()
		message = b64decode(content[0])
		if (message[0] == 102):
			count = count + 1
		if (message[1] == 108):
			count = count + 1
		if (message[2] == 97):
			count = count + 1
		if (message[3] == 103):
			count = count + 1
		if (message[4] == 45):
			count = count + 1
		if count == 2:
			print(name)



tabl=[]

for name in files:
	with open (name, 'rt') as f: 
		count=0
		content = f.readlines()
		message = b64decode(content[0])
		if (message[0] == 70):
			count = count + 1
		if (message[1] == 76):
			count = count + 1
		if (message[2] == 65):
			count = count + 1
		if (message[3] == 71):
			count = count + 1
		if (message[4] == 45):
			count = count + 1
		if count == 2:
			print(name)


# comparer ceux qui sont present le plus souvent
# tablMessage = []
# for index,ligne in enumerate(tablOrd):
# 	valeur = [x for x in ligne if (x < 127) and (x > 32)]
# 	final = min(valeur,key=valeur.count)
# 	#print(final)
# 	tablMessage.append(final)

#print(str(tablMessage, 'UTF-8'))

#tableaaaa = [23, 76, 126, 251, 125, 182, 19, 188, 149, 47, 97, 186, 211, 238, 53, 215, 185, 241, 189, 83, 32, 130, 88, 207, 55, 238, 152, 29, 191, 58, 79, 101, 74, 16, 158, 76, 121, 130, 214, 30, 166, 146, 236, 91, 236, 133, 169, 100, 2, 122, 224, 90, 39, 241, 223, 137, 113, 132, 144, 189, 65, 81, 196, 23, 230, 231, 29, 76, 152, 50, 238, 193, 40, 255, 39, 191, 65, 43, 124, 105, 16, 196, 50]

#print(''.join(chr(i) for i in tablMessage))



def cipher(key, value):
	i = 0
	ciphertext = b""

	for byte in value:
		mask = sha256(key + str(i).encode()).digest()[0]

		# If the mask is zero the byte won't be encrypted !
		# We must choose an other mask in this case
		if mask == 0:
			i += 1
			mask = sha256(key + str(i).encode()).digest()[0]

		ciphertext += bytes([byte ^ mask])
		i += 1

	return ciphertext



def encrypt(key, value):
	return b64encode(cipher(key, value))


def decrypt(key, value):
	return cipher(key, b64decode(value))
