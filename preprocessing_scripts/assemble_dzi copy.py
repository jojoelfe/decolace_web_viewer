# /// script
# dependencies = ["pyvips"]
# ///
import pyvips
from pathlib import Path



lamella = Path("/home/elferich/Pictures/montage.png")


bl = pyvips.Image.new_from_file(lamella )



bl.dzsave( Path("/home/elferich/Pictures/dzi") / "montage",suffix=".png")
