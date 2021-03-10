import sys, os, json

sourceFolder = "D:/logs"
allowedExt = ["log"]
destFile = "merged.log"

dest = open(os.path.join(sourceFolder, destFile), "a") #Append

for root, dirs, files in os.walk(sourceFolder):
    for filename in files:
        ext = filename.split(".")[-1]
        filePath = os.path.join(root, filename)

        if ext in allowedExt:
        	f = open(filePath, "r")
        	dest.write(f.read())
        	f.close()

print("Done")
dest.close()