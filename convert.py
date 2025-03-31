import subprocess
import shutil
import os

executable = r".\ffmpeg.exe"

name = input(r"Directory to file (C:\Path\To\File.mp4 or File.mp4: ").replace('"', '')
new = name
if len(name.split(" ")) != 1:
    new = name.replace(" ", "_")

amt = []
for path in new.split("\\"):
    if len(amt) == 0:
        amt.append(path)
    else:
        tmp = []
        for path1 in path.split("."):
            tmp.append(''.join(e for e in path1 if e.isalnum()))
        amt.append(".".join(tmp))

new = "\\".join(amt)
if name != new:
    shutil.copy(name, new)

output = input("Output filetype e.g. mp3: ")

subprocess.call([executable, "-i", new, f"{name.split('.')[0]}.{output}"])
if new != name:
    os.remove(new)
