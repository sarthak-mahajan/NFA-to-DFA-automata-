import json
import os

if os.path.exists("output.json"):
  os.remove("output.json")
else:
  pass

with open("input.json") as inp:
	nf = json.load(inp)
	bi=0
	# print(nf["t_func"])
	states2=[]
	dfa_fin=[]
	states1=[]
	power_state=[]
	start=[]
	start.append(nf["start"])
	y=[]
	t_func=[]
	# t_func2=[]
	# func=[]
	stat_no=2**nf["states"]
	for i in range (0,nf["states"]):
		states1.append(i)
	# print(bin(5)[2:].zfill(5))
	for i in range(0,stat_no):
		y=bin(i)[2:].zfill(nf["states"])
		states2.append(y)
	for i in range(0,stat_no):
		y2=[]
		for j in range(0,nf["states"]):
			if states2[i][j]=='1':
				y2.append(nf["states"]-1-j)
		# print(y2)	
		power_state.append(list(y2))
	for i in power_state:
		func=[]
		out_state=[]
		# func.append(i)
		# if i==[]:
		# 		for trans_nfa in nf["letters"]:
		# 			func.append([])
		# 			func.append(trans_nfa)
		# 			func.append([])
		# 			# assert len(func)==3
		# 			t_func.append(list(func))
		# 			func=[]
					# mot sure after this
		for l in nf["letters"]:
			for trans_nfa in nf["t_func"]:
				for j in i:
					if trans_nfa[0]==j and trans_nfa[1]==l:
						# func.append(trans_nfa[1])
						out_state.extend(list(trans_nfa[2]))
			func.append(i)			
			func.append(l)
			func.append(list(out_state))
			out_state=[]
			t_func.append(list(func))
			func=[]
	for i in power_state:
		for j in i:
			for k in nf["final"]:
				if k==j:
					bi=1
		if bi ==1:
			bi=0
			dfa_fin.append(i)




	res={}
	res["states"]=power_state
	res["letters"]=nf["letters"]
	res["t_func"]=t_func
	res["start"]=start
	res["final"]=dfa_fin

with open('output.json', 'w') as json_file:
  json.dump(res, json_file,indent=3)






	# print(dfa_fin)





