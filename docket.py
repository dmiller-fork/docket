import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

PROJECT_ROOT = Path(__file__).resolve().parent
SAVEFILE = PROJECT_ROOT / "data"/ "actions.tsv"

from libdocket import Matter
from libdocket import Docket

def main():
	docket = Docket.from_load(SAVEFILE, 5)

	print("Docket REPL")
	print("Commands: add, peel, today, quit")

	while True:
		try:
			command = input("> ").strip()

			if command == "quit":
				break

			elif command == "today":
				for tup in docket.today():
					print(f"{tup[0].isoformat()} {tup[2]}: {tup[1]}")
				   

			elif command == "peel":
				docket.peel()
					

			elif command == "add":
				line = input(
					"matter | deadline | outcome | action: "
				).strip()

				matter_name, deadline, outcome, action = (
					part.strip() for part in line.split("|")
				)

				matter = Matter(
					matter_name,
					deadline,
					outcome
				)

				docket.matters.append(matter)
				docket.add(matter.deadline, action, matter)
				print("BEFORE SAVE")
				print("MATTERS:")
				for matter in docket.matters:
					print(matter.name, matter.deadline, matter.outcome, list(matter.actions))

				print("HEAP:")
				print(docket.heap)

				docket.save(SAVEFILE)
				print("AFTER SAVE")

			else:
				print("Unknown command")

		except (EOFError, KeyboardInterrupt):
			print()
			break


if __name__ == "__main__":
	main()

