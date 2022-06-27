from traceback import print_list
import magic
import glob
import os.path as path
import hashlib

FOLDER = "vj3\\*"

OUTPUT = "LAB3_hash.txt"

with open(OUTPUT, "w") as out:
    files = glob.glob(FOLDER)
    for file in files:
        if path.isfile(file) is True:
            out_contents = []
            file_contents = open(file, "rt", encoding="ISO-8859-1").read().encode("ISO-8859-1")
            out_contents.append(f"================ {file} ================\n")
            out_contents.append(f"MD5: {hashlib.md5(file_contents).hexdigest()}\n")
            out_contents.append(f"SHA1: {hashlib.sha1(file_contents).hexdigest()}\n")
            out_contents.append(f"SHA256: {hashlib.sha256(file_contents).hexdigest()}\n")
            out.writelines(out_contents)
            out_contents_joined = " ".join(out_contents)
            print(out_contents_joined)
