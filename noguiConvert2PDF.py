import os
import img2pdf
import glob
import pathlib

def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders

ext = ['png', 'jpg', 'gif']

dirPath = pathlib.Path("F:/Manga/Inuyasha_test/")
dirList = fast_scandir(dirPath)

print (dirPath.name)

if len(dirList) == 1:
	outputPath = dirPath.parent
else:
	outputPath = dirPath

for path in dirList:
    files = []
    path = pathlib.Path(path)
    outputPDFPath = outputPath / path.name
    [files.extend(glob.glob(str(path / "*") + e)) for e in ext]
    if len(files) > 0:

        with open(str(outputPDFPath) + ".pdf", "wb") as f:
           	try:
           		f.write(img2pdf.convert(files))
           		print (str(path.name)+" -- Converted")
           	except:
           		print("Please choose valid Folder")