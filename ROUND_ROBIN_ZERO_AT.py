'''
	Author : ANIKET VERMA 
	Enroll : 0827CO191012
	FCFS with zero arrivial timw
	takeInput() -> takes input form user
	waiting() -> calculate total waiting time
	turntime -> calculate turn around time
	printData() -> print all process with waiting and turn around time in tabular form.
	makecopy() -> make copy of list
	Process -> represent class of all process
	Round Robin -> represent class of all operation performed on RR process	
'''

class Process:
	def __init__(self,id,bt):
		self.id=id
		self.bt=bt


class RoundRobin:

	def takeInput(self):
		temp = []
		total=0
		n = int(input("Enter No. of Process : "))
		q = int(input("Time Quantum : "))
		for i in range(n):
			print("Process ID :",i+1)
			bt = int(input("Burst Time : "))
			total+=bt
			p = Process(i+1,bt)
			temp.append(p)
		return temp,total,q

		
	def printData(self,process,turn,wait,sumW,sumT):
		n = len(process)
		print("Process ID  Burst Time  Turnaround Time  Waiting Time")
		for i in range(n):
			print(process[i].id,"\t\t",process[i].bt,"\t\t",turn[i],"\t\t",wait[i])
		print("Average Waiting Time : ",sumW/n)
		print("Average Turn Around Time : ",sumT/n)	

	def turntime(self,process,total,tq):
		sumT = 0
		x=0
		n=len(process)
		turn = [0]*n
		temp=0
		while temp!=total:
			for i in range(n):
				if process[i].bt>0:
					if process[i].bt > tq:
						temp+=tq
						process[i].bt-=tq
					else:
						temp+=process[i].bt
						turn[i] = temp
						sumT+=turn[i]
						process[i].bt=0

		return sumT,turn

	def waiting(self,turn,process):
		n = len(process)
		wait=[0]*n
		sumW=0
		for i in range(n):
			wait[i] = turn[i]-process[i].bt
			sumW+=wait[i]
		return sumW,wait

	def makeCopy(self,process):
		copy = [0]*(len(process))
		for i in range(len(process)):
			copy[i] = Process(process[i].id,process[i].bt)
		return copy



r = RoundRobin()
process,total,q = r.takeInput()
copy=r.makeCopy(process)


sumT,turn = r.turntime(copy,total,q)
sumW,wait = r.waiting(turn,process)
r.printData(process,turn,wait,sumW,sumT)