import heapq
from collections import deque
from datetime import date
from datetime import timedelta

class Matter:
	def __init__(self, name, deadline, outcome=None):
		self.name = name
		self.deadline = date.fromisoformat(deadline)
		self.outcome = outcome
		self.actions = deque()

	def enqueue(self, action):
		self.actions.append(action)

	def dequeue(self):
		return self.actions.popleft()

class Docket:
	def __init__(self, k):
		self.k = k
		self.heap = []
		self.matters = []

	@classmethod
	def from_load(cls, filename, k):
		docket = cls(k)

		matters = {}

		with open(filename) as f:
			for line in f:
				name, deadline, outcome, action = line.rstrip("\n").split("\t")

				if name not in matters:
					matter = Matter(name, deadline, outcome)
					matters[name] = matter
					docket.matters.append(matter)

				matters[name].actions.append(action)

		return docket
	
	def create_matter(self, name, deadline, outcome):
		matter = Matter(name, deadline, outcome)
		self.matters.append(matter)
		#for i, matter in enumerate(self.matters):
			# print(i, repr(matter), repr(matter.name))
		return matter
	
	def create_action(self, action, matter):
		self._revert()
		if matter not in self.matters:
			raise ValueError("Matter is not in docket")
		matter.enqueue(action)	
	
	def _push(self, deadline, action, matter):
		## private method to add to heap
		## first divide up days based on actions
		today = date.today()
		days = (deadline - today).days
		delta = timedelta(days=round(days / (len(matter.actions) + 1)))
		duedate = today + delta
		## then create entry 
		entry = (duedate, action, matter)
		if len(self.heap) < self.k:
			heapq.heappush(self.heap, entry)
			return None
		elif duedate > self.heap[0][0]:
			return heapq.heapreplace(self.heap, entry)
	def peel(self):
		for matter in self.matters:
			if not matter.actions:
				pass
			else:
				replaced = self._push(
					matter.deadline, 
					matter.dequeue(), 
					matter
				)
				if replaced is not None:
					replaced[2].actions.appendleft(replaced[1])

	def today(self):
		actions = [
			(duedate, action, matter.name)
			for duedate, action, matter 
			in sorted(self.heap, reverse=True)
		]
		for tup in actions:
			print(f"{tup[0].isoformat()} {tup[2]}: {tup[1]}")
	def _revert(self):
		while self.heap:
			entry = heapq.heappop(self.heap)
			entry[2].actions.appendleft(entry[1])

	def save(self, filename):
		self._revert()

		with open(filename, "w") as f:

			for matter in self.matters:
				for action in matter.actions:
					f.write(
						f"{matter.name}\t"
						f"{matter.deadline.isoformat()}\t"
						f"{matter.outcome}\t"
						f"{action}\n"
					)
