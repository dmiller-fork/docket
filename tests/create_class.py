import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from libdocket import Matter
from libdocket import Docket

if __name__ == "__main__":
	matter1 = Matter("nebula", "2026-09-26")
	docket = Docket(5)
