import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from libdocket import Matter
from libdocket import Docket

if __name__ == "__main__":
	docket = Docket(5)
	matter1 = docket.create_matter("nebula", "2026-12-31", "persist 10k")
	docket.create_action("build out UI", matter1)
	docket.peel()
	docket.today()
