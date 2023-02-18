import subprocess
import os

for filename in os.listdir(f"{os.getcwd()}/task"):
    if filename != "flag.py":
        text = subprocess.run(["gocr", f"{os.getcwd()}/task/{filename}"], stdout=subprocess.PIPE).stdout  # works only for Linux machines
        if "{" in str(text):
            print(filename, text.decode("utf-8"))  # GOCR recognized "0" as "O". After checking it manually, I entered the correct key "Skill{1_ju87_w4n7_70_s4y_u_f0und_17}
