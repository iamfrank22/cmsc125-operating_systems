import random
import time
import os
import sys

class Process:
	"""defining each process"""
	def __init__(self, name, id_num):
		self.id_num = id_num
		self.name = "P" + name
		self.arrival_time = random.randint(0, 100)
		self.burst_time = random.randint(1, 10)
		self.priority = random.randint(1, 100)
		self.waiting_time = 0


class CPU_Scheduling:
	def __init__(self):
		self.process = []
		self.waiting_time = []
		self.burst_time = []

	def add_process(self):
		for process in range(1, generate_process() + 1):
			job = Process(str(process), process)
			self.process.append(job)
	
	def add_burst_time(self):
		for job in self.process:
			self.burst_time.append(job.burst_time)

	def max_burst_time(self):
		return max(self.burst_time)

	def find_waiting_time(self):
		for index in range(0, len(self.process)):
			if index == 0:
				waiting_time = 0
			if(index is not 0):
				waiting_time = self.waiting_time[index - 1] + self.burst_time[index - 1]
			self.waiting_time.append(waiting_time)

		i = 0
		for job in self.process:
			job.waiting_time = self.waiting_time[i]
			i+=1

	def compute_waiting_time(self):
		total_wt = 0
		for i in self.waiting_time:
			total_wt += i
		return total_wt

	def compute_avg_waiting_time(self, total_wt):
		avg_wt = float(total_wt / len(self.process))
		return avg_wt

	def printp(self):
		print("process\t\tarrival\t\tburst\t\tpriority\twaiting\n")
		for process in self.process:
			print('{}\t\t{}\t\t{}\t\t{}\t\t{}'.format(
            process.name, process.arrival_time,
            process.burst_time, process.priority, process.waiting_time))

	def sum_burst_time(self):
		sum = 0
		for i in self.burst_time:
			sum += i
		return sum

	def fcfs(self):
		print("\n\n-------First Come First Served------")
		gantt_chart = []
		for jobs in self.process:
			for j in range(0, jobs.burst_time):
				gantt_chart.append(jobs.id_num)
		
		return gantt_chart

	def nonpreemptive_sjf(self):
		print("\n\n-------Nonpreemptive Shortest Job First------")
		swap_list = []
		gantt_chart = []
		index1 = 0
		for jobs in self.process:
			temp = index1
			for index2 in range(index1 + 1, len(self.process)):
				if self.process[index2].burst_time < self.process[temp].burst_time:
					temp = index2
				
			if temp != index1:
				swap_list = self.process[temp]
				self.process[temp] = self.process[index1]
				self.process[index1] = swap_list
			index1 += 1
		
		for process in self.process:
			for j in range(0, process.burst_time):
				gantt_chart.append(process.id_num)
		
		return gantt_chart

	# def preemptive_sjf(self):
	# 	print("\n\n-------Preemptive Shortest Job First------")
	# 	waiting_list = []

	# 	for jobs in self.process:
			

	def nonpreemptive_priority(self):
		print("\n\n-------Nonpreemptive Priority------")
		swap_list = []
		gantt_chart = []
		index1 = 0
		for jobs in self.process:
			temp = index1
			for index2 in range(index1 + 1, len(self.process)):
				if self.process[index2].priority < self.process[temp].priority:
					temp = index2
				
			if temp != index1:
				swap_list = self.process[temp]
				self.process[temp] = self.process[index1]
				self.process[index1] = swap_list
			index1 += 1
		
		for process in self.process:
			for j in range(0, process.burst_time):
				gantt_chart.append(process.id_num)
		
		return gantt_chart


"""generating an integer 
to represent the initial number of processes"""
def generate_process():
    return random.randint(1, 10)

"""generating a random number for quantum time"""
def generate_quantum_time():
	return random.randint(1, 49)

def GanttOutput(GanttChart):
	firstLine = "|"
	aboveLine = "____"
	underLine = "‾‾‾‾"
	secondLine = "0"

	timer = len(GanttChart)
	for i in range(0, timer):
		firstLine = firstLine + "P" + str(GanttChart[i]) + "|"
		if i < 10:
			secondLine = secondLine + "  " + str((i + 1))
		else:
			secondLine = secondLine + " " + str((i + 1))
		time.sleep(.3)
		os.system('CLS')
		print(aboveLine + "\n" + firstLine + "\n" + underLine + "\n" + secondLine)
		underLine += "‾‾‾"
		aboveLine += "___"

def main():
	gen = CPU_Scheduling()
	gen.add_process()
	gen.add_burst_time()
	gen.find_waiting_time()
	gen.printp()

	while(1):
		print("CPU Scheduling")
		print("\nEnter the type of scheduling...")
		print("1 for First Come First Served")
		print("2 for Nonpreemptive Shortest Job First")
		print("3 for Preemptive Shortest Job First")
		print("4 for Nonpreemptive Priority")
		print("5 for Preemptive Priority")
		print("6 for Round Robin")
		print("7 for Quit")
		print()
		
		scheduler = int(input())
		
		gantt_chart = []

		if scheduler is 1:
			gantt_chart = gen.fcfs()

		elif scheduler is 2:
			gantt_chart = gen.nonpreemptive_sjf()
		
		elif scheduler is 3:
			gantt_chart = gen.preemptive_sjf()
		
		elif scheduler is 4:
			gantt_chart = gen.nonpreemptive_priority()
		
		# elif scheduler is 5:
		# 	gantt_chart = gen.preemptive_priority()

		# elif scheduler is 6:
		# 	gantt_chart = gen.round_robin()

		else:
			sys.exit(0)	

		print("GanttChart :") 
		print(GanttOutput(gantt_chart))

		if scheduler is 1 or scheduler is 2 or scheduler is 4:
			print("Ave. waiting time: ", gen.compute_avg_waiting_time(gen.compute_waiting_time()))
		
		elif scheduler is 3:
			print("Ave. waiting time: ", gen.compute_avg_waiting_time(gen.compute_waiting_time()))

if __name__ == '__main__':
    main()