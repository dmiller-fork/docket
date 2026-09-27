import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SAVEFILE = PROJECT_ROOT / "data"/ "actions.tsv"

from libdocket import Matter
from libdocket import Docket

if __name__ == "__main__":
	matter1 = Matter("Gardening", "2026-09-30", "Practical Knowledge of how to grow your own food")
	matter1.enqueue("Harvest Plants")
	matter1.enqueue("Plant New Plants")

	matter2 = Matter("Home Improvement", "2026-09-30", "Save and Useable home")
	matter2.enqueue("Break down crib")
	matter2.enqueue("Clean Garage")

	docket = Docket(k=3)
	docket.matters = [matter1, matter2]

	docket.peel()
	docket.save(SAVEFILE)
	docket2 = Docket.from_load(SAVEFILE, k=3)
	docket2.peel()
	for tup in docket2.today():
		print(f"{tup[0].isoformat()} {tup[2]}: {tup[1]}")
