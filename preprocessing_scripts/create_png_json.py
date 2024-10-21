import sys
from pathlib import Path
import json

# Finall all pngs in the folder given as an argument
data = {"datasets" : []}
for lamella in Path(sys.argv[1]).glob("*mrc.png"):
    if "27_C_" in lamella.with_suffix("").name:
        name = f"Control {lamella.with_suffix('').name.split('_')[3]}"
    elif "27_drug_" in lamella.with_suffix("").name:
        name = f"Drug {lamella.with_suffix('').name.split('_')[3]}"
    elif "27_fil_90min_glyc" in lamella.with_suffix("").name:
        name = f"Filamentous glycerol {lamella.with_suffix('').name.split('_')[4]}"
    elif "27_fil_90min_g2" in lamella.with_suffix("").name:
        name = f"Filamentous noglycerol {lamella.with_suffix('').name.split('_')[4]}"
    elif "27_fil_C_glyc" in lamella.with_suffix("").name:
        name = f"Filamentous Control glycerol {lamella.with_suffix('').name.split('_')[4]}"
    else:
        raise ValueError(f"Unknown lamella name: {lamella.with_suffix('').name}")
    data["datasets"].append({"name": name, 
                             "micrograph": {
                                "default": f"http://www.s1023143047.onlinehome.us/candida/{str(lamella.name)}"
                             },
                             "match_overlays": [
                                {
                                    "name": "60S",
                                    "default": f"http://www.s1023143047.onlinehome.us/candida/{str(lamella.with_suffix('').name).replace('montage_filtered.mrc','3_tm_package_filtered_assembly')}.png"
                                },
                                {
                                    "name": "FAS",
                                    "default": f"http://www.s1023143047.onlinehome.us/candida/{str(lamella.with_suffix('').name).replace('montage_filtered.mrc','4_tm_package_filtered_assembly')}.png"
                                },
                                {
                                    "name": "tiles",
                                    "default": f"http://www.s1023143047.onlinehome.us/candida/{str(lamella.with_suffix('').name).replace('montage_filtered.mrc','tile_overlay')}.png"
                                }
                             ]})
data["datasets"].sort(key=lambda x: x["name"])

# Write the json to the output file
with open(sys.argv[2], "w") as f:
    json.dump(data, f, indent=4)