import os, sys

uiFiles = os.scandir("assets/qt/ui/")
for i in uiFiles:
	tempname = i.name.replace(".ui", "")
	os.system(f'pyside6-uic assets/qt/ui/{i.name} -o {tempname}.py')
