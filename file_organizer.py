import os

files = os.listdir()

for file in files:
    if "." in file:
        ext = file.split(".")[-1]
        folder = ext + "_files"

        if not os.path.exists(folder):
            os.mkdir(folder)

        os.rename(file, folder + "/" + file)

print("Files organized successfully!")
