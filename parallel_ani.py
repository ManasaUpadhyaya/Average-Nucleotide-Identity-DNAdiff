#!/usr/bin/python3
import argparse
import subprocess
import sys
import os
import shlex
from multiprocessing import Pool 

parser = argparse.ArgumentParser()
parser.add_argument("-t", help = "Number of threads to use", type = int)
parser.add_argument("file", nargs='+')
parser.add_argument("-o", help = "Name of the outputfile")
args = parser.parse_args()
outputfile = args.o
list_files = args.file
threads = args.t
def identity(files):	
	pos1 = files[0]
	pos2 = files[1]
	cmd = "dnadiff -p "+str(files[0]+files[1])+" "+files[0]+" "+files[1]
	os.system(cmd)
	getani="head -19 "+str(files[0]+files[1])+".report | tail -1 | awk '{{print $2}}'"
	var = os.popen(getani).readlines()
	string=("".join(str(elem) for elem in var)).strip('\n')
	rm="rm "+str(files[0]+files[1])+"*"
	os.system(rm)
	return pos1, pos2, string
output_matrix = []
temp_list=[" "]
for val in list_files:
	temp_list.append(val)
list_files = []
m=len(temp_list)
l = []
for i in range(1,m):
	for j in range(1,m):
		if temp_list[i] == temp_list[j]:
			break
		else:
			temp = list((temp_list[i], temp_list[j]))
			l.append(temp)

for i in range(m):
	col = []
	for j in range(m):
		col.append('0')		
	output_matrix.append(col)
for i in range(m):
	for j in range(m):
		if i == j:		
			output_matrix[i][j] = '100'
		else:
			output_matrix[i][0] = temp_list[i]
			output_matrix[0][i] = temp_list[i]

p = Pool(threads)
t = p.map(identity,l)
tup = ()
for x in t:
	tup += tuple(x) 
c = len(output_matrix)
d = len(tup)
for i in range(c):
	for j in range(c):
		for k in range(d):
			if output_matrix[i][0]==tup[k] and output_matrix[0][j]==tup[k+1]:
				output_matrix[i][j] = tup[k+2]
				output_matrix[j][i] = tup[k+2]
# with open('outputfile', 'w') 
outputfile = open(outputfile, 'w')
for line in output_matrix:
	for k in line:
		print(k, end='\t', file = outputfile)
	print('\n', file=outputfile)
outputfile.close()




	

	




		






		





















