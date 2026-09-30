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
             UI                    DOCKET                    MATTER
              │                       │                        │
              │ create_matter(...)    │                        │
              ├──────────────────────►│                        │
              │ create_action(...)    │                        │
              ├──────────────────────►│                        │
              │                       │                        │
              │                       │ find matter            │
              │                       │                        │
              │                       │ enqueue(action)        │
              │                       ├───────────────────────►│
              │                       │                        │
              │ peel()                │                        │
              ├──────────────────────►│                        │
              │                       │ dequeue()              │
              │                       ├───────────────────────►│
              │                       │                        │
              │                       │       push(action)     │
              │                       │◄───────────────────────┤
              │                       │                        │
              │       actions         │                        │
              │◄──────────────────────┤                        │
              │                       │                        │
              │ revert(action)        │                        │
              ├──────────────────────►│                        │
              │                       │ enqueue(action)        │
              │                       ├───────────────────────►│
              │                       │                        │
              │ complete(action)      │                        │
              ├──────────────────────►│                        │
              │                       │                        │
              │                       │ mark done in matter    │
              │                       │                        │

1. UI talks only to Docket.

2. Docket owns the collection of Matters and the active heap.

3. Matter owns its action queue.

4. An action is either:
       a. in exactly one Matter queue, or
       b. active/in the Docket heap,
   but never both.

5. Creating an action always goes through Docket.
   Docket finds or creates the Matter, then enqueues it.

6. Docket is the only thing that moves actions
   between Matter queues and the heap.

7. UI never manipulates a Matter queue directly.

8. peel() removes an action from its Matter before
   making it active.

9. revert() puts the active action back into its Matter.

10. complete() removes the active action from heap.
