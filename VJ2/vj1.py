import magic
import glob
import os.path as path

FOLDER = "Lab2_download_1\\*"

OUTPUT = "LAB2_dokaz.txt"

with open(OUTPUT, "w") as out:
    files = glob.glob(FOLDER)
    for file in files:
        if path.isfile(file) is True:
            info = f"{file} :: {magic.from_file(file)}\n"
            print(info)
            out.write(info)
