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
	print("Commands: matter, action, today, quit")

	while True:
		try:
			command = input("> ").strip()

			if command == "quit":
				break

			elif command == "today":
				docket.peel()
				docket.today()

			elif command == "matter":
				line = input(
					"matter | deadline | outcome\n"
				).strip()

				matter_name, deadline, outcome = (
					part.strip() for part in line.split("|")
				)

				matter = docket.create_matter(
					matter_name,
					deadline,
					outcome
				)
			elif command == "action":
				line = input(
					"matter | action\n"
				).strip()

				matter_name, action = (
					part.strip() for part in line.split("|")
				)

				for matter in docket.matters:
					# print(repr(matter.name), repr(matter_name))
					if matter.name == matter_name:
						docket.create_action(action, matter)
						break
				else:
					raise Exception("matter not found")	
			else:
				print("Unknown command")

		except (EOFError, KeyboardInterrupt):
			print()
			break


if __name__ == "__main__":
	main()

