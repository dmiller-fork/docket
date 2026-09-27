I've played around a little bit, and I think I've got it.
This project has three classes:
# classes
	- Action
	- Docket
	- Matter

# data structures
Action.action is just a dictionary
Docket.docket is a heap
Matter.matter is a deque

# workflow is intake flow and 
	Create Matters -> add actions to matters -> create dockets
	docket.peel() -> iterate through matters, popleft for each matter
		-> docket heap sorts by distance to expiration date
		-> any action that doesn't make it gets put back on the matter

