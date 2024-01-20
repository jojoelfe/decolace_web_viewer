import pyvips
from pathlib import Path

blender_output_path = Path("../new_blender_approach/output/")
dzi_path = Path("../dzi/")

lamellae = blender_output_path.glob("*")

for lamella in lamellae:
    lamella_name = lamella.name
    if lamella_name in ["micrograph", "ribosomes", "ribosomes_dc"]:
        continue
    bl = pyvips.Image.new_from_file(lamella / "micrograph/tl.png")
    br = pyvips.Image.new_from_file(lamella / "micrograph/tr.png")
    tl = pyvips.Image.new_from_file(lamella / "micrograph/bl.png")
    tr = pyvips.Image.new_from_file(lamella / "micrograph/br.png")

    out = pyvips.Image.arrayjoin([bl, br, tl, tr], across=2)
    print(out.width)
    res = out.resize(0.33)
    print(res.width)
    res.dzsave(dzi_path / lamella_name / "micrograph",suffix=".png")

    bl = pyvips.Image.new_from_file(lamella / "ribosomes/tl.png")
    br = pyvips.Image.new_from_file(lamella / "ribosomes/tr.png")
    tl = pyvips.Image.new_from_file(lamella / "ribosomes/bl.png")
    tr = pyvips.Image.new_from_file(lamella / "ribosomes/br.png")

    out = pyvips.Image.arrayjoin([bl, br, tl, tr], across=2)
    print(out.width)

    out.dzsave(dzi_path / lamella_name / "ribosomes",suffix=".png")

    bl = pyvips.Image.new_from_file(lamella / "ribosomes_dc/tl.png")
    br = pyvips.Image.new_from_file(lamella / "ribosomes_dc/tr.png")
    tl = pyvips.Image.new_from_file(lamella / "ribosomes_dc/bl.png")
    tr = pyvips.Image.new_from_file(lamella / "ribosomes_dc/br.png")

    out = pyvips.Image.arrayjoin([bl, br, tl, tr], across=2)
    print(out.width)

    out.dzsave(dzi_path / lamella_name / "ribosomes_dc",suffix=".png")