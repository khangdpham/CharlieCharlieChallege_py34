import random, sys, hashlib,os

#CharlieCharlie.py: Challenge.
#
#__author__      = "Khang Pham"
#__copyright__   = "Copyright 2015, Planet Earth"
#__license__ = "GPL"
#__email__ = "khangpham@ymail.com"
#__status__ = "Production"


while(1):
	question = input('\nCharlie, Charlie,...')
	array = os.urandom(1 << 20)
	md5 = hashlib.md5()
	md5.update(array)
	digest = md5.hexdigest()
	number = int(digest, 16)
	answer = number%2
	print("")
	if answer == 0:
		first_ans="\n||\t{}\t||\t{}\t||".format("YES","  ")
		sec_ans  ="\n||\t{}\t||\t{}\t||".format("   ","YES")
	else:
		first_ans="\n||\t{}\t||\t{}\t||".format("   ","NO")
		sec_ans  ="\n||\t{}\t||\t{}\t||".format("NO","")
	for i in range(len(first_ans)+1):
		print("=",end=' ')
	print(first_ans)
	for i in range(len(first_ans)+1):
		print("=",end=' ')
	print(sec_ans)
	for i in range(len(first_ans)+1):
		print("=",end=' ')
	print("")