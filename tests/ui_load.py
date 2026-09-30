import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SAVEFILE = PROJECT_ROOT / "data"/ "actions.tsv"

from libdocket import Matter
from libdocket import Docket

if __name__ == "__main__":
	### create flow
	docket = Docket(5)
	matter1 = docket.create_matter("nebula", "2026-12-31", "persist 10k")
	docket.create_action("build out UI", matter1)
	
	## docket visualization flow
	docket.peel()
	docket.today()
	
	## saving flow
	docket.save(SAVEFILE)

	## load flow
	docket2 = Docket.from_load(SAVEFILE, k=3)
	docket2.peel()
	docket2.today()
