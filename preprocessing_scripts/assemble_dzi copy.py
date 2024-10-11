# /// script
# dependencies = ["pyvips"]
# ///
import pyvips
from pathlib import Path


for lamella in Path("/nrs/elferich/candida_project/Montages").glob("*/*_filtered.png"):


    bl = pyvips.Image.new_from_file(lamella )



    bl.dzsave( Path("/nrs/elferich/candida_project/Montages/dzi/") / lamella.with_suffix("").name,suffix=".png")
