'''
	Author : ANIKET VERMA 
	Enroll : 0827CO191012
	FCFS with zero arrivial timw
	takeInput() -> takes input form user
	rearrange() -> sort process in ascending order.
	waiting() -> calculate total waiting time
	turntime -> calculate turn around time
	printData() -> print all process with waiting and turn around time in tabular form.
	Process -> represent class of all process
	SJF -> represent class of all operation performed on SJF process	
'''

class Process:
	def __init__(self,id,bt):
		self.id=id
		self.bt=bt


class SJF:

	def takeInput(self):
		temp = []
		n = int(input("Enter No. of Process : "))
		for i in range(n):
			print("Process ID :",i+1)
			bt = int(input("Burst Time : "))
			p = Process(i+1,bt)
			temp.append(p)
		return temp

	
	def rearrange(self,process):
		return sorted(process,key=lambda item:item.bt)

	def printData(self,process,turn,wait,sumW,sumT):
		n = len(process)
		print("Process ID  Burst Time  Turnaround Time  Waiting Time")
		for i in range(n):
			print(process[i].id,"\t\t",process[i].bt,"\t\t",turn[i],"\t\t",wait[i])
		print("Average Waiting Time : ",sumW/n)
		print("Average Turn Around Time : ",sumT/n)	

	def waiting(self,process):
		wait = [0]
		sumW = 0
		x=0
		n=len(process)
		for i in range(1,n):
			x = wait[i-1] + process[i-1].bt
			wait.append(x)
			sumW+=x
		return sumW,wait

	def turnTime(self,wait,process):
		n = len(process)
		turn=[]
		sumT=0
		for i in range(n):
			x=wait[i]+process[i].bt
			turn.append(x)
			sumT+=x
		return sumT,turn


s = SJF()
process = s.takeInput()
process = s.rearrange(process)
sumW,wait = s.waiting(process)
sumT,turn = s.turnTime(wait,process)
s.printData(process,turn,wait,sumW,sumT)




